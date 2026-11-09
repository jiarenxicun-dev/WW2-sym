/**
 * AIWA Web Command — フロントエンドアプリケーション
 * - 平時マップ（欧州・地中海プロビンス運営・建国・白地購入・バケツ塗り・平時ワープ）
 * - 戦時マップ（分離型戦術作戦ボード・NATO部隊シンボル移動・進軍矢印描画・AI審判）
 * - 陸海空・施設編成シミュレーター＆Discord連携
 */

let APP_STATE = null;
let CATALOG = null;
let SELECTED_PROV_ID = null;
let PEACE_TOOL = "inspect"; // inspect | found | bucket
let FOUND_SELECTION = { capital: null, cities: [], extra: [] };

// 平時マップ ズーム・パン状態
let PEACE_VB = { x: 150, y: 40, w: 1120, h: 920 };
let isPeacePanning = false;
let peacePanStart = { x: 0, y: 0 };

// 戦時マップ 状態
let ACTIVE_WAR_ID = null;
let WAR_TOOL = "move"; // move | add_unit | draw_attack | draw_defend | draw_naval | draw_counter
let draggingUnitId = null;
let isDrawingArrow = false;
let currentDrawPoints = [];

// 師団ビルダー状態
let BUILDER_REGIMENTS = [
  { regiment_id: "reg_infantry", tank_id: null, custom_calc: false },
  { regiment_id: "reg_infantry", tank_id: null, custom_calc: false },
  { regiment_id: "reg_infantry", tank_id: null, custom_calc: false },
];
let BUILDER_ARTILLERY = "art_light";
let BUILDER_SUPPORTS = [{ support_id: "sup_at", tank_id: null, custom_calc: false }];
let BUILDER_OVERRIDE_COST = 380.0;

// ショップタブ状態
let ACTIVE_SHOP_DOMAIN = "navy"; // navy | air | facility

// PNGバケツ塗りキャンバス履歴
let pngUndoStack = [];

// ============================================================================
// ユーティリティ
// ============================================================================
function showToast(msg, isError = false) {
  const container = document.getElementById("toast-container");
  const el = document.createElement("div");
  el.className = "toast" + (isError ? " error" : "");
  el.textContent = msg;
  container.appendChild(el);
  setTimeout(() => el.remove(), 4200);
}

function formatOku(oku) {
  const val = Number(oku || 0);
  const cho = (val / 10000).toFixed(2);
  return `${cho}兆円 (${val.toLocaleString()}億)`;
}

async function apiPost(url, data = {}) {
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  const json = await res.json();
  if (!res.ok || json.ok === false) {
    throw new Error(json.error || "APIエラーが発生しました");
  }
  return json;
}

function getActiveNation() {
  if (!APP_STATE || !APP_STATE.nations) return null;
  return (
    APP_STATE.nations.find((n) => n.id === APP_STATE.active_nation_id) ||
    APP_STATE.nations[0] ||
    null
  );
}

function getActiveWar() {
  if (!APP_STATE || !APP_STATE.wars || !APP_STATE.wars.length) return null;
  return (
    APP_STATE.wars.find((w) => w.id === ACTIVE_WAR_ID) || APP_STATE.wars[0]
  );
}

function getAllTanks() {
  if (!CATALOG) return [];
  return [...(APP_STATE?.custom_tanks || []), ...CATALOG.tanks];
}

// ============================================================================
// 初期化＆WebSocket同期
// ============================================================================
async function initApp() {
  try {
    const res = await fetch("/api/bootstrap");
    const data = await res.json();
    CATALOG = data.catalog;
    APP_STATE = data.state;
    if (APP_STATE.wars && APP_STATE.wars.length > 0) {
      ACTIVE_WAR_ID = APP_STATE.wars[0].id;
    }
    setupEventListeners();
    initPngPainterCanvas();
    renderAll();
    connectWebSocket();
    fetchDiscordLogs();
  } catch (err) {
    showToast("初期データの読み込みに失敗しました: " + err.message, true);
  }
}

function connectWebSocket() {
  const proto = location.protocol === "https:" ? "wss:" : "ws:";
  const ws = new WebSocket(`${proto}//${location.host}/ws`);
  ws.onmessage = (ev) => {
    try {
      const msg = JSON.parse(ev.data);
      if (msg.state) {
        APP_STATE = msg.state;
        renderAll();
      }
    } catch (e) {}
  };
  ws.onclose = () => setTimeout(connectWebSocket, 4000);
}

// ============================================================================
// 全体レンダリング
// ============================================================================
function renderAll() {
  if (!APP_STATE || !CATALOG) return;
  renderTopbar();
  renderPeacetimeMap();
  renderProvinceInspectPanel();
  renderPeacetimeNationList();
  renderWartimeTab();
  renderMilitaryTab();
  renderDiplomacyTab();
}

function renderTopbar() {
  document.getElementById("ui-week").textContent = `第${APP_STATE.week}週 (木曜支給)`;
  document.getElementById("select-game-mode").value = APP_STATE.mode || "sandbox";

  const sel = document.getElementById("select-active-nation");
  const currentId = APP_STATE.active_nation_id;
  sel.innerHTML = "";
  for (const nat of APP_STATE.nations) {
    const opt = document.createElement("option");
    opt.value = nat.id;
    opt.textContent = `${nat.flag} ${nat.name} (${nat.leader})`;
    if (nat.id === currentId) opt.selected = true;
    sel.appendChild(opt);
  }

  const activeNat = getActiveNation();
  const aiBadge = document.getElementById("ui-nation-ai-badge");
  if (activeNat) {
    document.getElementById("ui-nation-budget").textContent = formatOku(activeNat.budget);
    const bonus = Math.min(1000, Number(activeNat.war_prov_bonus_oku || 0));
    document.getElementById("ui-nation-income").textContent = `+${(Number(activeNat.weekly_income || 5000) + bonus).toLocaleString()}億/週`;
    aiBadge.style.display = activeNat.is_ai ? "inline-block" : "none";
  } else {
    document.getElementById("ui-nation-budget").textContent = "未建国";
    document.getElementById("ui-nation-income").textContent = "";
    aiBadge.style.display = "none";
  }

  // バケツ塗り用セレクト更新
  const bucketSel = document.getElementById("select-bucket-owner");
  const prevBucket = bucketSel.value;
  bucketSel.innerHTML = `<option value="">🏳️ 白地に戻す (未領有化)</option>`;
  for (const nat of APP_STATE.nations) {
    const opt = document.createElement("option");
    opt.value = nat.id;
    opt.textContent = `${nat.flag} ${nat.name}`;
    bucketSel.appendChild(opt);
  }
  if (prevBucket) bucketSel.value = prevBucket;
  else if (activeNat) bucketSel.value = activeNat.id;

  // アクティブ戦争数バッジ
  document.getElementById("badge-active-wars").textContent = (APP_STATE.wars || []).length;
}

// ============================================================================
// TAB 1: 平時マップ（欧州・地中海プロビンスSVGマップ）
// ============================================================================
const TERRAIN_COLORS = {
  plains: "#1e3a2f",
  urban: "#334155",
  mountain: "#3b2f2f",
  forest: "#143326",
  coastal: "#1c3545",
  desert: "#4a3b22",
};

function generateProvincePolygonPoints(prov, allProvs) {
  // 各プロビンスの中心(x,y)の周囲に8角形の有機的な領土ポリゴンを生成し、隣接プロビンスとの中点でクリップする
  const angles = 10;
  const baseRadius = 34;
  const pts = [];
  for (let i = 0; i < angles; i++) {
    const ang = (Math.PI * 2 * i) / angles;
    const dx = Math.cos(ang);
    const dy = Math.sin(ang);
    let r = baseRadius;

    // 近隣プロビンスとの重なりを抑えるボロノイ風クリッピング
    for (const other of allProvs) {
      if (other.id === prov.id) continue;
      const vx = other.x - prov.x;
      const vy = other.y - prov.y;
      const dist = Math.hypot(vx, vy);
      if (dist > 115 || dist < 1) continue;
      const dot = (vx * dx + vy * dy) / dist;
      if (dot > 0.25) {
        const maxR = (dist * 0.52) / dot;
        if (maxR < r) r = Math.max(15, maxR);
      }
    }
    pts.push(`${(prov.x + dx * r).toFixed(1)},${(prov.y + dy * r).toFixed(1)}`);
  }
  return pts.join(" ");
}

function renderPeacetimeMap() {
  const svg = document.getElementById("peacetime-svg");
  svg.setAttribute("viewBox", `${PEACE_VB.x} ${PEACE_VB.y} ${PEACE_VB.w} ${PEACE_VB.h}`);
  const showAdj = document.getElementById("chk-show-adj").checked;
  const showUnits = document.getElementById("chk-show-units").checked;

  const nationsById = {};
  for (const n of APP_STATE.nations) nationsById[n.id] = n;
  const provs = APP_STATE.provinces;
  const provById = {};
  for (const p of provs) provById[p.id] = p;

  // プロビンスごとの配備師団数を集計
  const divCountByProv = {};
  for (const n of APP_STATE.nations) {
    for (const d of n.divisions || []) {
      const pid = d.province_id || n.capital_id;
      if (!divCountByProv[pid]) divCountByProv[pid] = { count: 0, flag: n.flag, color: n.color };
      divCountByProv[pid].count += Number(d.count || 1);
    }
  }

  let html = `
    <defs>
      <pattern id="seaGrid" width="40" height="40" patternUnits="userSpaceOnUse">
        <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(148,163,184,0.06)" stroke-width="1"/>
      </pattern>
    </defs>
    <rect x="0" y="0" width="1600" height="1000" fill="url(#seaGrid)" />
    <!-- 海域名ラベル -->
    <text x="190" y="490" fill="rgba(148,163,184,0.25)" font-size="18" font-style="italic">大 西 洋 (ATLANTIC)</text>
    <text x="485" y="290" fill="rgba(148,163,184,0.25)" font-size="14" font-style="italic">北海</text>
    <text x="740" y="255" fill="rgba(148,163,184,0.25)" font-size="13" font-style="italic">バルト海</text>
    <text x="510" y="650" fill="rgba(148,163,184,0.28)" font-size="14" font-style="italic">リオン湾</text>
    <text x="730" y="810" fill="rgba(148,163,184,0.3)" font-size="17" font-style="italic">地 中 海 (MEDITERRANEAN SEA)</text>
    <text x="980" y="575" fill="rgba(148,163,184,0.25)" font-size="14" font-style="italic">黒海 (BLACK SEA)</text>
  `;

  // 1. 隣接ネットワーク線
  if (showAdj) {
    const drawnPairs = new Set();
    for (const p of provs) {
      for (const nbId of p.neighbors || []) {
        const pairKey = [p.id, nbId].sort().join("--");
        if (drawnPairs.has(pairKey)) continue;
        drawnPairs.add(pairKey);
        const nb = provById[nbId];
        if (!nb) continue;
        const isSeaLink = Math.hypot(p.x - nb.x, p.y - nb.y) > 95;
        html += `<line x1="${p.x}" y1="${p.y}" x2="${nb.x}" y2="${nb.y}"
          stroke="${isSeaLink ? "rgba(56,189,248,0.28)" : "rgba(148,163,184,0.22)"}"
          stroke-width="${isSeaLink ? "1.2" : "1.5"}"
          ${isSeaLink ? 'stroke-dasharray="4,4"' : ""} />`;
      }
    }
  }

  // 2. プロビンス領土ポリゴン描画
  for (const p of provs) {
    const owner = p.owner_id ? nationsById[p.owner_id] : null;
    const fill = owner ? owner.color : (TERRAIN_COLORS[p.terrain] || "#1e293b");
    const fillOpacity = owner ? "0.68" : "0.75";
    const isSelected = p.id === SELECTED_PROV_ID;
    const isFoundCap = FOUND_SELECTION.capital === p.id;
    const isFoundCity = FOUND_SELECTION.cities.includes(p.id);
    const isFoundExtra = FOUND_SELECTION.extra.includes(p.id);

    let stroke = owner ? "#f8fafc" : "#475569";
    let strokeW = owner ? "1.4" : "1";
    if (isSelected || isFoundCap || isFoundCity || isFoundExtra) {
      stroke = "#facc15";
      strokeW = "3";
    }

    const polyPts = generateProvincePolygonPoints(p, provs);
    const shortName = p.name.split("(")[0];

    let badges = "";
    if (p.is_capital || isFoundCap) badges += "★";
    else if (p.is_city || isFoundCity) badges += "●";
    if (p.has_port) badges += "⚓";
    if (p.has_fort) badges += "🏰";

    html += `
      <g class="prov-node" data-prov-id="${p.id}" style="cursor:pointer;">
        <polygon points="${polyPts}" fill="${fill}" fill-opacity="${fillOpacity}" stroke="${stroke}" stroke-width="${strokeW}" />
        <circle cx="${p.x}" cy="${p.y}" r="${p.is_capital ? 5 : (p.is_city ? 3.8 : 2.5)}" fill="${p.is_capital ? "#fde047" : "#f8fafc"}" />
        <text x="${p.x}" y="${p.y - 7}" text-anchor="middle" fill="#ffffff" font-size="9.5" font-weight="700" style="text-shadow: 0 1px 3px #000;">
          ${badges ? badges + " " : ""}${shortName}
        </text>
    `;

    if (showUnits && divCountByProv[p.id]) {
      const dc = divCountByProv[p.id];
      html += `
        <g transform="translate(${p.x - 16}, ${p.y + 4})">
          <rect x="0" y="0" width="32" height="13" rx="3" fill="#0f172a" stroke="${dc.color}" stroke-width="1.2" />
          <text x="16" y="9.8" text-anchor="middle" fill="#fde047" font-size="8.5" font-weight="700">${dc.flag}${dc.count}師</text>
        </g>
      `;
    }
    html += `</g>`;
  }

  svg.innerHTML = html;

  // プロビンスクリックイベント登録
  svg.querySelectorAll(".prov-node").forEach((node) => {
    node.addEventListener("click", (e) => {
      e.stopPropagation();
      const pid = node.getAttribute("data-prov-id");
      onPeacetimeProvinceClick(pid);
    });
  });
}

async function onPeacetimeProvinceClick(provId) {
  SELECTED_PROV_ID = provId;
  const prov = APP_STATE.provinces.find((p) => p.id === provId);
  if (!prov) return;

  if (PEACE_TOOL === "found") {
    if (prov.owner_id) {
      showToast(`『${prov.name}』は既に他国に領有されています。白地のプロビンスを選択してください。`, true);
      return;
    }
    if (FOUND_SELECTION.capital === provId) {
      FOUND_SELECTION.capital = null;
    } else if (FOUND_SELECTION.cities.includes(provId)) {
      FOUND_SELECTION.cities = FOUND_SELECTION.cities.filter((c) => c !== provId);
    } else if (FOUND_SELECTION.extra.includes(provId)) {
      FOUND_SELECTION.extra = FOUND_SELECTION.extra.filter((c) => c !== provId);
    } else if (!FOUND_SELECTION.capital) {
      FOUND_SELECTION.capital = provId;
    } else if (FOUND_SELECTION.cities.length < 2) {
      FOUND_SELECTION.cities.push(provId);
    } else {
      FOUND_SELECTION.extra.push(provId);
    }
    updateFoundSelectionUI();
    renderPeacetimeMap();
    return;
  }

  if (PEACE_TOOL === "bucket") {
    const targetOwner = document.getElementById("select-bucket-owner").value || null;
    try {
      const res = await apiPost("/api/province/action", {
        action: "bucket_paint",
        province_id: provId,
        target_owner_id: targetOwner,
      });
      APP_STATE = res.state;
      renderAll();
    } catch (err) {
      showToast(err.message, true);
    }
    return;
  }

  // inspect モード
  renderPeacetimeMap();
  renderProvinceInspectPanel();
}

function updateFoundSelectionUI() {
  const provById = {};
  for (const p of APP_STATE.provinces) provById[p.id] = p;
  document.getElementById("found-cap-label").textContent = FOUND_SELECTION.capital
    ? `★ ${provById[FOUND_SELECTION.capital]?.name}`
    : "マップ上の空き地をクリック (未選択)";
  document.getElementById("found-cities-label").textContent =
    FOUND_SELECTION.cities.length > 0
      ? FOUND_SELECTION.cities.map((c) => `● ${provById[c]?.name}`).join("、") + ` (${FOUND_SELECTION.cities.length}/2)`
      : "未選択 (0/2)";
  document.getElementById("found-provs-label").textContent =
    FOUND_SELECTION.extra.length > 0
      ? FOUND_SELECTION.extra.map((c) => provById[c]?.name).join("、")
      : "なし";
}

function renderProvinceInspectPanel() {
  const titleEl = document.getElementById("prov-detail-title");
  const bodyEl = document.getElementById("prov-detail-body");
  if (!SELECTED_PROV_ID) return;

  const prov = APP_STATE.provinces.find((p) => p.id === SELECTED_PROV_ID);
  if (!prov) return;

  const owner = APP_STATE.nations.find((n) => n.id === prov.owner_id);
  const activeNat = getActiveNation();
  const nbNames = (prov.neighbors || [])
    .map((nid) => APP_STATE.provinces.find((x) => x.id === nid)?.name.split("(")[0])
    .filter(Boolean)
    .join("、");

  titleEl.textContent = `📍 ${prov.name} [${prov.region}]`;

  let html = `
    <div style="display:flex;flex-direction:column;gap:8px;">
      <div><strong>領有国:</strong> ${owner ? `<span style="color:${owner.color};font-weight:700;">${owner.flag} ${owner.name}</span>` : "<span class='muted'>🏳️ 未領有（白地プロビンス）</span>"}</div>
      <div><strong>地形:</strong> <code>${prov.terrain}</code> ${prov.coastal ? "🌊沿岸プロビンス" : "⛰️内陸プロビンス"}</div>
      <div><strong>拠点ステータス:</strong>
        ${prov.is_capital ? "<span class='badge badge-warn'>★ 首都</span> " : ""}
        ${prov.is_city ? "<span class='badge badge-ok'>● 主要都市</span> " : ""}
        ${prov.has_port ? "<span class='badge badge-ok'>⚓ 軍港設置済</span> " : ""}
        ${prov.has_fort ? "<span class='badge badge-warn'>🏰 要塞線</span>" : ""}
        ${!prov.is_capital && !prov.is_city && !prov.has_port && !prov.has_fort ? "通常プロビンス" : ""}
      </div>
      <div><strong>陸続き隣接:</strong> <span class="muted">${nbNames || "なし"}</span></div>
  `;

  // 白地購入ボタン（未領有プロビンスの場合）
  if (!owner && activeNat) {
    html += `
      <div class="sub-box" style="margin-top:6px;">
        <strong>🛒 白地プロビンス購入（#外交ルール）</strong>
        <p class="muted">1プロビンス100億円で最大10プロビンスまで購入できます（現在購入済: ${activeNat.white_prov_bought || 0}/10）。</p>
        <button id="btn-buy-white-prov" class="btn btn-sm btn-primary btn-block" style="margin-top:6px;">
          💰 ${activeNat.flag}${activeNat.name}が100億円でこの白地を購入
        </button>
      </div>
    `;
  }

  // 平時ワープ機能（自国または同盟・通行権保有国のプロビンスへ師団移動）
  if (activeNat && activeNat.divisions && activeNat.divisions.length > 0) {
    html += `
      <div class="sub-box" style="margin-top:6px;">
        <strong>🚂 平時の部隊ワープ（#戦争ルール 準拠）</strong>
        <p class="muted">自国・同盟国・軍事通行権を持つ国のプロビンスへ師団を移動できます。</p>
        <div class="row-2" style="margin-top:5px;">
          <select id="select-warp-div">
            ${activeNat.divisions.map((d) => `<option value="${d.id}">${d.name} (${d.count}師団)</option>`).join("")}
          </select>
          <button id="btn-exec-warp" class="btn btn-xs btn-amber">📍 ここへワープ</button>
        </div>
      </div>
    `;
  }

  html += `</div>`;
  bodyEl.innerHTML = html;

  const buyBtn = document.getElementById("btn-buy-white-prov");
  if (buyBtn) {
    buyBtn.addEventListener("click", async () => {
      try {
        const res = await apiPost("/api/province/action", {
          action: "buy_white",
          province_id: prov.id,
          nation_id: activeNat.id,
        });
        APP_STATE = res.state;
        showToast(`${prov.name} を100億円で購入しました！`);
        renderAll();
      } catch (err) {
        showToast(err.message, true);
      }
    });
  }

  const warpBtn = document.getElementById("btn-exec-warp");
  if (warpBtn) {
    warpBtn.addEventListener("click", async () => {
      const divId = document.getElementById("select-warp-div").value;
      try {
        const res = await apiPost("/api/province/action", {
          action: "warp_unit",
          province_id: prov.id,
          nation_id: activeNat.id,
          division_id: divId,
        });
        APP_STATE = res.state;
        showToast(`${prov.name} へ部隊をワープ展開しました！`);
        renderAll();
      } catch (err) {
        showToast(err.message, true);
      }
    });
  }
}

function renderPeacetimeNationList() {
  const listEl = document.getElementById("peace-nation-list");
  listEl.innerHTML = "";
  for (const n of APP_STATE.nations) {
    const totalDivs = (n.divisions || []).reduce((acc, d) => acc + Number(d.count || 1), 0);
    const totalShips = (n.naval_units || []).reduce((acc, u) => acc + Number(u.count || 0), 0);
    const totalAir = (n.air_units || []).reduce((acc, u) => acc + Number(u.count || 0), 0);

    const item = document.createElement("div");
    item.className = "nation-mini-item";
    item.innerHTML = `
      <div>
        <div class="shop-item-title">
          <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:${n.color};margin-right:4px;"></span>
          ${n.flag} ${n.name} ${n.is_ai ? '<span class="badge badge-ai">AI</span>' : ""}
        </div>
        <div class="shop-item-sub">
          元首: ${n.leader} | 領土: ${(n.province_ids || []).length}プロビ | 陸:${totalDivs}師 / 海:${totalShips}隻 / 空:${totalAir}機
        </div>
      </div>
      <div style="text-align:right;">
        <div class="price-tag">${(n.budget / 10000).toFixed(2)}兆円</div>
        <button class="btn btn-xs btn-outline" data-switch-nat="${n.id}">操作切替</button>
      </div>
    `;
    item.querySelector("[data-switch-nat]").addEventListener("click", async () => {
      const res = await apiPost("/api/mode", { active_nation_id: n.id });
      APP_STATE = res.state;
      renderAll();
    });
    listEl.appendChild(item);
  }
}

// ============================================================================
// TAB 2: 戦時マップ（平時マップとは独立した戦術作戦ボード ＆ AI審判）
// ============================================================================
function renderWartimeTab() {
  const warSel = document.getElementById("select-active-war");
  warSel.innerHTML = "";
  for (const w of APP_STATE.wars || []) {
    const opt = document.createElement("option");
    opt.value = w.id;
    opt.textContent = `${w.name} (${w.status === "resolved" ? "判定済" : "作戦立案中"})`;
    if (w.id === ACTIVE_WAR_ID) opt.selected = true;
    warSel.appendChild(opt);
  }

  const theaterSel = document.getElementById("select-war-theater");
  const declTheaterSel = document.getElementById("decl-war-theater");
  theaterSel.innerHTML = "";
  declTheaterSel.innerHTML = "";
  const theaters = APP_STATE.tactical_theaters || {};
  for (const tid of Object.keys(theaters)) {
    const th = theaters[tid];
    theaterSel.innerHTML += `<option value="${tid}">${th.name}</option>`;
    declTheaterSel.innerHTML += `<option value="${tid}">${th.name}</option>`;
  }

  const war = getActiveWar();
  if (!war) return;
  ACTIVE_WAR_ID = war.id;
  if (war.theater_id && theaters[war.theater_id]) {
    theaterSel.value = war.theater_id;
  }

  document.getElementById("war-panel-title").textContent = `⚔️ ${war.name}`;
  const badge = document.getElementById("war-status-badge");
  badge.textContent = war.status === "resolved" ? "✅ 審判判定済" : "📝 作戦立案・提出中";
  badge.className = "badge " + (war.status === "resolved" ? "badge-ok" : "badge-warn");

  const nationsById = {};
  for (const n of APP_STATE.nations) nationsById[n.id] = n;

  const atkNames = (war.attackers || []).map((id) => nationsById[id] ? `${nationsById[id].flag}${nationsById[id].name}` : id).join("<br/>");
  const dfnNames = (war.defenders || []).map((id) => nationsById[id] ? `${nationsById[id].flag}${nationsById[id].name}` : id).join("<br/>");

  document.getElementById("war-coalition-box").innerHTML = `
    <div>
      <div style="color:#f87171;font-weight:700;font-size:11.5px;">🔴 宣戦・攻撃陣営 (${(war.attackers || []).length}/3)</div>
      <div style="font-size:12px;margin-top:3px;">${atkNames || "なし"}</div>
    </div>
    <div style="font-weight:800;color:#fbbf24;">VS</div>
    <div style="text-align:right;">
      <div style="color:#60a5fa;font-weight:700;font-size:11.5px;">🔵 防衛連合陣営 (${(war.defenders || []).length}/3)</div>
      <div style="font-size:12px;margin-top:3px;">${dfnNames || "なし"}</div>
    </div>
  `;

  document.getElementById("war-atk-doctrine").value = war.attacker_doctrine || "";
  document.getElementById("war-dfn-doctrine").value = war.defender_doctrine || "";

  // 戦略目標プロビンスセレクト
  const fromSel = document.getElementById("war-arrow-from");
  const toSel = document.getElementById("war-arrow-to");
  fromSel.innerHTML = "";
  toSel.innerHTML = "";
  for (const p of APP_STATE.provinces) {
    if ((war.attackers || []).includes(p.owner_id)) {
      fromSel.innerHTML += `<option value="${p.id}">[発] ${p.name}</option>`;
    }
    if ((war.defenders || []).includes(p.owner_id)) {
      toSel.innerHTML += `<option value="${p.id}">[目標] ${p.name}</option>`;
    }
  }

  const targetListEl = document.getElementById("war-strat-target-list");
  targetListEl.innerHTML = "";
  const provById = {};
  for (const p of APP_STATE.provinces) provById[p.id] = p;
  for (const arr of war.tactical_arrows || []) {
    const fn = provById[arr.from_prov]?.name.split("(")[0] || arr.from_prov;
    const tn = provById[arr.to_prov]?.name.split("(")[0] || arr.to_prov;
    const chip = document.createElement("span");
    chip.className = "tag-chip";
    chip.innerHTML = `${fn} → ${tn} [${arr.type}] <b style="cursor:pointer;" data-del-arr="${arr.id}">×</b>`;
    chip.querySelector("[data-del-arr]").addEventListener("click", () => {
      war.tactical_arrows = war.tactical_arrows.filter((x) => x.id !== arr.id);
      saveWarPlanSilent(war);
    });
    targetListEl.appendChild(chip);
  }

  if (war.result && war.result.report_markdown) {
    document.getElementById("war-result-container").textContent = war.result.report_markdown;
  }

  renderTacticalWarSvg(war);
}

function renderTacticalWarSvg(war) {
  const svg = document.getElementById("wartime-svg");
  const theaters = APP_STATE.tactical_theaters || {};
  const theater = theaters[war.theater_id] || Object.values(theaters)[0];
  if (!theater) return;

  const layerView = document.getElementById("select-war-layer-view").value; // both | attacker | defender

  let html = `
    <defs>
      <pattern id="tacGrid" width="54" height="54" patternUnits="userSpaceOnUse">
        <path d="M 54 0 L 0 0 0 54" fill="none" stroke="rgba(148,163,184,0.11)" stroke-width="1"/>
      </pattern>
      <marker id="arrowAtk" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#ef4444" />
      </marker>
      <marker id="arrowDfn" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#3b82f6" />
      </marker>
      <marker id="arrowNaval" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#06b6d4" />
      </marker>
    </defs>

    <!-- 背景・戦術グリッド -->
    <rect x="0" y="0" width="1080" height="860" fill="#111a27" />
    <rect x="0" y="0" width="1080" height="860" fill="url(#tacGrid)" />

    <!-- 海域ゾーン背景 -->
    <rect x="0" y="675" width="1080" height="185" fill="rgba(14, 116, 144, 0.22)" />
    <line x1="0" y1="675" x2="1080" y2="675" stroke="rgba(56, 189, 248, 0.35)" stroke-width="2" stroke-dasharray="8,6" />

    <!-- 戦域タイトル透かし -->
    <text x="24" y="36" fill="rgba(248,250,252,0.85)" font-size="18" font-weight="800">🗺️ 戦時戦術作戦マップ：${theater.name}</text>
    <text x="24" y="56" fill="rgba(148,163,184,0.75)" font-size="12">${theater.description}</text>
  `;

  // 河川描画
  for (const riv of theater.rivers || []) {
    const pts = riv.map((pt) => `${pt[0]},${pt[1]}`).join(" ");
    html += `<polyline points="${pts}" fill="none" stroke="rgba(56,189,248,0.45)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" />`;
  }

  // デフォルト前線ライン
  if (theater.frontline_default) {
    const fpts = theater.frontline_default.map((pt) => `${pt[0]},${pt[1]}`).join(" ");
    html += `<polyline points="${fpts}" fill="none" stroke="rgba(250,204,21,0.35)" stroke-width="3" stroke-dasharray="10,8" />`;
  }

  // 戦術ランドマーク（都市・要塞・峠・軍港・海域）
  for (const lm of theater.landmarks || []) {
    const isCap = lm.type === "capital";
    const isPort = lm.type === "port" || lm.type === "port_city";
    const isPass = lm.type === "pass" || lm.type === "fort";
    const fillCol = isCap ? "#fde047" : (isPort ? "#38bdf8" : (isPass ? "#f97316" : "#e2e8f0"));

    html += `
      <g transform="translate(${lm.x}, ${lm.y})">
        <circle cx="0" cy="0" r="${isCap ? 9 : 6}" fill="${fillCol}" fill-opacity="0.25" stroke="${fillCol}" stroke-width="2" />
        <circle cx="0" cy="0" r="2.5" fill="${fillCol}" />
        <text x="0" y="-12" text-anchor="middle" fill="${fillCol}" font-size="11.5" font-weight="700" style="text-shadow:0 1px 4px #000;">
          ${lm.name}
        </text>
        <text x="0" y="18" text-anchor="middle" fill="#94a3b8" font-size="9.5">[${lm.terrain}]</text>
      </g>
    `;
  }

  // プレイヤーおよびAIが描画した作戦矢印・防衛線 (tactical_drawings)
  const drawings = [...(war.tactical_drawings || [])];
  if (isDrawingArrow && currentDrawPoints.length > 1) {
    drawings.push({
      id: "temp_drawing",
      side: document.getElementById("select-war-side").value,
      style: WAR_TOOL.replace("draw_", ""),
      label: "描画中...",
      points: currentDrawPoints,
    });
  }

  for (const d of drawings) {
    if (layerView !== "both" && d.side !== layerView) continue;
    const pts = (d.points || []).map((p) => `${p[0]},${p[1]}`).join(" ");
    if (!pts) continue;

    const isAtk = d.side === "attacker";
    let stroke = isAtk ? "#ef4444" : "#3b82f6";
    let dash = "";
    let marker = isAtk ? "url(#arrowAtk)" : "url(#arrowDfn)";
    let width = "5";

    if (d.style === "defend") {
      dash = "10,5";
      marker = "";
      width = "6";
      stroke = isAtk ? "#f97316" : "#60a5fa";
    } else if (d.style === "naval") {
      dash = "6,6";
      stroke = "#06b6d4";
      marker = "url(#arrowNaval)";
    } else if (d.style === "counter") {
      stroke = "#eab308";
    }

    const midPt = d.points[Math.floor(d.points.length / 2)] || d.points[0];
    html += `
      <g class="tac-drawing" data-draw-id="${d.id}">
        <polyline points="${pts}" fill="none" stroke="${stroke}" stroke-width="${width}"
          stroke-linecap="round" stroke-linejoin="round"
          ${dash ? `stroke-dasharray="${dash}"` : ""}
          ${marker ? `marker-end="${marker}"` : ""} />
        <text x="${midPt[0]}" y="${midPt[1] - 8}" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="700" style="text-shadow:0 1px 4px #000;">
          ${d.label || ""}
        </text>
      </g>
    `;
  }

  // NATO兵科シンボル描画 (tactical_units)
  for (const u of war.tactical_units || []) {
    if (layerView !== "both" && u.side !== layerView) continue;
    const isAtk = u.side === "attacker";
    const boxFill = isAtk ? "#7f1d1d" : "#1e3a8a";
    const boxStroke = isAtk ? "#f87171" : "#60a5fa";

    let natoInner = "";
    if (u.unit_type === "infantry") {
      natoInner = `<line x1="-18" y1="-11" x2="18" y2="11" stroke="#fff" stroke-width="1.8"/><line x1="-18" y1="11" x2="18" y2="-11" stroke="#fff" stroke-width="1.8"/>`;
    } else if (u.unit_type === "mech") {
      natoInner = `<line x1="-18" y1="-11" x2="18" y2="11" stroke="#fff" stroke-width="1.6"/><line x1="-18" y1="11" x2="18" y2="-11" stroke="#fff" stroke-width="1.6"/><ellipse cx="0" cy="0" rx="11" ry="6" fill="none" stroke="#fde047" stroke-width="1.8"/>`;
    } else if (u.unit_type === "armor") {
      natoInner = `<ellipse cx="0" cy="0" rx="13" ry="7" fill="none" stroke="#fde047" stroke-width="2.2"/>`;
    } else if (u.unit_type === "mountain") {
      natoInner = `<polygon points="0,-8 -10,9 10,9" fill="#fff"/>`;
    } else if (u.unit_type === "airborne") {
      natoInner = `<path d="M -10,-2 C -6,-10 6,-10 10,-2 L 0,9 Z" fill="none" stroke="#fff" stroke-width="1.8"/>`;
    } else if (u.unit_type === "fleet") {
      natoInner = `<text x="0" y="5" text-anchor="middle" fill="#38bdf8" font-size="14" font-weight="800">⚓</text>`;
    } else if (u.unit_type === "air") {
      natoInner = `<text x="0" y="5" text-anchor="middle" fill="#fde047" font-size="14" font-weight="800">✈️</text>`;
    } else {
      natoInner = `<line x1="-18" y1="-11" x2="18" y2="11" stroke="#fff" stroke-width="1.8"/>`;
    }

    html += `
      <g class="tac-unit" data-unit-id="${u.id}" transform="translate(${u.x}, ${u.y})" style="cursor:move;">
        <text x="0" y="-15" text-anchor="middle" fill="#fde047" font-size="9" font-weight="800">XX</text>
        <rect x="-18" y="-11" width="36" height="22" rx="2" fill="${boxFill}" stroke="${boxStroke}" stroke-width="2" />
        ${natoInner}
        <rect x="-56" y="13" width="112" height="14" rx="3" fill="rgba(15,23,42,0.85)" />
        <text x="0" y="23" text-anchor="middle" fill="#f8fafc" font-size="9.5" font-weight="600">${u.name}</text>
      </g>
    `;
  }

  svg.innerHTML = html;

  // NATO部隊アイコンのドラッグ移動イベント
  svg.querySelectorAll(".tac-unit").forEach((el) => {
    el.addEventListener("mousedown", (e) => {
      if (WAR_TOOL !== "move") return;
      e.stopPropagation();
      draggingUnitId = el.getAttribute("data-unit-id");
    });
  });
}

function getSvgPoint(svgEl, clientX, clientY) {
  const pt = svgEl.createSVGPoint();
  pt.x = clientX;
  pt.y = clientY;
  const ctm = svgEl.getScreenCTM();
  if (!ctm) return { x: 0, y: 0 };
  const transformed = pt.matrixTransform(ctm.inverse());
  return { x: Math.round(transformed.x), y: Math.round(transformed.y) };
}

async function saveWarPlanSilent(war) {
  try {
    const res = await apiPost("/api/war/tactical_plan", {
      war_id: war.id,
      action: "save",
      tactical_units: war.tactical_units,
      tactical_drawings: war.tactical_drawings,
      tactical_arrows: war.tactical_arrows,
      attacker_doctrine: document.getElementById("war-atk-doctrine").value,
      defender_doctrine: document.getElementById("war-dfn-doctrine").value,
    });
    APP_STATE = res.state;
    renderWartimeTab();
  } catch (err) {
    showToast(err.message, true);
  }
}

// ============================================================================
// TAB 3: 軍備編成・師団ビルダー・ショップ
// ============================================================================
function renderMilitaryTab() {
  const activeNat = getActiveNation();
  if (!activeNat) return;

  // 配備プロビンスセレクト
  const provSel = document.getElementById("div-prov");
  provSel.innerHTML = "";
  for (const pid of activeNat.province_ids || []) {
    const p = APP_STATE.provinces.find((x) => x.id === pid);
    if (p) {
      provSel.innerHTML += `<option value="${pid}" ${pid === activeNat.capital_id ? "selected" : ""}>${p.name}</option>`;
    }
  }

  renderDivisionBuilderRows();
  renderDivisionSpecPreview();
  renderProcurementShop();
  renderNationInventory(activeNat);
}

function renderDivisionBuilderRows() {
  const allTanks = getAllTanks();
  const regListEl = document.getElementById("builder-regiments-list");
  regListEl.innerHTML = "";

  BUILDER_REGIMENTS.forEach((item, idx) => {
    const regDef = CATALOG.base_regiments.find((r) => r.id === item.regiment_id) || CATALOG.base_regiments[0];
    const row = document.createElement("div");
    row.className = "reg-row";

    const regSelectHtml = `
      <select data-reg-idx="${idx}" class="sel-reg-type">
        ${CATALOG.base_regiments.map((r) => `<option value="${r.id}" ${r.id === item.regiment_id ? "selected" : ""}>${r.name} (${r.cost}億)</option>`).join("")}
      </select>
    `;

    let tankSelectHtml = `<span class="muted" style="font-size:11px;">${regDef.desc.slice(0, 26)}...</span>`;
    if (regDef.is_tank_unit) {
      const curTank = item.tank_id || regDef.default_tank_id || "su_t34_85";
      tankSelectHtml = `
        <select data-tank-reg-idx="${idx}" class="sel-reg-tank">
          ${allTanks.map((t) => `<option value="${t.id}" ${t.id === curTank ? "selected" : ""}>[${t.country}] ${t.name} (${t.cost}億/両 → 大隊${(t.cost * 76 + 10).toFixed(0)}億)</option>`).join("")}
        </select>
      `;
    }

    row.innerHTML = `
      ${regSelectHtml}
      ${tankSelectHtml}
      <button type="button" class="btn btn-xs btn-outline" data-del-reg="${idx}" ${BUILDER_REGIMENTS.length <= 3 ? "disabled" : ""}>✕</button>
    `;
    regListEl.appendChild(row);
  });

  // 砲兵セレクト
  const artSel = document.getElementById("builder-artillery");
  artSel.innerHTML = CATALOG.artillery_regiments
    .map((a) => `<option value="${a.id}" ${a.id === BUILDER_ARTILLERY ? "selected" : ""}>${a.name} (${a.cost}億)</option>`)
    .join("");

  // 補助大隊リスト
  const supListEl = document.getElementById("builder-supports-list");
  supListEl.innerHTML = "";
  BUILDER_SUPPORTS.forEach((item, idx) => {
    const supDef = CATALOG.support_battalions.find((s) => s.id === item.support_id) || CATALOG.support_battalions[0];
    const row = document.createElement("div");
    row.className = "reg-row";

    const supSelectHtml = `
      <select data-sup-idx="${idx}" class="sel-sup-type">
        ${CATALOG.support_battalions.map((s) => `<option value="${s.id}" ${s.id === item.support_id ? "selected" : ""}>${s.name} (${s.cost}億)</option>`).join("")}
      </select>
    `;

    let tankSelectHtml = `<span class="muted" style="font-size:11px;">${supDef.desc.slice(0, 24)}...</span>`;
    if (supDef.is_tank_unit) {
      const curTank = item.tank_id || supDef.default_tank_id || "su_t34_85";
      tankSelectHtml = `
        <select data-tank-sup-idx="${idx}" class="sel-sup-tank">
          ${allTanks.map((t) => `<option value="${t.id}" ${t.id === curTank ? "selected" : ""}>[${t.country}] ${t.name} (${t.cost}億/両 → 中隊${(t.cost * 22).toFixed(0)}億)</option>`).join("")}
        </select>
      `;
    }

    row.innerHTML = `
      ${supSelectHtml}
      ${tankSelectHtml}
      <button type="button" class="btn btn-xs btn-outline" data-del-sup="${idx}">✕</button>
    `;
    supListEl.appendChild(row);
  });

  // イベントバインド
  regListEl.querySelectorAll(".sel-reg-type").forEach((el) => {
    el.addEventListener("change", () => {
      const i = Number(el.getAttribute("data-reg-idx"));
      BUILDER_REGIMENTS[i] = { regiment_id: el.value, tank_id: "su_t34_85", custom_calc: false };
      BUILDER_OVERRIDE_COST = null;
      renderDivisionBuilderRows();
      renderDivisionSpecPreview();
    });
  });

  regListEl.querySelectorAll(".sel-reg-tank").forEach((el) => {
    el.addEventListener("change", () => {
      const i = Number(el.getAttribute("data-tank-reg-idx"));
      BUILDER_REGIMENTS[i].tank_id = el.value;
      BUILDER_REGIMENTS[i].custom_calc = true;
      BUILDER_OVERRIDE_COST = null;
      renderDivisionSpecPreview();
    });
  });

  regListEl.querySelectorAll("[data-del-reg]").forEach((el) => {
    el.addEventListener("click", () => {
      const i = Number(el.getAttribute("data-del-reg"));
      if (BUILDER_REGIMENTS.length > 3) {
        BUILDER_REGIMENTS.splice(i, 1);
        BUILDER_OVERRIDE_COST = null;
        renderDivisionBuilderRows();
        renderDivisionSpecPreview();
      }
    });
  });

  supListEl.querySelectorAll(".sel-sup-type").forEach((el) => {
    el.addEventListener("change", () => {
      const i = Number(el.getAttribute("data-sup-idx"));
      BUILDER_SUPPORTS[i] = { support_id: el.value, tank_id: "su_t34_85", custom_calc: false };
      BUILDER_OVERRIDE_COST = null;
      renderDivisionBuilderRows();
      renderDivisionSpecPreview();
    });
  });

  supListEl.querySelectorAll(".sel-sup-tank").forEach((el) => {
    el.addEventListener("change", () => {
      const i = Number(el.getAttribute("data-tank-sup-idx"));
      BUILDER_SUPPORTS[i].tank_id = el.value;
      BUILDER_SUPPORTS[i].custom_calc = true;
      BUILDER_OVERRIDE_COST = null;
      renderDivisionSpecPreview();
    });
  });

  supListEl.querySelectorAll("[data-del-sup]").forEach((el) => {
    el.addEventListener("click", () => {
      const i = Number(el.getAttribute("data-del-sup"));
      BUILDER_SUPPORTS.splice(i, 1);
      BUILDER_OVERRIDE_COST = null;
      renderDivisionBuilderRows();
      renderDivisionSpecPreview();
    });
  });
}

function computeClientDivisionSpec() {
  const allTanks = getAllTanks();
  const tankMap = {};
  for (const t of allTanks) tankMap[t.id] = t;
  const regMap = {};
  for (const r of CATALOG.base_regiments) regMap[r.id] = r;
  const artMap = {};
  for (const a of CATALOG.artillery_regiments) artMap[a.id] = a;
  const supMap = {};
  for (const s of CATALOG.support_battalions) supMap[s.id] = s;

  let cost = 0;
  let sa = 0, ha = 0, def = 0, brk = 0, armorSum = 0, aa = 10, recon = 10;
  let minSpeed = 3;
  const warnings = [];

  for (const item of BUILDER_REGIMENTS) {
    const r = regMap[item.regiment_id];
    if (!r) continue;
    minSpeed = Math.min(minSpeed, r.speed_tier || 1);
    if (r.is_tank_unit) {
      const tk = tankMap[item.tank_id || "su_t34_85"] || tankMap["su_t34_85"];
      const c = !item.custom_calc && (tk.id === "su_t34_85" || tk.id === "us_m4_76") ? r.cost : +(tk.cost * 76 + 10).toFixed(1);
      cost += c;
      sa += tk.sa * 1.4;
      ha += tk.ha * 1.5;
      def += 55;
      brk += (tk.ha + tk.armor) * 0.9;
      armorSum += tk.armor;
    } else {
      cost += r.cost;
      sa += r.sa;
      ha += r.ha;
      def += r.defense;
      brk += r.breakthrough;
      armorSum += r.armor;
    }
  }

  const art = artMap[BUILDER_ARTILLERY] || artMap["art_none"];
  if (art && art.id !== "art_none") {
    cost += art.cost;
    sa += art.sa;
    ha += art.ha;
    def += art.defense;
    brk += art.breakthrough;
    if ((art.max_speed_tier || 3) < minSpeed) {
      warnings.push(`⚠️ ${art.name}は機械化・機甲部隊に追従できないため速度が低下します（自走砲兵を推奨）`);
    }
  }

  for (const sItem of BUILDER_SUPPORTS) {
    const s = supMap[sItem.support_id];
    if (!s) continue;
    if (s.is_tank_unit) {
      const tk = tankMap[sItem.tank_id || "su_t34_85"] || tankMap["su_t34_85"];
      const c = !sItem.custom_calc && (tk.id === "su_t34_85" || tk.id === "us_m4_76") ? s.cost : +(tk.cost * 22).toFixed(1);
      cost += c;
      sa += tk.sa * 0.5;
      ha += tk.ha * 0.55;
      def += 20;
      brk += (tk.ha + tk.armor) * 0.35;
      armorSum += tk.armor * 0.4;
    } else {
      cost += s.cost;
      sa += s.sa || 0;
      ha += s.ha || 0;
      aa += s.aa || 0;
      recon += s.recon || 0;
      def += s.defense || 0;
      brk += s.breakthrough || 0;
      armorSum += (s.armor || 0) * 0.3;
    }
  }

  const finalCost = BUILDER_OVERRIDE_COST !== null ? BUILDER_OVERRIDE_COST : +cost.toFixed(1);
  const count = Math.max(1, Number(document.getElementById("div-count")?.value || 1));
  return {
    unitCost: finalCost,
    totalCost: +(finalCost * count).toFixed(1),
    count,
    sa: Math.round(sa),
    ha: Math.round(ha),
    def: Math.round(def),
    brk: Math.round(brk),
    armor: Math.round(armorSum / Math.max(1, BUILDER_REGIMENTS.length)),
    aa: Math.round(aa),
    warnings,
  };
}

function renderDivisionSpecPreview() {
  const spec = computeClientDivisionSpec();
  const box = document.getElementById("div-preview-box");
  box.innerHTML = `
    <div style="display:flex;justify-content:space-between;align-items:center;">
      <span><strong>1個師団単価:</strong> <span class="price-tag">${spec.unitCost}億円</span></span>
      <span><strong>${spec.count}個師団 合計費用:</strong> <span class="price-tag" style="font-size:15px;">${spec.totalCost.toLocaleString()}億円 (${(spec.totalCost / 10000).toFixed(2)}兆円)</span></span>
    </div>
    <div class="spec-stats-grid">
      <div class="stat-box"><span>対人火力</span><strong>${spec.sa}</strong></div>
      <div class="stat-box"><span>対戦車火力</span><strong>${spec.ha}</strong></div>
      <div class="stat-box"><span>突破力</span><strong>${spec.brk}</strong></div>
      <div class="stat-box"><span>防衛・装甲</span><strong>${spec.def} / 装${spec.armor}</strong></div>
    </div>
    ${spec.warnings.map((w) => `<div style="color:#fbbf24;font-size:11.5px;margin-top:5px;">${w}</div>`).join("")}
  `;
}

function renderProcurementShop() {
  const countrySel = document.getElementById("shop-country-filter");
  const searchVal = (document.getElementById("shop-search").value || "").trim().toLowerCase();
  const listEl = document.getElementById("shop-items-list");

  let items = [];
  if (ACTIVE_SHOP_DOMAIN === "navy") items = CATALOG.naval_units;
  else if (ACTIVE_SHOP_DOMAIN === "air") items = CATALOG.air_units;
  else items = CATALOG.facilities;

  // 国フィルタ更新
  const countries = Array.from(new Set(items.map((x) => x.country).filter(Boolean)));
  const prevCountry = countrySel.value;
  countrySel.innerHTML = `<option value="ALL">すべての国・カテゴリ (${items.length}種)</option>`;
  for (const c of countries) {
    countrySel.innerHTML += `<option value="${c}" ${c === prevCountry ? "selected" : ""}>${c}</option>`;
  }
  const activeCountry = countrySel.value;

  const filtered = items.filter((item) => {
    if (activeCountry !== "ALL" && item.country && item.country !== activeCountry) return false;
    if (searchVal && !`${item.name} ${item.country || ""} ${item.category || ""}`.toLowerCase().includes(searchVal)) return false;
    return true;
  });

  listEl.innerHTML = "";
  const activeNat = getActiveNation();

  for (const item of filtered) {
    const row = document.createElement("div");
    row.className = "shop-item";
    let subInfo = "";
    if (ACTIVE_SHOP_DOMAIN === "navy") {
      subInfo = `[${item.country} / ${item.category}] 砲雷撃:${item.naval_atk} 防御:${item.naval_def} 対空:${item.aa}${item.carrier_air ? ` 艦載機:${item.carrier_air}機込` : ""}`;
    } else if (ACTIVE_SHOP_DOMAIN === "air") {
      subInfo = `[${item.country} / ${item.category}] 制空:${item.air_atk} 対地CAS:${item.cas} 戦略爆撃:${item.strat}`;
    } else {
      subInfo = item.desc;
    }

    row.innerHTML = `
      <div>
        <div class="shop-item-title">${item.name}</div>
        <div class="shop-item-sub">${subInfo}</div>
      </div>
      <div style="display:flex;align-items:center;gap:6px;">
        <span class="price-tag">${item.cost}億</span>
        ${ACTIVE_SHOP_DOMAIN !== "facility" ? `<input type="number" value="${ACTIVE_SHOP_DOMAIN === "air" && !item.is_nuke ? 10 : 1}" min="1" max="500" style="width:58px;" class="shop-qty-input" />` : ""}
        <button class="btn btn-xs btn-primary btn-buy-item">購入</button>
      </div>
    `;

    row.querySelector(".btn-buy-item").addEventListener("click", async () => {
      if (!activeNat) return;
      const qtyInput = row.querySelector(".shop-qty-input");
      const qty = qtyInput ? Math.max(1, Number(qtyInput.value || 1)) : 1;
      try {
        const res = await apiPost("/api/military/procure", {
          nation_id: activeNat.id,
          domain: ACTIVE_SHOP_DOMAIN,
          action: "buy",
          unit_id: item.id,
          count: qty,
        });
        APP_STATE = res.state;
        showToast(`${item.name} ×${qty} を調達しました！`);
        renderAll();
      } catch (err) {
        showToast(err.message, true);
      }
    });

    listEl.appendChild(row);
  }
}

function renderNationInventory(nat) {
  const banner = document.getElementById("nation-force-summary");
  const listEl = document.getElementById("nation-inventory-list");

  const hasPort = (nat.facilities || []).includes("fac_naval_port");
  const navMap = {};
  for (const u of CATALOG.naval_units) navMap[u.id] = u;
  const airMap = {};
  for (const u of CATALOG.air_units) airMap[u.id] = u;
  const facMap = {};
  for (const f of CATALOG.facilities) facMap[f.id] = f;

  banner.innerHTML = `
    <div class="sub-box" style="border-color:${hasPort ? "#10b981" : "#f59e0b"};">
      <div><strong>${nat.flag} ${nat.name} 軍備ステータス</strong></div>
      <div style="font-size:11.5px;margin-top:3px;">
        ⚓ 軍港(500億): ${hasPort ? "<strong style='color:#34d399;'>設置済み（海軍補給・修理有効）</strong>" : "<strong style='color:#fbbf24;'>⚠️ 未設置（海軍を運用する場合は必ず軍港を購入してください！）</strong>"}
      </div>
    </div>
  `;

  listEl.innerHTML = "";

  // 1. 施設
  for (const fid of nat.facilities || []) {
    const f = facMap[fid];
    if (!f) continue;
    const el = document.createElement("div");
    el.className = "inv-item";
    el.innerHTML = `
      <div>
        <div class="shop-item-title">🏰 [施設] ${f.name}</div>
        <div class="shop-item-sub">解体にすると ${f.cost}億円 返金</div>
      </div>
      <button class="btn btn-xs btn-outline">解体(+${f.cost}億)</button>
    `;
    el.querySelector("button").addEventListener("click", async () => {
      const res = await apiPost("/api/military/procure", {
        nation_id: nat.id,
        domain: "facility",
        action: "disband",
        unit_id: fid,
        count: 1,
      });
      APP_STATE = res.state;
      showToast(`${f.name} を解体し全額返金しました。`);
      renderAll();
    });
    listEl.appendChild(el);
  }

  // 2. 陸軍師団
  for (const div of nat.divisions || []) {
    const refund = +(Number(div.spec?.cost || 380) * Number(div.count || 1)).toFixed(1);
    const provName = APP_STATE.provinces.find((p) => p.id === div.province_id)?.name.split("(")[0] || "首都";
    const el = document.createElement("div");
    el.className = "inv-item";
    el.innerHTML = `
      <div>
        <div class="shop-item-title">🪖 ${div.name} × ${div.count}個師団 <span class="badge badge-ok">📍${provName}</span></div>
        <div class="shop-item-sub">${(div.spec?.breakdown || []).join(" / ")}</div>
      </div>
      <button class="btn btn-xs btn-outline">解体(+${refund}億)</button>
    `;
    el.querySelector("button").addEventListener("click", async () => {
      const res = await apiPost("/api/military/division", {
        nation_id: nat.id,
        action: "disband",
        division_id: div.id,
      });
      APP_STATE = res.state;
      showToast(`${div.name} を解体し ${refund}億円 を返金しました。`);
      renderAll();
    });
    listEl.appendChild(el);
  }

  // 3. 海軍
  for (const item of nat.naval_units || []) {
    const u = navMap[item.unit_id];
    if (!u) continue;
    const refund = +(u.cost * item.count).toFixed(1);
    const el = document.createElement("div");
    el.className = "inv-item";
    el.innerHTML = `
      <div>
        <div class="shop-item-title">⚓ ${u.name} × ${item.count}隻</div>
        <div class="shop-item-sub">単価 ${u.cost}億 / 合計 ${refund}億</div>
      </div>
      <button class="btn btn-xs btn-outline">全解体(+${refund}億)</button>
    `;
    el.querySelector("button").addEventListener("click", async () => {
      const res = await apiPost("/api/military/procure", {
        nation_id: nat.id,
        domain: "navy",
        action: "disband",
        unit_id: item.unit_id,
        count: item.count,
      });
      APP_STATE = res.state;
      showToast(`${u.name} を解体し ${refund}億円 を返金しました。`);
      renderAll();
    });
    listEl.appendChild(el);
  }

  // 4. 空軍
  for (const item of nat.air_units || []) {
    const u = airMap[item.unit_id];
    if (!u) continue;
    const refund = +(u.cost * item.count).toFixed(1);
    const el = document.createElement("div");
    el.className = "inv-item";
    el.innerHTML = `
      <div>
        <div class="shop-item-title">✈️ ${u.name} × ${item.count}${u.is_nuke ? "発" : "機"}</div>
        <div class="shop-item-sub">単価 ${u.cost}億 / 合計 ${refund}億</div>
      </div>
      <button class="btn btn-xs btn-outline">全解体(+${refund}億)</button>
    `;
    el.querySelector("button").addEventListener("click", async () => {
      const res = await apiPost("/api/military/procure", {
        nation_id: nat.id,
        domain: "air",
        action: "disband",
        unit_id: item.unit_id,
        count: item.count,
      });
      APP_STATE = res.state;
      showToast(`${u.name} を解体し ${refund}億円 を返金しました。`);
      renderAll();
    });
    listEl.appendChild(el);
  }
}

// ============================================================================
// TAB 4: 外交・条約・国際ニュース＆Discordログ
// ============================================================================
function renderDiplomacyTab() {
  const natASel = document.getElementById("treaty-nat-a");
  const natBSel = document.getElementById("treaty-nat-b");
  const prevA = natASel.value;
  const prevB = natBSel.value;

  natASel.innerHTML = "";
  natBSel.innerHTML = "";
  for (const n of APP_STATE.nations) {
    natASel.innerHTML += `<option value="${n.id}">${n.flag} ${n.name}</option>`;
    natBSel.innerHTML += `<option value="${n.id}">${n.flag} ${n.name}</option>`;
  }
  if (prevA) natASel.value = prevA;
  else if (APP_STATE.active_nation_id) natASel.value = APP_STATE.active_nation_id;
  if (prevB) natBSel.value = prevB;
  else if (APP_STATE.nations.length > 1) natBSel.value = APP_STATE.nations[1].id;

  updatePeaceCedeProvincesUI();

  // 条約一覧
  const nationsById = {};
  for (const n of APP_STATE.nations) nationsById[n.id] = n;
  const trList = document.getElementById("active-treaties-list");
  trList.innerHTML = "";
  for (const tr of APP_STATE.treaties || []) {
    const na = nationsById[tr.nation_a];
    const nb = nationsById[tr.nation_b];
    const item = document.createElement("div");
    item.className = "treaty-item";
    item.innerHTML = `
      <div>
        <div class="shop-item-title">📜 ${tr.name} <span class="badge badge-ok">${tr.type.toUpperCase()}</span></div>
        <div class="shop-item-sub">${na ? na.flag + na.name : tr.nation_a} ⇔ ${nb ? nb.flag + nb.name : tr.nation_b} | 期限: ${tr.expires_week >= 900 ? "無期限" : "第" + tr.expires_week + "週"}</div>
        <div style="font-size:11.5px;margin-top:2px;">${tr.desc || ""}</div>
      </div>
      <button class="btn btn-xs btn-outline">破棄</button>
    `;
    item.querySelector("button").addEventListener("click", async () => {
      const res = await apiPost("/api/diplomacy/treaty", { action: "delete", treaty_id: tr.id });
      APP_STATE = res.state;
      renderAll();
    });
    trList.appendChild(item);
  }

  // ニュースタイムライン
  const newsEl = document.getElementById("news-feed-list");
  newsEl.innerHTML = "";
  for (const n of APP_STATE.news || []) {
    const item = document.createElement("div");
    item.className = "news-item";
    item.innerHTML = `
      <div style="display:flex;justify-content:space-between;width:100%;">
        <strong style="color:#38bdf8;">${n.flag || "📰"} ${n.speaker} — ${n.title}</strong>
        <span class="muted">第${n.week || 1}週</span>
      </div>
      <div style="margin-top:4px;white-space:pre-wrap;">${n.body}</div>
    `;
    newsEl.appendChild(item);
  }
}

function updatePeaceCedeProvincesUI() {
  const ttype = document.getElementById("treaty-type").value;
  const box = document.getElementById("peace-cede-box");
  if (ttype !== "peace") {
    box.style.display = "none";
    return;
  }
  box.style.display = "block";
  const loserId = document.getElementById("treaty-nat-b").value;
  const loser = APP_STATE.nations.find((n) => n.id === loserId);
  const grid = document.getElementById("peace-cede-provinces");
  grid.innerHTML = "";
  if (!loser) return;

  for (const pid of loser.province_ids || []) {
    const p = APP_STATE.provinces.find((x) => x.id === pid);
    if (!p) continue;
    grid.innerHTML += `
      <label class="checkbox-label">
        <input type="checkbox" class="chk-cede-prov" value="${pid}" /> ${p.name}
      </label>
    `;
  }
}

async function fetchDiscordLogs() {
  const listEl = document.getElementById("discord-logs-list");
  try {
    const res = await fetch("/api/discord_sync");
    const data = await res.json();
    listEl.innerHTML = "";
    for (const m of data.messages || []) {
      const item = document.createElement("div");
      item.className = "news-item";
      item.innerHTML = `
        <div style="display:flex;justify-content:space-between;width:100%;">
          <strong style="color:#a78bfa;">#${m.channel_name} — ${m.author_name}</strong>
          <span class="muted">${(m.created_at || "").slice(0, 16).replace("T", " ")}</span>
        </div>
        <div style="margin-top:3px;font-size:12px;white-space:pre-wrap;">${m.content}</div>
      `;
      listEl.appendChild(item);
    }
  } catch (e) {}
}

// ============================================================================
// TAB 5: 白地図PNG バケツ塗りツール（フラッドフィル）
// ============================================================================
function initPngPainterCanvas() {
  const canvas = document.getElementById("png-paint-canvas");
  const ctx = canvas.getContext("2d");

  // 初期状態として欧州・地中海の白地図アウトラインをキャンバスに描画しておく
  ctx.fillStyle = "#bcd4e6";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  if (APP_STATE && APP_STATE.provinces) {
    for (const p of APP_STATE.provinces) {
      const pts = generateProvincePolygonPoints(p, APP_STATE.provinces)
        .split(" ")
        .map((pair) => pair.split(",").map(Number));
      ctx.beginPath();
      pts.forEach((pt, idx) => {
        const cx = (pt[0] - 150) * 0.95;
        const cy = (pt[1] - 40) * 0.75;
        if (idx === 0) ctx.moveTo(cx, cy);
        else ctx.lineTo(cx, cy);
      });
      ctx.closePath();
      ctx.fillStyle = "#ffffff";
      ctx.fill();
      ctx.lineWidth = 2;
      ctx.strokeStyle = "#1e293b";
      ctx.stroke();
    }
  }

  canvas.addEventListener("click", (e) => {
    const rect = canvas.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    const x = Math.floor((e.clientX - rect.left) * scaleX);
    const y = Math.floor((e.clientY - rect.top) * scaleY);
    const hexColor = document.getElementById("png-fill-color").value;
    const tol = Number(document.getElementById("png-tolerance").value || 32);

    pngUndoStack.push(ctx.getImageData(0, 0, canvas.width, canvas.height));
    if (pngUndoStack.length > 15) pngUndoStack.shift();
    floodFillCanvas(ctx, x, y, hexToRgb(hexColor), tol);
  });
}

function hexToRgb(hex) {
  const n = parseInt(hex.replace("#", ""), 16);
  return { r: (n >> 16) & 255, g: (n >> 8) & 255, b: n & 255 };
}

function floodFillCanvas(ctx, startX, startY, fillRgb, tolerance) {
  const w = ctx.canvas.width;
  const h = ctx.canvas.height;
  const imgData = ctx.getImageData(0, 0, w, h);
  const data = imgData.data;

  const startPos = (startY * w + startX) * 4;
  const sr = data[startPos], sg = data[startPos + 1], sb = data[startPos + 2];
  if (Math.abs(sr - fillRgb.r) < 3 && Math.abs(sg - fillRgb.g) < 3 && Math.abs(sb - fillRgb.b) < 3) return;

  const visited = new Uint8Array(w * h);
  const stack = [startX, startY];

  while (stack.length > 0) {
    const y = stack.pop();
    const x = stack.pop();
    const idx = y * w + x;
    if (x < 0 || x >= w || y < 0 || y >= h || visited[idx]) continue;

    const p = idx * 4;
    const dr = Math.abs(data[p] - sr);
    const dg = Math.abs(data[p + 1] - sg);
    const db = Math.abs(data[p + 2] - sb);
    if (dr <= tolerance && dg <= tolerance && db <= tolerance) {
      visited[idx] = 1;
      data[p] = fillRgb.r;
      data[p + 1] = fillRgb.g;
      data[p + 2] = fillRgb.b;
      data[p + 3] = 255;
      stack.push(x + 1, y, x - 1, y, x, y + 1, x, y - 1);
    }
  }
  ctx.putImageData(imgData, 0, 0);
}

// ============================================================================
// イベントリスナー登録
// ============================================================================
function setupEventListeners() {
  // メインタブ切替
  document.querySelectorAll(".tab-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".tab-btn").forEach((b) => b.classList.remove("active"));
      document.querySelectorAll(".tab-panel").forEach((p) => p.classList.remove("active"));
      btn.classList.add("active");
      document.getElementById(btn.getAttribute("data-tab")).classList.add("active");
    });
  });

  // 操作国家切替
  document.getElementById("select-active-nation").addEventListener("change", async (e) => {
    const res = await apiPost("/api/mode", { active_nation_id: e.target.value });
    APP_STATE = res.state;
    renderAll();
  });

  // ゲームモード切替 (まず1: ソロ/プロトタイプ ⇔ のちに2: マルチプレイ)
  document.getElementById("select-game-mode").addEventListener("change", async (e) => {
    const res = await apiPost("/api/mode", { mode: e.target.value });
    APP_STATE = res.state;
    showToast(`モードを『${e.target.value === "sandbox" ? "ソロ/プロトタイプモード" : "マルチプレイモード"}』に切り替えました`);
    renderAll();
  });

  // 次の週へ進行 (+5000億支給)
  document.getElementById("btn-advance-week").addEventListener("click", async () => {
    try {
      const res = await apiPost("/api/advance_week");
      APP_STATE = res.state;
      showToast(`第${APP_STATE.week}週へ進行し、週資金5,000億円（＋割譲ボーナス）を支給しました！`);
      renderAll();
    } catch (err) {
      showToast(err.message, true);
    }
  });

  // 平時マップツール切替
  document.querySelectorAll(".map-tool-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".map-tool-btn").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      PEACE_TOOL = btn.getAttribute("data-ptool");
      document.getElementById("peace-panel-inspect").style.display = PEACE_TOOL === "inspect" ? "block" : "none";
      document.getElementById("peace-panel-found").style.display = PEACE_TOOL === "found" ? "block" : "none";
      document.getElementById("peace-panel-bucket").style.display = PEACE_TOOL === "bucket" ? "block" : "none";
    });
  });

  document.getElementById("chk-show-adj").addEventListener("change", renderPeacetimeMap);
  document.getElementById("chk-show-units").addEventListener("change", renderPeacetimeMap);

  // 平時マップ ズーム・パン
  document.getElementById("btn-peace-zoom-in").addEventListener("click", () => {
    PEACE_VB.w *= 0.8;
    PEACE_VB.h *= 0.8;
    renderPeacetimeMap();
  });
  document.getElementById("btn-peace-zoom-out").addEventListener("click", () => {
    PEACE_VB.w = Math.min(1500, PEACE_VB.w * 1.25);
    PEACE_VB.h = Math.min(1100, PEACE_VB.h * 1.25);
    renderPeacetimeMap();
  });
  document.getElementById("btn-peace-zoom-reset").addEventListener("click", () => {
    PEACE_VB = { x: 150, y: 40, w: 1120, h: 920 };
    renderPeacetimeMap();
  });

  const peaceSvg = document.getElementById("peacetime-svg");
  peaceSvg.addEventListener("mousedown", (e) => {
    if (e.target.closest(".prov-node")) return;
    isPeacePanning = true;
    peacePanStart = { x: e.clientX, y: e.clientY };
  });
  window.addEventListener("mousemove", (e) => {
    if (!isPeacePanning) return;
    const dx = (e.clientX - peacePanStart.x) * (PEACE_VB.w / 900);
    const dy = (e.clientY - peacePanStart.y) * (PEACE_VB.h / 700);
    PEACE_VB.x -= dx;
    PEACE_VB.y -= dy;
    peacePanStart = { x: e.clientX, y: e.clientY };
    renderPeacetimeMap();
  });
  window.addEventListener("mouseup", () => {
    isPeacePanning = false;
  });

  // 建国フォーム送信
  document.getElementById("btn-found-clear-sel").addEventListener("click", () => {
    FOUND_SELECTION = { capital: null, cities: [], extra: [] };
    updateFoundSelectionUI();
    renderPeacetimeMap();
  });

  document.getElementById("btn-submit-found").addEventListener("click", async () => {
    try {
      const res = await apiPost("/api/nation/found", {
        name: document.getElementById("found-name").value,
        flag: document.getElementById("found-flag").value,
        color: document.getElementById("found-color").value,
        leader: document.getElementById("found-leader").value,
        passcode: document.getElementById("found-passcode").value,
        is_ai: document.getElementById("found-is-ai").checked,
        lore: document.getElementById("found-lore").value,
        capital_id: FOUND_SELECTION.capital,
        city_ids: FOUND_SELECTION.cities,
        province_ids: FOUND_SELECTION.extra,
      });
      APP_STATE = res.state;
      FOUND_SELECTION = { capital: null, cities: [], extra: [] };
      updateFoundSelectionUI();
      showToast(`🎉 ${res.nation.flag}${res.nation.name} を建国しました！（初期資金5兆円交付）`);
      renderAll();
    } catch (err) {
      showToast(err.message, true);
    }
  });

  // 戦時マップツール切替
  document.querySelectorAll(".war-tool-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".war-tool-btn").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      WAR_TOOL = btn.getAttribute("data-wtool");
      document.getElementById("war-add-unit-box").style.display = WAR_TOOL === "add_unit" ? "block" : "none";
    });
  });

  document.getElementById("select-active-war").addEventListener("change", (e) => {
    ACTIVE_WAR_ID = e.target.value;
    renderWartimeTab();
  });

  document.getElementById("select-war-theater").addEventListener("change", async (e) => {
    const war = getActiveWar();
    if (!war) return;
    const res = await apiPost("/api/war/tactical_plan", {
      war_id: war.id,
      action: "change_theater",
      theater_id: e.target.value,
    });
    APP_STATE = res.state;
    renderWartimeTab();
  });

  document.getElementById("select-war-layer-view").addEventListener("change", () => {
    const war = getActiveWar();
    if (war) renderTacticalWarSvg(war);
  });

  // 戦時マップ上でのドラッグ描画・部隊配置
  const warSvg = document.getElementById("wartime-svg");
  warSvg.addEventListener("mousedown", (e) => {
    const war = getActiveWar();
    if (!war) return;
    const pt = getSvgPoint(warSvg, e.clientX, e.clientY);

    if (WAR_TOOL === "add_unit") {
      const side = document.getElementById("select-war-side").value;
      const utype = document.getElementById("new-tu-type").value;
      const uname = document.getElementById("new-tu-name").value.trim() || "戦術部隊";
      war.tactical_units = war.tactical_units || [];
      war.tactical_units.push({
        id: "tu_" + Date.now(),
        side,
        nation_id: APP_STATE.active_nation_id,
        name: uname,
        unit_type: utype,
        x: pt.x,
        y: pt.y,
      });
      saveWarPlanSilent(war);
      return;
    }

    if (WAR_TOOL.startsWith("draw_")) {
      isDrawingArrow = true;
      currentDrawPoints = [[pt.x, pt.y]];
      renderTacticalWarSvg(war);
    }
  });

  warSvg.addEventListener("mousemove", (e) => {
    const war = getActiveWar();
    if (!war) return;
    const pt = getSvgPoint(warSvg, e.clientX, e.clientY);

    if (draggingUnitId) {
      const u = (war.tactical_units || []).find((x) => x.id === draggingUnitId);
      if (u) {
        u.x = Math.max(25, Math.min(1055, pt.x));
        u.y = Math.max(25, Math.min(835, pt.y));
        renderTacticalWarSvg(war);
      }
      return;
    }

    if (isDrawingArrow) {
      const last = currentDrawPoints[currentDrawPoints.length - 1];
      if (!last || Math.hypot(pt.x - last[0], pt.y - last[1]) > 28) {
        currentDrawPoints.push([pt.x, pt.y]);
        renderTacticalWarSvg(war);
      }
    }
  });

  window.addEventListener("mouseup", () => {
    const war = getActiveWar();
    if (draggingUnitId && war) {
      draggingUnitId = null;
      saveWarPlanSilent(war);
    }
    if (isDrawingArrow && war) {
      isDrawingArrow = false;
      if (currentDrawPoints.length >= 2) {
        const side = document.getElementById("select-war-side").value;
        const style = WAR_TOOL.replace("draw_", "");
        const styleLabels = { attack: "主攻突破軸", defend: "防衛陣地線", naval: "強襲揚陸・艦隊機動", counter: "機動逆襲" };
        war.tactical_drawings = war.tactical_drawings || [];
        war.tactical_drawings.push({
          id: "td_" + Date.now(),
          side,
          style,
          label: `${side === "attacker" ? "攻" : "防"}:${styleLabels[style] || "作戦線"}`,
          points: currentDrawPoints,
        });
        saveWarPlanSilent(war);
      }
      currentDrawPoints = [];
    }
  });

  document.getElementById("btn-war-clear-drawings").addEventListener("click", () => {
    const war = getActiveWar();
    if (!war) return;
    const side = document.getElementById("select-war-side").value;
    war.tactical_drawings = (war.tactical_drawings || []).filter((d) => d.side !== side);
    saveWarPlanSilent(war);
  });

  document.getElementById("btn-add-strat-target").addEventListener("click", () => {
    const war = getActiveWar();
    if (!war) return;
    const fromP = document.getElementById("war-arrow-from").value;
    const toP = document.getElementById("war-arrow-to").value;
    const atype = document.getElementById("war-arrow-type").value;
    if (!fromP || !toP) return;
    war.tactical_arrows = war.tactical_arrows || [];
    war.tactical_arrows.push({
      id: "arr_" + Date.now(),
      side: "attacker",
      nation_id: war.attackers[0],
      from_prov: fromP,
      to_prov: toP,
      type: atype,
      label: `攻略目標`,
    });
    saveWarPlanSilent(war);
  });

  document.getElementById("btn-save-war-plan").addEventListener("click", async () => {
    const war = getActiveWar();
    if (!war) return;
    await saveWarPlanSilent(war);
    showToast("戦時作戦マップの部隊配置・矢印・ドクトリンを保存しました！");
  });

  document.getElementById("btn-ai-plan-atk").addEventListener("click", async () => {
    const war = getActiveWar();
    if (!war) return;
    const res = await apiPost("/api/war/tactical_plan", { war_id: war.id, action: "ai_plan", side: "attacker" });
    APP_STATE = res.state;
    showToast("🤖 AIが攻撃側の進撃矢印と作戦ドクトリンを自動立案しました！");
    renderWartimeTab();
  });

  document.getElementById("btn-ai-plan-dfn").addEventListener("click", async () => {
    const war = getActiveWar();
    if (!war) return;
    const res = await apiPost("/api/war/tactical_plan", { war_id: war.id, action: "ai_plan", side: "defender" });
    APP_STATE = res.state;
    showToast("🤖 AIが防衛側の防衛線・逆襲計画を自動立案しました！");
    renderWartimeTab();
  });

  document.getElementById("btn-resolve-war").addEventListener("click", async () => {
    const war = getActiveWar();
    if (!war) return;
    const useAi = document.getElementById("chk-use-ai-llm").checked;
    showToast("⚖️ 戦争審判を実行中...");
    try {
      const res = await apiPost("/api/war/resolve", {
        war_id: war.id,
        use_ai_llm: useAi,
        apply_territory: true,
      });
      APP_STATE = res.state;
      showToast(`⚔️ 判定完了: ${res.result.outcome}`);
      renderAll();
    } catch (err) {
      showToast(err.message, true);
    }
  });

  // 作戦ファイル(.milxyz/.json)エクスポート＆インポート
  document.getElementById("btn-export-milx").addEventListener("click", () => {
    const war = getActiveWar();
    if (!war) return;
    const blob = new Blob([JSON.stringify(war, null, 2)], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `${war.id}_tactical_plan.milxyz.json`;
    a.click();
  });

  document.getElementById("input-import-milx").addEventListener("change", (e) => {
    const file = e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = async (ev) => {
      try {
        const imported = JSON.parse(ev.target.result);
        const war = getActiveWar();
        if (!war) return;
        war.tactical_units = imported.tactical_units || war.tactical_units;
        war.tactical_drawings = imported.tactical_drawings || war.tactical_drawings;
        war.attacker_doctrine = imported.attacker_doctrine || war.attacker_doctrine;
        war.defender_doctrine = imported.defender_doctrine || war.defender_doctrine;
        await saveWarPlanSilent(war);
        showToast("📂 作戦ファイルを戦時マップに読み込みました！");
      } catch (err) {
        showToast("ファイルの読み込みに失敗しました", true);
      }
    };
    reader.readAsText(file);
  });

  // 新規宣戦布告モーダル
  document.getElementById("btn-open-declare-war").addEventListener("click", () => {
    const atkGrid = document.getElementById("decl-attackers-list");
    const dfnGrid = document.getElementById("decl-defenders-list");
    atkGrid.innerHTML = "";
    dfnGrid.innerHTML = "";
    for (const n of APP_STATE.nations) {
      atkGrid.innerHTML += `<label class="checkbox-label"><input type="checkbox" class="chk-decl-atk" value="${n.id}" ${n.id === APP_STATE.active_nation_id ? "checked" : ""}/> ${n.flag}${n.name}</label>`;
      dfnGrid.innerHTML += `<label class="checkbox-label"><input type="checkbox" class="chk-decl-dfn" value="${n.id}"/> ${n.flag}${n.name}</label>`;
    }
    document.getElementById("modal-declare-war").style.display = "flex";
  });

  document.getElementById("btn-confirm-declare-war").addEventListener("click", async () => {
    const attackers = Array.from(document.querySelectorAll(".chk-decl-atk:checked")).map((el) => el.value);
    const defenders = Array.from(document.querySelectorAll(".chk-decl-dfn:checked")).map((el) => el.value);
    const name = document.getElementById("decl-war-name").value;
    const theater_id = document.getElementById("decl-war-theater").value;
    try {
      const res = await apiPost("/api/war/declare", { attackers, defenders, name, theater_id });
      APP_STATE = res.state;
      ACTIVE_WAR_ID = res.war.id;
      document.getElementById("modal-declare-war").style.display = "none";
      showToast(`⚔️ ${res.war.name} を宣戦布告しました！`);
      renderAll();
    } catch (err) {
      showToast(err.message, true);
    }
  });

  // 師団ビルダー操作
  document.querySelectorAll(".tpl-load-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const tplId = btn.getAttribute("data-tpl");
      const tpl = CATALOG.division_templates.find((t) => t.id === tplId);
      if (!tpl) return;
      document.getElementById("div-name").value = tpl.name.replace("（公式テンプレ）", "");
      BUILDER_REGIMENTS = tpl.regiments.map((r) => ({ ...r, custom_calc: false }));
      BUILDER_ARTILLERY = tpl.artillery_id;
      BUILDER_SUPPORTS = tpl.supports.map((s) => ({ ...s, custom_calc: false }));
      BUILDER_OVERRIDE_COST = tpl.override_cost || tpl.official_cost;
      renderDivisionBuilderRows();
      renderDivisionSpecPreview();
    });
  });

  document.getElementById("btn-add-regiment").addEventListener("click", () => {
    if (BUILDER_REGIMENTS.length >= 4) {
      showToast("基幹連隊は最大4個までです", true);
      return;
    }
    BUILDER_REGIMENTS.push({ regiment_id: "reg_infantry", tank_id: null, custom_calc: false });
    BUILDER_OVERRIDE_COST = null;
    renderDivisionBuilderRows();
    renderDivisionSpecPreview();
  });

  document.getElementById("builder-artillery").addEventListener("change", (e) => {
    BUILDER_ARTILLERY = e.target.value;
    BUILDER_OVERRIDE_COST = null;
    renderDivisionSpecPreview();
  });

  document.getElementById("btn-add-support").addEventListener("click", () => {
    if (BUILDER_SUPPORTS.length >= 4) {
      showToast("補助大隊は最大4個までです", true);
      return;
    }
    BUILDER_SUPPORTS.push({ support_id: "sup_at", tank_id: null, custom_calc: false });
    BUILDER_OVERRIDE_COST = null;
    renderDivisionBuilderRows();
    renderDivisionSpecPreview();
  });

  document.getElementById("div-count").addEventListener("input", renderDivisionSpecPreview);

  document.getElementById("btn-buy-division").addEventListener("click", async () => {
    const activeNat = getActiveNation();
    if (!activeNat) return;
    try {
      const res = await apiPost("/api/military/division", {
        action: "create",
        nation_id: activeNat.id,
        name: document.getElementById("div-name").value,
        count: Number(document.getElementById("div-count").value || 1),
        province_id: document.getElementById("div-prov").value,
        regiments: BUILDER_REGIMENTS,
        artillery_id: BUILDER_ARTILLERY,
        supports: BUILDER_SUPPORTS,
        override_cost: BUILDER_OVERRIDE_COST,
      });
      APP_STATE = res.state;
      showToast("🪖 新規師団を編成・配備しました！");
      renderAll();
    } catch (err) {
      showToast(err.message, true);
    }
  });

  // カスタム戦車開発モーダル
  document.getElementById("btn-open-custom-tank").addEventListener("click", () => {
    document.getElementById("modal-custom-tank").style.display = "flex";
  });

  document.getElementById("btn-submit-custom-tank").addEventListener("click", async () => {
    try {
      const res = await apiPost("/api/military/custom_tank", {
        name: document.getElementById("ct-name").value,
        base_hull: document.getElementById("ct-hull").value,
        main_gun: document.getElementById("ct-gun").value,
        cost: Number(document.getElementById("ct-cost").value),
        ha: Number(document.getElementById("ct-ha").value),
        sa: Number(document.getElementById("ct-sa").value),
        armor: Number(document.getElementById("ct-armor").value),
        speed: Number(document.getElementById("ct-speed").value),
      });
      APP_STATE = res.state;
      document.getElementById("modal-custom-tank").style.display = "none";
      showToast(`🔧 カスタム戦車『${res.tank.name}』を登録しました！`);
      renderAll();
    } catch (err) {
      showToast(err.message, true);
    }
  });

  // ショップタブ切替・検索
  document.querySelectorAll(".shop-tab-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".shop-tab-btn").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      ACTIVE_SHOP_DOMAIN = btn.getAttribute("data-shop");
      renderProcurementShop();
    });
  });

  document.getElementById("shop-country-filter").addEventListener("change", renderProcurementShop);
  document.getElementById("shop-search").addEventListener("input", renderProcurementShop);

  // 外交・条約・ニュース
  document.getElementById("treaty-type").addEventListener("change", updatePeaceCedeProvincesUI);
  document.getElementById("treaty-nat-b").addEventListener("change", updatePeaceCedeProvincesUI);

  document.getElementById("btn-create-treaty").addEventListener("click", async () => {
    const cedeIds = Array.from(document.querySelectorAll(".chk-cede-prov:checked")).map((c) => c.value);
    try {
      const res = await apiPost("/api/diplomacy/treaty", {
        action: "create",
        type: document.getElementById("treaty-type").value,
        nation_a: document.getElementById("treaty-nat-a").value,
        nation_b: document.getElementById("treaty-nat-b").value,
        name: document.getElementById("treaty-name").value,
        desc: document.getElementById("treaty-desc").value,
        cede_province_ids: cedeIds,
      });
      APP_STATE = res.state;
      showToast(`📜 条約『${res.treaty.name}』を締結・公示しました！`);
      renderAll();
    } catch (err) {
      showToast(err.message, true);
    }
  });

  document.getElementById("btn-post-news").addEventListener("click", async () => {
    const activeNat = getActiveNation();
    try {
      const res = await apiPost("/api/news/post", {
        nation_id: activeNat?.id,
        title: document.getElementById("news-title").value,
        body: document.getElementById("news-body").value,
      });
      APP_STATE = res.state;
      document.getElementById("news-title").value = "";
      document.getElementById("news-body").value = "";
      showToast("📣 国際ニュースに声明を発表しました！");
      renderAll();
    } catch (err) {
      showToast(err.message, true);
    }
  });

  document.getElementById("btn-sync-discord").addEventListener("click", () => {
    fetchDiscordLogs();
    showToast("🔄 Discord SQLite DBから最新ログを取得しました");
  });

  // Discord用フォーマット出力
  document.getElementById("btn-export-discord").addEventListener("click", () => {
    const nat = getActiveNation();
    if (!nat) return;
    const navMap = {};
    for (const u of CATALOG.naval_units) navMap[u.id] = u;
    const airMap = {};
    for (const u of CATALOG.air_units) airMap[u.id] = u;
    const facMap = {};
    for (const f of CATALOG.facilities) facMap[f.id] = f;
    const provById = {};
    for (const p of APP_STATE.provinces) provById[p.id] = p;

    let totalSpent = 0;
    const lines = [
      `# ${nat.flag} ${nat.name} 軍備・内政スレッド報告`,
      `- **元首**: ${nat.leader}`,
      `- **首都**: ★${provById[nat.capital_id]?.name || nat.capital_id}`,
      `- **主要都市**: ${(nat.city_ids || []).map((c) => "●" + (provById[c]?.name || c)).join("、")}`,
      `- **保有プロビンス数**: ${(nat.province_ids || []).length}プロビンス`,
      "",
      `## 🪖 陸軍編成`,
    ];

    for (const d of nat.divisions || []) {
      const sub = +(Number(d.spec?.cost || 0) * Number(d.count || 1)).toFixed(1);
      totalSpent += sub;
      lines.push(`- **${d.name}** × ${d.count}個師団 （単価 ${d.spec?.cost}億 / 小計 ${sub}億）`);
      lines.push(`  - 内訳: ${(d.spec?.breakdown || []).join(" ＋ ")}`);
    }

    lines.push("", `## ⚓ 海軍編成`);
    for (const item of nat.naval_units || []) {
      const u = navMap[item.unit_id];
      if (!u) continue;
      const sub = +(u.cost * item.count).toFixed(1);
      totalSpent += sub;
      lines.push(`- **${u.name}** × ${item.count}隻 （小計 ${sub}億）`);
    }

    lines.push("", `## ✈️ 空軍編成`);
    for (const item of nat.air_units || []) {
      const u = airMap[item.unit_id];
      if (!u) continue;
      const sub = +(u.cost * item.count).toFixed(1);
      totalSpent += sub;
      lines.push(`- **${u.name}** × ${item.count}${u.is_nuke ? "発" : "機"} （小計 ${sub}億）`);
    }

    lines.push("", `## 🏰 施設・その他`);
    for (const fid of nat.facilities || []) {
      const f = facMap[fid];
      if (!f) continue;
      totalSpent += f.cost;
      lines.push(`- **${f.name}** （${f.cost}億）`);
    }

    lines.push(
      "",
      `---`,
      `- **装備・施設使用金合計**: ${formatOku(totalSpent)}`,
      `- **現在残金**: ${formatOku(nat.budget)}`,
      `- **週資金収入**: ${(Number(nat.weekly_income || 5000) + Math.min(1000, Number(nat.war_prov_bonus_oku || 0))).toLocaleString()}億円/週`
    );

    document.getElementById("modal-output-text").value = lines.join("\n");
    document.getElementById("modal-output").style.display = "flex";
  });

  document.getElementById("btn-copy-output").addEventListener("click", () => {
    const txt = document.getElementById("modal-output-text");
    txt.select();
    navigator.clipboard.writeText(txt.value);
    showToast("📋 クリップボードにコピーしました！Discordの自分用スレッドにそのまま貼れます。");
  });

  // シナリオ初期化モーダル
  document.getElementById("btn-scenario-menu").addEventListener("click", () => {
    document.getElementById("modal-scenario").style.display = "flex";
  });

  document.getElementById("btn-reset-aiwa").addEventListener("click", async () => {
    const res = await apiPost("/api/scenario/reset", { scenario_type: "aiwa_current" });
    APP_STATE = res.state;
    ACTIVE_WAR_ID = APP_STATE.wars[0]?.id || null;
    document.getElementById("modal-scenario").style.display = "none";
    showToast("🌍 AIWA 現行サーバー再現シナリオで初期化しました！");
    renderAll();
  });

  document.getElementById("btn-reset-blank").addEventListener("click", async () => {
    const res = await apiPost("/api/scenario/reset", { scenario_type: "blank_map" });
    APP_STATE = res.state;
    ACTIVE_WAR_ID = null;
    document.getElementById("modal-scenario").style.display = "none";
    showToast("🏳️ 白地図から新規スタートしました！『新規建国』モードで建国してください。");
    renderAll();
  });

  // PNGバケツ塗りツール操作
  document.getElementById("png-file-input").addEventListener("change", (e) => {
    const file = e.target.files[0];
    if (!file) return;
    const img = new Image();
    img.onload = () => {
      const canvas = document.getElementById("png-paint-canvas");
      canvas.width = img.width;
      canvas.height = img.height;
      const ctx = canvas.getContext("2d");
      ctx.drawImage(img, 0, 0);
      pngUndoStack = [];
      showToast(`📂 白地図画像 (${img.width}×${img.height}) を読み込みました！クリックでバケツ塗りできます。`);
    };
    img.src = URL.createObjectURL(file);
  });

  document.getElementById("btn-png-undo").addEventListener("click", () => {
    if (pngUndoStack.length === 0) return;
    const canvas = document.getElementById("png-paint-canvas");
    const ctx = canvas.getContext("2d");
    ctx.putImageData(pngUndoStack.pop(), 0, 0);
  });

  document.getElementById("btn-png-download").addEventListener("click", () => {
    const canvas = document.getElementById("png-paint-canvas");
    const a = document.createElement("a");
    a.href = canvas.toDataURL("image/png");
    a.download = `aiwa_map_${Date.now()}.png`;
    a.click();
  });

  // モーダル閉じるボタン共通
  document.querySelectorAll(".modal-close").forEach((btn) => {
    btn.addEventListener("click", () => {
      const target = btn.getAttribute("data-close");
      if (target) document.getElementById(target).style.display = "none";
    });
  });
}

window.addEventListener("DOMContentLoaded", initApp);
