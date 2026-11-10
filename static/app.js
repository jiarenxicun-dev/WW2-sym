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
let ACTIVE_WORLD_ID = localStorage.getItem("aiwa_active_world_id") || "world_admin1";
let PEACE_VB = ACTIVE_WORLD_ID === "world_admin1" ? { x: 0, y: 0, w: 1440, h: 720 } : { x: 45, y: 35, w: 1510, h: 930 };
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
let pngWorldMap = null;

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

function escapeMapText(value) {
  return String(value ?? "").replace(/[&<>"']/g, (ch) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  })[ch]);
}

function formatOku(oku) {
  const val = Number(oku || 0);
  const cho = (val / 10000).toFixed(2);
  return `${cho}兆円 (${val.toLocaleString()}億)`;
}

let IS_STANDALONE_MODE = false;

function syncStandaloneFacilities(state) {
  if (!state || !state.provinces) return;
  const provById = {};
  for (const p of state.provinces) {
    p.has_port = false;
    p.has_fort = false;
    p.has_radar = false;
    p.has_coastal_gun = false;
    p.facilities = [];
    provById[p.id] = p;
  }
  for (const nat of state.nations || []) {
    const pids = nat.province_ids || [];
    const capId = nat.capital_id || pids[0] || "";
    const coastalPid = pids.find((pid) => provById[pid]?.coastal) || capId;
    const normalized = [];
    (nat.facilities || []).forEach((item, idx) => {
      const fid = typeof item === "string" ? item : item?.facility_id || item?.unit_id;
      if (!fid) return;
      const pid = typeof item === "string"
        ? (fid === "fac_naval_port" || fid === "fac_coastal_gun" ? coastalPid : capId)
        : (item.province_id || capId);
      const id = (typeof item === "object" && item?.id) || `finst_${nat.id}_${idx + 1}_${fid}`;
      normalized.push({ id, facility_id: fid, province_id: pid });
      const tp = provById[pid];
      if (tp) {
        if (!tp.facilities.includes(fid)) tp.facilities.push(fid);
        if (fid === "fac_naval_port") tp.has_port = true;
        else if (fid === "fac_fortress") tp.has_fort = true;
        else if (fid === "fac_radar") tp.has_radar = true;
        else if (fid === "fac_coastal_gun") tp.has_coastal_gun = true;
      }
    });
    nat.facilities = normalized;
  }
}

function saveStandaloneState() {
  if (APP_STATE) syncStandaloneFacilities(APP_STATE);
  if (!IS_STANDALONE_MODE || !APP_STATE) return;
  try {
    localStorage.setItem("aiwa_web_standalone_state_v2", JSON.stringify(APP_STATE));
  } catch (e) {}
}

function calcStandaloneDivisionSpec(regiments, artilleryId, supports, overrideCost) {
  const allTanks = getAllTanks();
  const tankMap = {};
  for (const t of allTanks) tankMap[t.id] = t;
  const regMap = {};
  for (const r of CATALOG.base_regiments) regMap[r.id] = r;
  const artMap = {};
  for (const a of CATALOG.artillery_regiments) artMap[a.id] = a;
  const supMap = {};
  for (const s of CATALOG.support_battalions) supMap[s.id] = s;

  let totalCost = 0;
  let minSpeed = 3;
  let canParadrop = true;
  const warnings = [];
  const breakdown = [];
  const unitDescriptions = [];

  (regiments || []).forEach((item, idx) => {
    const r = regMap[item.regiment_id];
    if (!r) return;
    minSpeed = Math.min(minSpeed, r.speed_tier || 1);
    if (!r.can_paradrop) canParadrop = false;
    if (r.is_tank_unit) {
      const tid = item.tank_id || r.default_tank_id || "su_t34_85";
      const tk = tankMap[tid] || tankMap["su_t34_85"];
      const c = !item.custom_calc && (tid === "su_t34_85" || tid === "us_m4_76") ? r.cost : +(tk.cost * 76 + 10).toFixed(1);
      totalCost += c;
      const label = `${r.name}[${tk.name}×76両]`;
      breakdown.push(`${label}: ${c}億`);
      unitDescriptions.push({ slot: `基幹連隊#${idx + 1}`, name: label, cost: c, desc: `${r.desc} （選択車両: ${tk.name} / 単価 ${tk.cost}億 × 76両 ＋ 諸経費10億）` });
    } else {
      totalCost += r.cost;
      breakdown.push(`${r.name}: ${r.cost}億`);
      unitDescriptions.push({ slot: `基幹連隊#${idx + 1}`, name: r.name, cost: r.cost, desc: r.desc });
    }
  });

  const art = artMap[artilleryId || "art_none"] || artMap["art_none"];
  if (art && art.id !== "art_none") {
    totalCost += art.cost;
    breakdown.push(`${art.name}: ${art.cost}億`);
    unitDescriptions.push({ slot: "砲兵連隊", name: art.name, cost: art.cost, desc: art.desc });
    if ((art.max_speed_tier || 3) < minSpeed) {
      warnings.push(`⚠️ ${art.name}は機械化・機甲部隊に追従できないため機動力が低下します`);
    }
    if (!art.can_paradrop) canParadrop = false;
  }

  (supports || []).slice(0, 4).forEach((sItem, idx) => {
    const s = supMap[sItem.support_id];
    if (!s) return;
    if (s.is_tank_unit) {
      const tid = sItem.tank_id || s.default_tank_id || "su_t34_85";
      const tk = tankMap[tid] || tankMap["su_t34_85"];
      const c = !sItem.custom_calc && (tid === "su_t34_85" || tid === "us_m4_76") ? s.cost : +(tk.cost * 22).toFixed(1);
      totalCost += c;
      const label = `${s.name}[${tk.name}×22両]`;
      breakdown.push(`${label}: ${c}億`);
      unitDescriptions.push({ slot: `補助大隊#${idx + 1}`, name: label, cost: c, desc: `${s.desc} （選択車両: ${tk.name} / 単価 ${tk.cost}億 × 22両）` });
    } else {
      totalCost += s.cost;
      breakdown.push(`${s.name}: ${s.cost}億`);
      unitDescriptions.push({ slot: `補助大隊#${idx + 1}`, name: s.name, cost: s.cost, desc: s.desc });
    }
  });

  const finalCost = overrideCost !== null && overrideCost !== undefined ? overrideCost : +totalCost.toFixed(1);
  return {
    cost: finalCost,
    raw_cost: +totalCost.toFixed(1),
    speed_tier: minSpeed,
    can_paradrop: canParadrop,
    breakdown,
    unit_descriptions: unitDescriptions,
    warnings,
  };
}

function handleStandaloneApi(url, data = {}) {
  const state = APP_STATE;
  const findNat = (id) => (state.nations || []).find((n) => n.id === id);

  if (url === "/api/mode") {
    if (data.mode) state.mode = data.mode;
    if (data.active_nation_id) state.active_nation_id = data.active_nation_id;
    saveStandaloneState();
    return { ok: true, state };
  }

  if (url === "/api/scenario/reset") {
    const base = data.scenario_type === "blank_map" ? window.STANDALONE_BOOTSTRAP.state_blank : window.STANDALONE_BOOTSTRAP.state_aiwa;
    const savedTpls = state?.saved_division_templates || [];
    APP_STATE = JSON.parse(JSON.stringify(base));
    APP_STATE.saved_division_templates = savedTpls;
    saveStandaloneState();
    return { ok: true, state: APP_STATE };
  }

  if (url === "/api/advance_week") {
    state.week = Number(state.week || 1) + 1;
    for (const nat of state.nations || []) {
      const bonus = Math.min(1000, Number(nat.war_prov_bonus_oku || 0));
      nat.budget = +(Number(nat.budget || 0) + Number(nat.weekly_income || 5000) + bonus).toFixed(1);
    }
    state.treaties = (state.treaties || []).filter((t) => Number(t.expires_week || 999) >= state.week);
    saveStandaloneState();
    return { ok: true, state };
  }

  if (url === "/api/nation/found") {
    const name = (data.name || "").trim();
    const capId = data.capital_id;
    const cityIds = (data.city_ids || []).filter((c) => c && c !== capId);
    if (!name || !capId || cityIds.length < 2) {
      throw new Error("国名、首都1つ、および都市2つを指定してください（建国ルール）。");
    }
    const provIds = Array.from(new Set([capId, ...cityIds, ...(data.province_ids || [])]));
    const provMap = {};
    for (const p of state.provinces) provMap[p.id] = p;
    for (const pid of provIds) {
      if (provMap[pid]?.owner_id) throw new Error(`プロビンス『${provMap[pid].name}』は既に領有されています。`);
    }
    const nid = "nat_" + Date.now();
    for (const pid of provIds) provMap[pid].owner_id = nid;
    provMap[capId].is_capital = true;
    for (const cid of cityIds.slice(0, 2)) provMap[cid].is_city = true;
    const newNat = {
      id: nid,
      name,
      flag: data.flag || "🏳️",
      color: data.color || "#06b6d4",
      leader: data.leader || "プレイヤー",
      capital_id: capId,
      city_ids: cityIds.slice(0, 2),
      province_ids: provIds,
      initial_province_count: provIds.length,
      white_prov_bought: 0,
      cede_count: 0,
      war_prov_bonus_oku: 0,
      budget: 50000.0,
      weekly_income: 5000.0,
      is_ai: !!data.is_ai,
      lore: data.lore || "",
      facilities: [],
      divisions: [],
      naval_units: [],
      air_units: [],
    };
    state.nations.push(newNat);
    state.active_nation_id = nid;
    saveStandaloneState();
    return { ok: true, state, nation: newNat };
  }

  if (url === "/api/province/action") {
    const prov = state.provinces.find((p) => p.id === data.province_id);
    if (!prov) throw new Error("プロビンスが見つかりません。");
    if (data.action === "buy_white") {
      const nat = findNat(data.nation_id);
      if (!nat) throw new Error("国家を選択してください。");
      if (prov.owner_id) throw new Error("既に領有されています。");
      if ((nat.white_prov_bought || 0) >= 10) throw new Error("白地購入は最大10プロビンスまでです。");
      if (nat.budget < 100) throw new Error("資金不足です（100億円）。");
      nat.budget = +(nat.budget - 100).toFixed(1);
      nat.white_prov_bought = (nat.white_prov_bought || 0) + 1;
      nat.province_ids.push(prov.id);
      prov.owner_id = nat.id;
    } else if (data.action === "bucket_paint") {
      const target = data.target_owner_id || null;
      if (prov.owner_id && prov.owner_id !== target) {
        const oldN = findNat(prov.owner_id);
        if (oldN) {
          oldN.province_ids = oldN.province_ids.filter((x) => x !== prov.id);
          const facMap = {};
          for (const f of CATALOG.facilities) facMap[f.id] = f;
          const keepFacs = [];
          for (const item of (oldN.facilities || [])) {
            const pid = typeof item === "object" ? item.province_id : oldN.capital_id;
            const fid = typeof item === "object" ? item.facility_id : item;
            if (pid === prov.id) {
              const cost = Number(facMap[fid]?.cost || 0);
              oldN.budget = +(oldN.budget + cost).toFixed(1);
            } else {
              keepFacs.push(item);
            }
          }
          oldN.facilities = keepFacs;
        }
      }
      prov.owner_id = target;
      if (target) {
        const newN = findNat(target);
        if (newN && !newN.province_ids.includes(prov.id)) newN.province_ids.push(prov.id);
      }
    }
    saveStandaloneState();
    return { ok: true, state };
  }

  if (url === "/api/military/division") {
    state.saved_division_templates = state.saved_division_templates || [];
    if (data.action === "save_template") {
      const spec = calcStandaloneDivisionSpec(data.regiments, data.artillery_id, data.supports, data.override_cost);
      const tpl = {
        id: "utpl_" + Date.now(),
        name: (data.name || "マイ師団").trim(),
        nation_id: data.nation_id || "",
        regiments: data.regiments,
        artillery_id: data.artillery_id,
        supports: data.supports,
        override_cost: data.override_cost,
        official_cost: spec.cost,
        desc: spec.breakdown.join(" ＋ ") + `（計 ${spec.cost}億）`,
        spec,
      };
      state.saved_division_templates.push(tpl);
      saveStandaloneState();
      return { ok: true, state, template: tpl };
    }
    if (data.action === "delete_template") {
      state.saved_division_templates = state.saved_division_templates.filter((t) => t.id !== data.template_id);
      saveStandaloneState();
      return { ok: true, state };
    }
    const nat = findNat(data.nation_id);
    if (!nat) throw new Error("国家を選択してください。");
    if (data.action === "create") {
      const count = Math.max(1, Number(data.count || 1));
      const spec = calcStandaloneDivisionSpec(data.regiments, data.artillery_id, data.supports, data.override_cost);
      const totalCost = +(spec.cost * count).toFixed(1);
      if (nat.budget < totalCost) throw new Error(`予算不足です（必要: ${totalCost}億 / 残資金: ${nat.budget}億）`);
      nat.budget = +(nat.budget - totalCost).toFixed(1);
      nat.divisions.push({
        id: "div_" + Date.now(),
        name: (data.name || "新編師団").trim(),
        regiments: data.regiments,
        artillery_id: data.artillery_id,
        supports: data.supports,
        override_cost: data.override_cost,
        count,
        province_id: nat.capital_id,
        spec,
      });
      if (data.also_save_template) {
        state.saved_division_templates.push({
          id: "utpl_" + Date.now(),
          name: (data.name || "マイ師団").trim(),
          nation_id: nat.id,
          regiments: data.regiments,
          artillery_id: data.artillery_id,
          supports: data.supports,
          override_cost: data.override_cost,
          official_cost: spec.cost,
          desc: spec.breakdown.join(" ＋ ") + `（計 ${spec.cost}億）`,
          spec,
        });
      }
    } else if (data.action === "adjust_count") {
      const target = (nat.divisions || []).find((d) => d.id === data.division_id);
      if (!target) throw new Error("対象の師団が見つかりません。");
      const delta = Number(data.delta || 0);
      const unitCost = Number(target.spec?.cost || 0);
      if (delta > 0) {
        const need = +(unitCost * delta).toFixed(1);
        if (nat.budget < need) throw new Error(`追加配備の予算が不足しています（必要: ${need}億 / 残資金: ${nat.budget}億）`);
        nat.budget = +(nat.budget - need).toFixed(1);
        target.count += delta;
      } else if (delta < 0) {
        const rem = Math.min(target.count, Math.abs(delta));
        nat.budget = +(nat.budget + unitCost * rem).toFixed(1);
        target.count -= rem;
        if (target.count <= 0) nat.divisions = nat.divisions.filter((d) => d.id !== data.division_id);
      }
    } else if (data.action === "disband") {
      const target = (nat.divisions || []).find((d) => d.id === data.division_id);
      if (!target) throw new Error("解体する師団が見つかりません。");
      const refund = +(Number(target.spec?.cost || 0) * Number(target.count || 1)).toFixed(1);
      nat.budget = +(nat.budget + refund).toFixed(1);
      nat.divisions = nat.divisions.filter((d) => d.id !== data.division_id);
    }
    saveStandaloneState();
    return { ok: true, state };
  }

  if (url === "/api/military/custom_tank") {
    const checkStr = `${data.name || ""} ${data.base_hull || ""} ${data.main_gun || ""}`.toLowerCase();
    if (["t-54", "t54", "is-4", "is4"].some((f) => checkStr.includes(f))) {
      throw new Error("【架空兵器ルール違反】T-54試作およびIS-4は強過ぎるため出禁です！");
    }
    const newTk = {
      id: "custom_tk_" + Date.now(),
      name: data.base_hull ? `${data.name} (${data.base_hull}+${data.main_gun})` : data.name,
      country: "独自開発",
      type: "架空/カスタム戦車",
      cost: Math.max(0.5, Number(data.cost || 3.5)),
      desc: data.desc || "",
    };
    state.custom_tanks = state.custom_tanks || [];
    state.custom_tanks.push(newTk);
    saveStandaloneState();
    return { ok: true, state, tank: newTk };
  }

  if (url === "/api/military/procure") {
    const nat = findNat(data.nation_id);
    if (!nat) throw new Error("国家を選択してください。");
    const count = Math.max(1, Number(data.count || 1));
    if (data.domain === "navy") {
      const u = CATALOG.naval_units.find((x) => x.id === data.unit_id);
      const total = +(u.cost * count).toFixed(1);
      if (data.action === "buy") {
        if (nat.budget < total) throw new Error(`予算不足です（必要: ${total}億）`);
        nat.budget = +(nat.budget - total).toFixed(1);
        const ex = nat.naval_units.find((x) => x.unit_id === data.unit_id);
        if (ex) ex.count += count;
        else nat.naval_units.push({ unit_id: data.unit_id, count });
      } else {
        nat.budget = +(nat.budget + total).toFixed(1);
        nat.naval_units = nat.naval_units.filter((x) => x.unit_id !== data.unit_id);
      }
    } else if (data.domain === "air") {
      const u = CATALOG.air_units.find((x) => x.id === data.unit_id);
      if (u.is_nuke && data.action === "buy") {
        const hasB29 = (nat.air_units || []).some((x) => x.unit_id === "air_us_b29" && x.count > 0);
        if (!hasB29) throw new Error("核兵器は『B-29 スーパーフォートレス』にのみ搭載可能です。");
      }
      const total = +(u.cost * count).toFixed(1);
      if (data.action === "buy") {
        if (nat.budget < total) throw new Error(`予算不足です（必要: ${total}億）`);
        nat.budget = +(nat.budget - total).toFixed(1);
        const ex = nat.air_units.find((x) => x.unit_id === data.unit_id);
        if (ex) ex.count += count;
        else nat.air_units.push({ unit_id: data.unit_id, count });
      } else {
        nat.budget = +(nat.budget + total).toFixed(1);
        nat.air_units = nat.air_units.filter((x) => x.unit_id !== data.unit_id);
      }
    } else if (data.domain === "facility") {
      const f = CATALOG.facilities.find((x) => x.id === data.unit_id);
      syncStandaloneFacilities(state);
      if (data.action === "buy") {
        const pid = data.province_id || nat.capital_id || (nat.province_ids || [])[0];
        const prov = state.provinces.find((p) => p.id === pid);
        if (!prov || prov.owner_id !== nat.id) throw new Error("施設は自国が領有するプロビンスにのみ配備できます。");
        if (["fac_naval_port", "fac_coastal_gun"].includes(f.id) && !prov.coastal) {
          throw new Error(`『${f.name}』は沿岸プロビンスにのみ配備可能です（『${prov.name}』は内陸です）。`);
        }
        if ((nat.facilities || []).some((x) => x.facility_id === f.id && x.province_id === pid)) {
          throw new Error(`『${prov.name}』には既に『${f.name}』が配備されています。`);
        }
        if (nat.budget < f.cost) throw new Error(`予算不足です（必要: ${f.cost}億）`);
        nat.budget = +(nat.budget - f.cost).toFixed(1);
        nat.facilities.push({ id: "finst_" + Date.now(), facility_id: f.id, province_id: pid });
      } else {
        let removed = false;
        nat.facilities = (nat.facilities || []).filter((x) => {
          if (removed) return true;
          if ((data.instance_id && x.id === data.instance_id) || (!data.instance_id && x.facility_id === f.id && (!data.province_id || x.province_id === data.province_id))) {
            removed = true;
            return false;
          }
          return true;
        });
        if (removed) nat.budget = +(nat.budget + f.cost).toFixed(1);
      }
    }
    saveStandaloneState();
    return { ok: true, state };
  }

  if (url === "/api/diplomacy/treaty") {
    if (data.action === "delete") {
      state.treaties = (state.treaties || []).filter((t) => t.id !== data.treaty_id);
      saveStandaloneState();
      return { ok: true, state };
    }
    const tr = {
      id: "tr_" + Date.now(),
      name: data.name || "二国間条約",
      type: data.type || "nap",
      nation_a: data.nation_a,
      nation_b: data.nation_b,
      expires_week: data.type === "transit" ? 999 : state.week + 1,
      desc: data.desc || "",
    };
    state.treaties.push(tr);
    saveStandaloneState();
    return { ok: true, state, treaty: tr };
  }

  if (url === "/api/news/post") {
    const nat = findNat(data.nation_id);
    state.news.unshift({
      id: "news_" + Date.now(),
      week: state.week,
      speaker: nat ? `${nat.flag}${nat.name} 外務省` : "国際通信社",
      flag: nat?.flag || "📰",
      title: data.title || "公式声明",
      body: data.body || "",
    });
    saveStandaloneState();
    return { ok: true, state };
  }

  saveStandaloneState();
  return { ok: true, state };
}

async function apiPost(url, data = {}) {
  if (IS_STANDALONE_MODE) {
    return handleStandaloneApi(url, data);
  }
  if (!data.world_id && APP_STATE && APP_STATE.world_id) {
    data.world_id = APP_STATE.world_id;
  }
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
    const res = await fetch(`/api/bootstrap?world=${ACTIVE_WORLD_ID}`);
    if (!res.ok) throw new Error("Static web mode");
    const data = await res.json();
    CATALOG = data.catalog;
    APP_STATE = data.state;
    if (APP_STATE.wars && APP_STATE.wars.length > 0) {
      ACTIVE_WAR_ID = APP_STATE.wars[0].id;
    }
    setupEventListeners();
    initPngPainterCanvas();
    ACTIVE_WORLD_ID = data.active_world_id || APP_STATE.world_id || ACTIVE_WORLD_ID;
    localStorage.setItem("aiwa_active_world_id", ACTIVE_WORLD_ID);
    const selWorld = document.getElementById("select-active-world");
    if (selWorld) selWorld.value = ACTIVE_WORLD_ID;
    renderAll();
    connectWebSocket();
    fetchDiscordLogs();
  } catch (err) {
    if (window.STANDALONE_BOOTSTRAP) {
      IS_STANDALONE_MODE = true;
      CATALOG = window.STANDALONE_BOOTSTRAP.catalog;
      let saved = null;
      try {
        saved = JSON.parse(localStorage.getItem("aiwa_web_standalone_state_v2") || "null");
      } catch (e) {}
      APP_STATE = saved || JSON.parse(JSON.stringify(window.STANDALONE_BOOTSTRAP.state_aiwa));
      if (APP_STATE.wars && APP_STATE.wars.length > 0) {
        ACTIVE_WAR_ID = APP_STATE.wars[0].id;
      }
      setupEventListeners();
      initPngPainterCanvas();
      renderAll();
      showToast("🌐 Webブラウザ完結モード（自動保存有効）で起動しました！");
      return;
    }
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
  syncStandaloneFacilities(APP_STATE);
  renderTopbar();
  renderPeacetimeMap();
  updateFoundSelectionUI();
  renderStateSearch();
  renderProvinceInspectPanel();
  renderPeacetimeNationList();
  renderWartimeTab();
  renderMilitaryTab();
  renderDiplomacyTab();
}

function getProvinceFacilityIcons(p) {
  const icons = [];
  if (p.has_port) icons.push({ icon: "⚓", color: "#38bdf8", label: "軍港" });
  if (p.has_radar) icons.push({ icon: "📡", color: "#a78bfa", label: "防空レーダー網" });
  if (p.has_fort) icons.push({ icon: "🏰", color: "#e2e8f0", label: "永久要塞線" });
  if (p.has_coastal_gun) icons.push({ icon: "🛡️", color: "#f97316", label: "海岸砲要塞" });
  return icons;
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
// TAB 1: 平時マップ（欧州・地中海 リアル地理プロビンスSVGマップ）
// ============================================================================
const TERRAIN_COLORS = {
  plains: "#777d58",
  urban: "#777365",
  mountain: "#77705e",
  forest: "#596b4b",
  coastal: "#79836a",
  desert: "#a89970",
};

function generateProvincePolygonPoints(prov, allProvs) {
  const angles = 10;
  const baseRadius = 34;
  const pts = [];
  for (let i = 0; i < angles; i++) {
    const ang = (Math.PI * 2 * i) / angles;
    const dx = Math.cos(ang);
    const dy = Math.sin(ang);
    let r = baseRadius;
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


async function switchWorld(worldId) {
  const container = document.getElementById("world-admin1-container");
  if (container) container.remove();
  WORLD_ADMIN1_RENDERED = false;
  WORLD_PATH_MAP = {};
  ACTIVE_WORLD_ID = worldId;
  localStorage.setItem("aiwa_active_world_id", worldId);
  if (ACTIVE_WORLD_ID === "world_admin1") {
    PEACE_VB = { x: 0, y: 0, w: 1440, h: 720 };
  } else {
    PEACE_VB = { x: 45, y: 35, w: 1510, h: 930 };
  }
  SELECTED_PROV_ID = null;
  FOUND_SELECTION = { capital: null, cities: [], extra: [] };
  try {
    const res = await fetch(`/api/bootstrap?world=${ACTIVE_WORLD_ID}`);
    if (res.ok) {
      const data = await res.json();
      APP_STATE = data.state;
      const selWorld = document.getElementById("select-active-world");
      if (selWorld) selWorld.value = ACTIVE_WORLD_ID;
      renderAll();
      showToast(`ワールドを『${APP_STATE.name || worldId}』に切り替えました。`);
    }
  } catch (err) {
    showToast("ワールド切替に失敗しました: " + err.message, true);
  }
}

let WORLD_ADMIN1_RENDERED = false;
let WORLD_PATH_MAP = {};
let WORLD_MARKER_GROUP = null;
let WORLD_ADJ_GROUP = null;
let WORLD_BADGES_GROUP = null;

function renderWorldAdmin1Map(svg, tooltip, provs, provById, nationsById) {
  const wMap = window.WORLD_ADMIN1_MAP || null;
  const showAdj = document.getElementById("chk-show-adj")?.checked ?? false;
  const showUnits = document.getElementById("chk-show-units")?.checked ?? true;
  const showIslandMarkers = document.getElementById("chk-show-island-markers")?.checked ?? true;
  const mapStyle = document.getElementById("select-peace-map-style")?.value || "political";

  svg.setAttribute("viewBox", `${PEACE_VB.x} ${PEACE_VB.y} ${PEACE_VB.w} ${PEACE_VB.h}`);

  const container = document.getElementById("world-admin1-container");
  if (!container) {
    // 初回ビルド
    WORLD_ADMIN1_RENDERED = false;
    WORLD_PATH_MAP = {};
    svg.innerHTML = `
      <defs>
        <radialGradient id="worldOceanGrad" cx="50%" cy="45%" r="70%">
          <stop offset="0%" stop-color="#1b2a3a" />
          <stop offset="100%" stop-color="#0c1520" />
        </radialGradient>
        <pattern id="worldSeaGrid" width="60" height="60" patternUnits="userSpaceOnUse">
          <path d="M 60 0 L 0 0 0 60" fill="none" stroke="rgba(255,255,255,0.02)" stroke-width="0.8"/>
        </pattern>
      </defs>
      <g id="world-admin1-container">
        <rect x="-100" y="-100" width="1640" height="920" fill="url(#worldOceanGrad)" />
        <rect x="-100" y="-100" width="1640" height="920" fill="url(#worldSeaGrid)" />
        <g id="world-provs-layer"></g>
        <g id="world-adj-layer"></g>
        <g id="world-island-markers-layer"></g>
        <g id="world-badges-layer"></g>
      </g>
    `;

    const provsLayer = document.getElementById("world-provs-layer");
    const frag = document.createDocumentFragment();

    for (const p of provs) {
      const pData = wMap?.provinces?.[p.id];
      if (!pData || !pData.path) continue;
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      g.classList.add("prov-node");
      g.setAttribute("data-prov-id", p.id);
      g.style.cursor = "pointer";

      const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
      path.classList.add("prov-path");
      path.setAttribute("d", pData.path);
      path.setAttribute("fill-rule", "evenodd");
      path.setAttribute("vector-effect", "non-scaling-stroke");
      g.appendChild(path);
      frag.appendChild(g);

      WORLD_PATH_MAP[p.id] = path;
    }
    provsLayer.appendChild(frag);

    // Island markers
    const markerGroup = document.getElementById("world-island-markers-layer");
    if (wMap?.island_markers) {
      const mFrag = document.createDocumentFragment();
      for (const m of wMap.island_markers) {
        const c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        c.classList.add("island-marker");
        c.setAttribute("data-prov-id", m.id);
        c.setAttribute("cx", m.cx);
        c.setAttribute("cy", m.cy);
        c.setAttribute("r", m.r);
        mFrag.appendChild(c);
      }
      markerGroup.appendChild(mFrag);
    }
    WORLD_MARKER_GROUP = markerGroup;

    // Adjacent connections
    const adjGroup = document.getElementById("world-adj-layer");
    const drawnPairs = new Set();
    const adjFrag = document.createDocumentFragment();
    for (const p of provs) {
      const p1 = wMap?.provinces?.[p.id];
      if (!p1) continue;
      for (const nbId of p.neighbors || []) {
        const pairKey = [p.id, nbId].sort().join("--");
        if (drawnPairs.has(pairKey)) continue;
        drawnPairs.add(pairKey);
        const p2 = wMap?.provinces?.[nbId];
        if (!p2) continue;
        const dist = Math.hypot(p1.cx - p2.cx, p1.cy - p2.cy);
        if (dist > 180) continue;
        const isSea = dist > 45;
        const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
        line.setAttribute("x1", p1.cx);
        line.setAttribute("y1", p1.cy);
        line.setAttribute("x2", p2.cx);
        line.setAttribute("y2", p2.cy);
        line.setAttribute("stroke", isSea ? "rgba(56,189,248,0.5)" : "rgba(255,255,255,0.22)");
        line.setAttribute("stroke-width", isSea ? "1.1" : "0.9");
        if (isSea) line.setAttribute("stroke-dasharray", "3,3");
        line.setAttribute("pointer-events", "none");
        adjFrag.appendChild(line);
      }
    }
    adjGroup.appendChild(adjFrag);
    WORLD_ADJ_GROUP = adjGroup;

    // Tooltip and Click events (登録は初回のみ！)
    svg.querySelectorAll(".prov-node, .island-marker").forEach((node) => {
      const pid = node.getAttribute("data-prov-id");
      const showTooltip = (e) => {
        const p = APP_STATE?.provinces?.find((x) => x.id === pid) || provById[pid];
        if (!p) return;
        const owner = APP_STATE?.nations?.find((n) => n.id === p.owner_id);
        const facIcons = getProvinceFacilityIcons(p);
        const facText = facIcons.length > 0 ? facIcons.map((f) => `${f.icon}${f.label}`).join("・") : "なし";
        tooltip.textContent = `${p.name} (${p.id})
国/地域: ${p.region || "不明"}
面積: ${p.area_km2 ? p.area_km2.toLocaleString() + " km²" : "不明"}
${p.coastal ? "沿岸" : "内陸"}
領有国: ${owner ? `${owner.flag || ""} ${owner.name}` : "未領有（白地）"}
配備施設: ${facText}`;
        tooltip.hidden = false;
        const rect = tooltip.parentElement.getBoundingClientRect();
        const x = e.clientX - rect.left + 14;
        const y = e.clientY - rect.top + 14;
        tooltip.style.left = `${Math.max(0, Math.min(x, rect.width - tooltip.offsetWidth))}px`;
        tooltip.style.top = `${Math.max(0, Math.min(y, rect.height - tooltip.offsetHeight))}px`;
      };
      node.addEventListener("mouseenter", showTooltip);
      node.addEventListener("mousemove", showTooltip);
      node.addEventListener("mouseleave", () => { tooltip.hidden = true; });
      node.addEventListener("click", (e) => {
        e.stopPropagation();
        if (window.peaceDragMoved) return; // ドラッグ後の誤クリックを防止
        onPeacetimeProvinceClick(pid);
      });
    });

    WORLD_ADMIN1_RENDERED = true;
  }

  // 2回目以降：属性の高速差分更新（DOM再生成ゼロ！）
  if (WORLD_MARKER_GROUP) {
    WORLD_MARKER_GROUP.style.display = showIslandMarkers ? "" : "none";
  }
  if (WORLD_ADJ_GROUP) {
    WORLD_ADJ_GROUP.style.display = showAdj ? "" : "none";
  }

  for (const p of provs) {
    const path = WORLD_PATH_MAP[p.id];
    if (!path) continue;
    const owner = p.owner_id ? nationsById[p.owner_id] : null;

    let fill = "#f1f0eb";
    let fillOpacity = "0.90";
    let stroke = "rgba(71,85,105,0.45)";
    let strokeW = "0.45";

    if (owner) {
      fill = owner.color;
      fillOpacity = "0.75";
      stroke = "rgba(15,23,42,0.85)";
      strokeW = "0.65";
    } else if (mapStyle === "hq_dark") {
      fill = "#1e293b";
      fillOpacity = "0.92";
      stroke = "#334155";
      strokeW = "0.45";
    }

    const isSelected = p.id === SELECTED_PROV_ID;
    const foundFill = getFoundFill(p.id);
    if (foundFill) {
      fill = foundFill;
      fillOpacity = "0.9";
    }

    if (isSelected || foundFill) {
      stroke = "#facc15";
      strokeW = "1.8";
    }

    path.setAttribute("fill", fill);
    path.setAttribute("fill-opacity", fillOpacity);
    path.setAttribute("stroke", stroke);
    path.setAttribute("stroke-width", strokeW);
  }

  WORLD_MARKER_GROUP?.querySelectorAll(".island-marker").forEach((marker) => {
    marker.style.fill = getFoundFill(marker.getAttribute("data-prov-id")) || "";
  });

  // Badges Layer (首都・都市・施設バッジ)
  let badgesGroup = document.getElementById("world-badges-layer");
  if (!badgesGroup) {
    badgesGroup = document.createElementNS("http://www.w3.org/2000/svg", "g");
    badgesGroup.id = "world-badges-layer";
    container.appendChild(badgesGroup);
  }
  let bHtml = "";
  for (const p of provs) {
    const pData = wMap?.provinces?.[p.id];
    if (!pData) continue;
    const cx = pData.cx;
    const cy = pData.cy;
    const isFoundCap = PEACE_TOOL === "found" && FOUND_SELECTION.capital === p.id;
    const isFoundCity = PEACE_TOOL === "found" && FOUND_SELECTION.cities.includes(p.id);

    if (p.is_capital || isFoundCap) {
      bHtml += `<text x="${cx}" y="${cy}" font-size="11" fill="#fbbf24" text-anchor="middle" dominant-baseline="central" pointer-events="none" filter="drop-shadow(0 1px 2px rgba(0,0,0,0.8))">★</text>`;
    } else if (p.is_city || isFoundCity) {
      bHtml += `<text x="${cx}" y="${cy}" font-size="8.5" fill="#f8fafc" text-anchor="middle" dominant-baseline="central" pointer-events="none" filter="drop-shadow(0 1px 2px rgba(0,0,0,0.8))">●</text>`;
    }
    if (showUnits) {
      const facIcons = getProvinceFacilityIcons(p);
      if (facIcons.length > 0) {
        const iconsStr = facIcons.map((f) => f.icon).join("");
        const badgeW = Math.max(16, facIcons.length * 10 + 6);
        bHtml += `
          <g transform="translate(${cx}, ${cy - 9})" pointer-events="none">
            <rect x="${-badgeW / 2}" y="-6" width="${badgeW}" height="12" rx="2.5" fill="rgba(15,23,42,0.88)" stroke="rgba(56,189,248,0.75)" stroke-width="0.9" />
            <text x="0" y="0.5" text-anchor="middle" dominant-baseline="central" font-size="7.8">${iconsStr}</text>
          </g>
        `;
      }
    }
  }
  badgesGroup.innerHTML = bHtml;
}

function getFoundFill(provinceId) {
  if (PEACE_TOOL !== "found") return null;
  if (FOUND_SELECTION.capital === provinceId) return "var(--found-capital)";
  if (FOUND_SELECTION.cities.includes(provinceId)) return "var(--found-city)";
  if (FOUND_SELECTION.extra.includes(provinceId)) return "var(--found-extra)";
  return null;
}

function renderPeacetimeMap() {
  const svg = document.getElementById("peacetime-svg");
  const tooltip = document.getElementById("hoi4-state-tooltip");
  tooltip.hidden = true;

  const isWorldAdmin1 = (APP_STATE.world_id === "world_admin1" || APP_STATE.scenario_type === "world_admin1");
  const nationsById = {};
  for (const n of APP_STATE.nations) nationsById[n.id] = n;
  const provs = APP_STATE.provinces;
  const provById = {};
  for (const p of provs) provById[p.id] = p;

  if (isWorldAdmin1) {
    return renderWorldAdmin1Map(svg, tooltip, provs, provById, nationsById);
  }

  svg.setAttribute("viewBox", `${PEACE_VB.x} ${PEACE_VB.y} ${PEACE_VB.w} ${PEACE_VB.h}`);
  const showAdj = document.getElementById("chk-show-adj")?.checked ?? false;
  const showUnits = document.getElementById("chk-show-units")?.checked ?? true;
  const showTerrain = document.getElementById("chk-show-terrain")?.checked ?? true;
  const mapStyle = document.getElementById("select-peace-map-style")?.value || "political";
  const rmap = window.REALISTIC_MAP_DATA || null;
  const seaBgColor = mapStyle === "hq_dark" ? "#15262a" : "#273f43";

  let html = `
    <defs>
      <radialGradient id="oceanGrad" cx="48%" cy="45%" r="65%">
        <stop offset="0%" stop-color="${mapStyle === "hq_dark" ? "#253c3d" : "#486766"}" />
        <stop offset="100%" stop-color="${seaBgColor}" />
      </radialGradient>
      <pattern id="seaGrid" width="40" height="40" patternUnits="userSpaceOnUse">
        <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(220,218,181,0.025)" stroke-width="0.8"/>
      </pattern>
      <filter id="landDropShadow" x="-5%" y="-5%" width="110%" height="110%">
        <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-color="#000000" flood-opacity="0.55" />
      </filter>
    </defs>

    <!-- 1. 海洋ベース＆経緯度グリッド -->
    <rect x="-100" y="-100" width="1800" height="1200" fill="url(#oceanGrad)" />
    <rect x="-100" y="-100" width="1800" height="1200" fill="url(#seaGrid)" />
  `;

  if (rmap) {
    // 大陸棚（浅瀬グラデーション）
    if (rmap.shelf_outer_path) {
      html += `<path d="${rmap.shelf_outer_path}" fill="${mapStyle === "hq_dark" ? "rgba(112,146,137,0.10)" : "rgba(149,177,159,0.14)"}" stroke="none" pointer-events="none" />`;
    }
    if (rmap.shelf_inner_path) {
      html += `<path d="${rmap.shelf_inner_path}" fill="${mapStyle === "hq_dark" ? "rgba(143,171,151,0.10)" : "rgba(166,190,166,0.16)"}" stroke="none" pointer-events="none" />`;
    }
    // 経緯度線 (Graticules)
    if (rmap.graticules_path) {
      html += `<path d="${rmap.graticules_path}" fill="none" stroke="rgba(222,220,189,0.08)" stroke-width="0.7" stroke-dasharray="3,4" pointer-events="none" />`;
    }
    // 大陸全体のドロップシャドウ＆隙間防止アンダーレイ
    if (rmap.land_base_path) {
      html += `<path d="${rmap.land_base_path}" fill="#686d52" filter="url(#landDropShadow)" pointer-events="none" />`;
    }
    // 周辺中立陸地（イラン・カザフ・アラビア内陸・フェロー等）
    if (rmap.neutral_land_path) {
      html += `<path d="${rmap.neutral_land_path}" fill="#696f56" stroke="#4c5547" stroke-width="0.8" pointer-events="none" />`;
    }
  }

  // 2. プロビンス領土ポリゴン描画（Natural Earth 50m 精密海岸線＋有機的州境）
  for (const p of provs) {
    const owner = p.owner_id ? nationsById[p.owner_id] : null;
    const rProv = rmap?.provinces?.[p.id];
    const cx = rProv ? rProv.cx : p.x;
    const cy = rProv ? rProv.cy : p.y;
    const terrainCol = TERRAIN_COLORS[p.terrain] || "#1e293b";

    let fill = terrainCol;
    let fillOpacity = "0.90";
    let stroke = "rgba(148,163,184,0.35)";
    let strokeW = "0.75";

    if (mapStyle === "political") {
      if (owner) {
        fill = owner.color;
        fillOpacity = "0.55";
        stroke = "rgba(36,43,35,0.65)";
        strokeW = "0.8";
      } else {
        fill = terrainCol;
        fillOpacity = "0.86";
        stroke = "rgba(40,48,38,0.55)";
        strokeW = "0.75";
      }
    } else if (mapStyle === "terrain") {
      fill = terrainCol;
      fillOpacity = "0.94";
      stroke = owner ? owner.color : "rgba(148,163,184,0.35)";
      strokeW = owner ? "1.6" : "0.7";
    } else if (mapStyle === "hq_dark") {
      fill = owner ? owner.color : "#0f172a";
      fillOpacity = owner ? "0.38" : "0.88";
      stroke = owner ? owner.color : "#1e293b";
      strokeW = owner ? "1.4" : "0.8";
    }

    const isSelected = p.id === SELECTED_PROV_ID;
    const foundFill = getFoundFill(p.id);
    if (foundFill) {
      fill = foundFill;
      fillOpacity = "0.9";
    }

    if (isSelected || foundFill) {
      stroke = "#facc15";
      strokeW = "2.6";
    }

    html += `<g class="prov-node" data-prov-id="${p.id}" style="cursor:pointer;">`;

    if (rProv && rProv.path) {
      // 下地に自然地形色を敷き、その上に領有国カラーを重ねることで重厚な地図質感を出す
      html += `<path d="${rProv.path}" fill="${terrainCol}" fill-opacity="0.92" stroke="none" />`;
      if (owner && mapStyle === "terrain" && !foundFill) {
        html += `<path d="${rProv.path}" fill="${owner.color}" fill-opacity="0.26" stroke="${stroke}" stroke-width="${strokeW}" stroke-linejoin="round" />`;
      } else {
        html += `<path d="${rProv.path}" fill="${fill}" fill-opacity="${fillOpacity}" stroke="${stroke}" stroke-width="${strokeW}" stroke-linejoin="round" />`;
      }
    } else {
      const polyPts = generateProvincePolygonPoints(p, provs);
      html += `<polygon points="${polyPts}" fill="${fill}" fill-opacity="${fillOpacity}" stroke="${stroke}" stroke-width="${strokeW}" />`;
    }

    html += `</g>`;
  }

  // 3. 湖沼レイヤー
  if (rmap && showTerrain) {
    if (rmap.lakes_path) {
      html += `<path d="${rmap.lakes_path}" fill="#557b78" stroke="#9bbcb0" stroke-opacity="0.65" stroke-width="0.65" pointer-events="none" />`;
    }
  }

  // 海岸線シャープ輪郭オーバーレイ
  if (rmap && rmap.land_base_path) {
    html += `<path d="${rmap.land_base_path}" fill="none" stroke="rgba(33, 48, 42, 0.75)" stroke-width="1.2" stroke-linejoin="round" pointer-events="none" />`;
  }

  // 海域名ラベル（地図帳風の優雅な配置）
  html += `
    <g pointer-events="none" opacity="0.48" font-family="Georgia, serif">
      <text x="145" y="495" fill="#d0ded0" font-size="15" font-style="italic" letter-spacing="3">ATLANTIC OCEAN (大西洋)</text>
      <text x="455" y="305" fill="#d0ded0" font-size="11.5" font-style="italic" letter-spacing="2">北海 (NORTH SEA)</text>
      <text x="765" y="295" fill="#d0ded0" font-size="11" font-style="italic" letter-spacing="1.5">バルト海 (BALTIC)</text>
      <text x="475" y="625" fill="#d0ded0" font-size="10.5" font-style="italic">リオン湾</text>
      <text x="695" y="758" fill="#d0ded0" font-size="14" font-style="italic" letter-spacing="3">MEDITERRANEAN SEA (地中海)</text>
      <text x="1115" y="568" fill="#d0ded0" font-size="12" font-style="italic" letter-spacing="2">黒海 (BLACK SEA)</text>
    </g>
  `;

  // 4. 隣接ネットワーク線（ON時）
  if (showAdj) {
    const drawnPairs = new Set();
    for (const p of provs) {
      const rp1 = rmap?.provinces?.[p.id];
      const x1 = rp1 ? rp1.cx : p.x;
      const y1 = rp1 ? rp1.cy : p.y;
      for (const nbId of p.neighbors || []) {
        const pairKey = [p.id, nbId].sort().join("--");
        if (drawnPairs.has(pairKey)) continue;
        drawnPairs.add(pairKey);
        const nb = provById[nbId];
        if (!nb) continue;
        const rp2 = rmap?.provinces?.[nbId];
        const x2 = rp2 ? rp2.cx : nb.x;
        const y2 = rp2 ? rp2.cy : nb.y;
        const isSeaLink = Math.hypot(x1 - x2, y1 - y2) > 95;
        html += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}"
          stroke="${isSeaLink ? "rgba(56,189,248,0.45)" : "rgba(226,232,240,0.28)"}"
          stroke-width="${isSeaLink ? "1.3" : "1.2"}"
          ${isSeaLink ? 'stroke-dasharray="4,4"' : ""} pointer-events="none" />`;
      }
    }
  }

  const zoomedOut = PEACE_VB.w > 980;
  if (zoomedOut) {
    const centroids = {};
    for (const p of provs) {
      if (!p.owner_id || !nationsById[p.owner_id]) continue;
      const rp = rmap?.provinces?.[p.id];
      const point = centroids[p.owner_id] ||= { x: 0, y: 0, count: 0 };
      point.x += rp?.cx ?? p.x;
      point.y += rp?.cy ?? p.y;
      point.count++;
    }
    for (const [id, point] of Object.entries(centroids)) {
      const nation = nationsById[id];
      html += `<text class="nation-label" x="${point.x / point.count}" y="${point.y / point.count}" text-anchor="middle" fill="#fff4cf" font-size="15" font-weight="800" paint-order="stroke" stroke="#17201c" stroke-width="3" stroke-linejoin="round" pointer-events="none">${escapeMapText(nation.flag)} ${escapeMapText(nation.name)}</text>`;
    }
  }

  // 5. 都市・首都ポイント・ラベル・施設バッジ（最前面レイヤー）
  for (const p of provs) {
    const rProv = rmap?.provinces?.[p.id];
    const cx = rProv ? rProv.cx : p.x;
    const cy = rProv ? rProv.cy : p.y;
    const isFoundCap = PEACE_TOOL === "found" && FOUND_SELECTION.capital === p.id;
    const isFoundCity = PEACE_TOOL === "found" && FOUND_SELECTION.cities.includes(p.id);
    const facIcons = showUnits ? getProvinceFacilityIcons(p) : [];
    if (!p.is_capital && !p.is_city && !isFoundCap && !isFoundCity && facIcons.length === 0) continue;
    const shortName = p.name.split("(")[0];
    const labelFontSize = zoomedOut ? 8.4 : Math.max(5.2, Math.min(8.5, (PEACE_VB.w / 1500) * 8.8));

    let badges = "";
    if (p.is_capital || isFoundCap) badges += "★";
    else if (p.is_city || isFoundCity) badges += "●";
    if (showUnits && facIcons.length > 0) {
      badges += (badges ? " " : "") + facIcons.map((f) => f.icon).join("");
    }

    const dotR = (p.is_capital || isFoundCap) ? 4.6 : ((p.is_city || isFoundCity) ? 3.4 : 2.5);
    const dotCol = (p.is_capital || isFoundCap) ? "#fde047" : ((p.is_city || isFoundCity) ? "#f8fafc" : "#38bdf8");

    html += `
      <g class="prov-label-node" data-prov-id="${p.id}" style="cursor:pointer;">
        <circle cx="${cx}" cy="${cy}" r="${dotR}" fill="${dotCol}" stroke="#0f172a" stroke-width="1" />
        <text x="${cx}" y="${cy - 6}" text-anchor="middle" fill="#ffffff" font-size="${labelFontSize}" font-weight="700" style="text-shadow: 0 1px 3px #000, 0 0 2px #000;">
          ${badges ? badges + " " : ""}${escapeMapText(shortName)}
        </text>
      </g>
    `;
  }

  svg.innerHTML = html;

  // プロビンスクリックイベント登録
  svg.querySelectorAll(".prov-node, .prov-label-node").forEach((node) => {
    const p = provById[node.getAttribute("data-prov-id")];
    const showTooltip = (e) => {
      const owner = nationsById[p.owner_id];
      const facIcons = getProvinceFacilityIcons(p);
      const facText = facIcons.length > 0 ? facIcons.map((f) => `${f.icon}${f.label}`).join("・") : "なし";
      tooltip.textContent = `${p.name} (${p.id})\n地域: ${p.region || "不明"}\n地形: ${p.terrain || "不明"}\n${p.coastal ? "沿岸" : "内陸"}\n領有国: ${owner ? `${owner.flag || ""} ${owner.name}` : "未領有"}\n配備施設: ${facText}`;
      tooltip.hidden = false;
      const rect = tooltip.parentElement.getBoundingClientRect();
      const x = e.clientX - rect.left + 14;
      const y = e.clientY - rect.top + 14;
      tooltip.style.left = `${Math.max(0, Math.min(x, rect.width - tooltip.offsetWidth))}px`;
      tooltip.style.top = `${Math.max(0, Math.min(y, rect.height - tooltip.offsetHeight))}px`;
    };
    node.addEventListener("mouseenter", showTooltip);
    node.addEventListener("mousemove", showTooltip);
    node.addEventListener("mouseleave", () => { tooltip.hidden = true; });
    node.addEventListener("click", (e) => {
      e.stopPropagation();
      const pid = node.getAttribute("data-prov-id");
      onPeacetimeProvinceClick(pid);
    });
  });
}

function renderStateSearch() {
  const region = document.getElementById("state-region-filter");
  const query = document.getElementById("state-search").value.trim().toLocaleLowerCase();
  const selectedRegion = region.value;
  const regions = [...new Set(APP_STATE.provinces.map((p) => p.region).filter(Boolean))].sort();
  region.replaceChildren(new Option("すべての地域", ""), ...regions.map((name) => new Option(name, name)));
  region.value = regions.includes(selectedRegion) ? selectedRegion : "";
  const results = document.getElementById("state-search-results");
  results.replaceChildren(...APP_STATE.provinces.filter((p) =>
    (!region.value || p.region === region.value) &&
    `${p.name} ${p.id}`.toLocaleLowerCase().includes(query)
  ).map((p) => new Option(`${p.name} (${p.id}) — ${p.region || "不明"}`, p.id)));
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

function getFoundSelection() {
  const { capital, cities, extra } = FOUND_SELECTION;
  const provinces = new Map(APP_STATE.provinces.map((p) => [p.id, p]));
  return { capital, cities, provinces, selected: new Set([capital, ...cities, ...extra].filter(Boolean)) };
}

function getFoundPaths(capital, provinces, canEnter) {
  const previous = new Map([[capital, null]]);
  const queue = [capital];
  for (let i = 0; i < queue.length; i++) {
    const id = queue[i];
    for (const next of provinces.get(id)?.neighbors || []) {
      if (previous.has(next) || !canEnter(next)) continue;
      previous.set(next, id);
      queue.push(next);
    }
  }
  return previous;
}

function getFoundReadiness({ capital, cities, provinces, selected }) {
  if (!capital || cities.length !== 2) {
    return { message: "白地の首都1つと主要都市2つを選んでください。" };
  }
  for (const id of selected) {
    const province = provinces.get(id);
    if (!province || province.owner_id) {
      return { message: `「${province?.name || id}」は選択できません。別の白地を選んでください。` };
    }
  }
  const paths = getFoundPaths(capital, provinces, (id) => selected.has(id));
  const disconnected = cities.filter((id) => !paths.has(id));
  if (disconnected.length) {
    const names = disconnected.map((id) => provinces.get(id).name).join("、");
    return {
      message: `首都と「${names}」がつながっていません。間の白地も追加領土に選んでください。`,
      disconnected: true,
    };
  }
  return { message: "首都と主要都市2つがつながっています。", ready: true };
}

function updateFoundSelectionUI() {
  const selection = getFoundSelection();
  const { provinces } = selection;
  document.getElementById("found-cap-label").textContent = FOUND_SELECTION.capital
    ? `★ ${provinces.get(FOUND_SELECTION.capital)?.name}`
    : "マップ上の空き地をクリック (未選択)";
  document.getElementById("found-cities-label").textContent =
    FOUND_SELECTION.cities.length > 0
      ? FOUND_SELECTION.cities.map((c) => `● ${provinces.get(c)?.name}`).join("、") + ` (${FOUND_SELECTION.cities.length}/2)`
      : "未選択 (0/2)";
  document.getElementById("found-provs-label").textContent =
    FOUND_SELECTION.extra.length > 0
      ? FOUND_SELECTION.extra.map((c) => provinces.get(c)?.name).join("、")
      : "なし";
  const readiness = getFoundReadiness(selection);
  document.getElementById("found-status").textContent = readiness.message;
  document.getElementById("btn-found-connect").disabled = !readiness.disconnected;
  document.getElementById("btn-found-austria-1914").hidden =
    APP_STATE.world_id !== "world_admin1" || !window.WORLD_ADMIN1_MAP?.austriaHungary1914;
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

  titleEl.textContent = `📍 ${prov.name} [${prov.region}] — 州 (State)`;

  let html = `
    <div style="display:flex;flex-direction:column;gap:8px;">
      <div><strong>領有国:</strong> ${owner ? `<span style="color:${owner.color};font-weight:700;">${owner.flag} ${owner.name}</span>` : "<span class='muted'>🏳️ 未領有（白地プロビンス）</span>"}</div>
      <div><strong>地形:</strong> <code>${prov.terrain}</code> ${prov.coastal ? "🌊沿岸プロビンス" : "⛰️内陸プロビンス"}</div>
      <div><strong>拠点ステータス・配備施設:</strong>
        ${prov.is_capital ? "<span class='badge badge-warn'>★ 首都</span> " : ""}
        ${prov.is_city ? "<span class='badge badge-ok'>● 主要都市</span> " : ""}
        ${prov.has_port ? "<span class='badge badge-ok'>⚓ 軍港設置済</span> " : ""}
        ${prov.has_radar ? "<span class='badge badge-ok'>📡 防空レーダー網</span> " : ""}
        ${prov.has_fort ? "<span class='badge badge-warn'>🏰 永久要塞線</span> " : ""}
        ${prov.has_coastal_gun ? "<span class='badge badge-warn'>🛡️ 海岸砲要塞</span> " : ""}
        ${!prov.is_capital && !prov.is_city && !prov.has_port && !prov.has_radar && !prov.has_fort && !prov.has_coastal_gun ? "通常プロビンス（施設なし）" : ""}
      </div>
      <div><strong>陸続き隣接:</strong> <span class="muted">${nbNames || "なし"}</span></div>
  `;

  // 自国領プロビンスの場合：施設の直接配備・管理（白地図配備）
  if (owner && activeNat && owner.id === activeNat.id) {
    html += `
      <div class="sub-box" style="margin-top:6px;">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
          <strong>🏗️ 施設の直接配備・管理（白地図配備）</strong>
          <span class="price-tag" style="font-size:11px;">残資金: ${formatOku(activeNat.budget)}</span>
        </div>
        <div style="display:flex;flex-direction:column;gap:5px;">
    `;
    const facDefs = CATALOG?.facilities || [];
    for (const f of facDefs) {
      const isDeployed = (prov.facilities || []).includes(f.id) ||
        (f.id === "fac_naval_port" && prov.has_port) ||
        (f.id === "fac_radar" && prov.has_radar) ||
        (f.id === "fac_fortress" && prov.has_fort) ||
        (f.id === "fac_coastal_gun" && prov.has_coastal_gun);

      const isCoastalReq = ["fac_naval_port", "fac_coastal_gun"].includes(f.id);
      const isCoastalBlocked = isCoastalReq && !prov.coastal;

      html += `
        <div style="display:flex;align-items:center;justify-content:space-between;padding:5px 7px;background:rgba(15,23,42,0.6);border-radius:4px;gap:6px;">
          <div style="flex:1;min-width:0;">
            <div style="font-size:12px;font-weight:700;color:#f8fafc;">${f.name} <span class="price-tag" style="font-size:10.5px;">(${f.cost}億)</span></div>
            <div class="muted" style="font-size:10.5px;line-height:1.3;">${f.desc}</div>
          </div>
          <div style="flex-shrink:0;">
      `;

      if (isDeployed) {
        html += `
          <button class="btn btn-xs btn-outline btn-disband-prov-fac" data-fac-id="${f.id}" title="解体して全額返金">
            🗑️ 解体(+${f.cost}億)
          </button>
        `;
      } else if (isCoastalBlocked) {
        html += `
          <button class="btn btn-xs btn-outline" disabled title="内陸プロビンスのため配備できません" style="opacity:0.45;cursor:not-allowed;">
            ⚠️ 内陸不可
          </button>
        `;
      } else {
        html += `
          <button class="btn btn-xs btn-primary btn-deploy-prov-fac" data-fac-id="${f.id}">
            💰 配備
          </button>
        `;
      }

      html += `
          </div>
        </div>
      `;
    }
    html += `
        </div>
      </div>
    `;
  }

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

  html += `</div>`;
  bodyEl.innerHTML = html;

  // 施設直接配備・解体イベント
  bodyEl.querySelectorAll(".btn-deploy-prov-fac").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const facId = btn.getAttribute("data-fac-id");
      try {
        const res = await apiPost("/api/military/procure", {
          nation_id: activeNat.id,
          domain: "facility",
          action: "buy",
          unit_id: facId,
          province_id: prov.id,
          count: 1,
        });
        APP_STATE = res.state;
        const fDef = CATALOG?.facilities?.find((x) => x.id === facId);
        showToast(`『${prov.name}』に『${fDef?.name || facId}』を配備しました！`);
        renderAll();
      } catch (err) {
        showToast(err.message, true);
      }
    });
  });

  bodyEl.querySelectorAll(".btn-disband-prov-fac").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const facId = btn.getAttribute("data-fac-id");
      try {
        const res = await apiPost("/api/military/procure", {
          nation_id: activeNat.id,
          domain: "facility",
          action: "disband",
          unit_id: facId,
          province_id: prov.id,
          count: 1,
        });
        APP_STATE = res.state;
        const fDef = CATALOG?.facilities?.find((x) => x.id === facId);
        showToast(`『${prov.name}』の『${fDef?.name || facId}』を解体し全額返金しました。`);
        renderAll();
      } catch (err) {
        showToast(err.message, true);
      }
    });
  });

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

  const rmap = window.REALISTIC_MAP_DATA || null;
  const thGeo = rmap?.theaters?.[theater.id] || null;
  const layerView = document.getElementById("select-war-layer-view").value; // both | attacker | defender

  const nationsById = {};
  for (const n of APP_STATE.nations) nationsById[n.id] = n;
  const provById = {};
  for (const p of APP_STATE.provinces) provById[p.id] = p;

  const atkSet = new Set(war.attackers || []);
  const dfnSet = new Set(war.defenders || []);

  let html = `
    <defs>
      <radialGradient id="tacOceanGrad" cx="50%" cy="55%" r="70%">
        <stop offset="0%" stop-color="#506e6a" />
        <stop offset="100%" stop-color="#293f40" />
      </radialGradient>
      <pattern id="tacGrid" width="54" height="54" patternUnits="userSpaceOnUse">
        <path d="M 54 0 L 0 0 0 54" fill="none" stroke="rgba(231,226,191,0.06)" stroke-width="0.9"/>
      </pattern>
      <filter id="tacLandShadow" x="-5%" y="-5%" width="110%" height="110%">
        <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#000000" flood-opacity="0.65" />
      </filter>
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

    <!-- 1. 海洋ベース＆戦術グリッド -->
    <rect x="0" y="0" width="1080" height="860" fill="url(#tacOceanGrad)" />
    <rect x="0" y="0" width="1080" height="860" fill="url(#tacGrid)" />
  `;

  if (thGeo) {
    // 2. 実在の大陸棚・浅瀬と陸地ベース
    if (thGeo.shelf_path) {
      html += `<path d="${thGeo.shelf_path}" fill="rgba(160,185,164,0.18)" stroke="rgba(183,200,174,0.16)" stroke-width="0.8" />`;
    }
    if (thGeo.land_path) {
      html += `<path d="${thGeo.land_path}" fill="#6f7859" filter="url(#tacLandShadow)" />`;
    }

    // 3. 戦域内プロビンスの実形状ポリゴン＆陣営支配色
    for (const tp of thGeo.provinces || []) {
      const p = provById[tp.id];
      if (!p || !tp.path) continue;
      const owner = p.owner_id ? nationsById[p.owner_id] : null;
      const baseTerrainCol = TERRAIN_COLORS[p.terrain] || "#1e293b";

      let overlayFill = owner ? owner.color : baseTerrainCol;
      let overlayOp = owner ? "0.28" : "0.15";
      let borderCol = "rgba(35,43,34,0.58)";
      let borderW = "0.9";

      if (p.owner_id && atkSet.has(p.owner_id)) {
        overlayFill = "#dc2626";
        overlayOp = "0.34";
        borderCol = "rgba(248,113,113,0.65)";
        borderW = "1.3";
      } else if (p.owner_id && dfnSet.has(p.owner_id)) {
        overlayFill = "#2563eb";
        overlayOp = "0.34";
        borderCol = "rgba(96,165,250,0.65)";
        borderW = "1.3";
      }

      html += `
        <path d="${tp.path}" fill="${baseTerrainCol}" fill-opacity="0.88" stroke="none" />
        <path d="${tp.path}" fill="${overlayFill}" fill-opacity="${overlayOp}" stroke="${borderCol}" stroke-width="${borderW}" stroke-linejoin="round" />
      `;
    }

    // 4. 湖沼・海岸線輪郭
    if (thGeo.lakes_path) {
      html += `<path d="${thGeo.lakes_path}" fill="#557b78" stroke="#9bbcb0" stroke-width="0.9" />`;
    }
    if (thGeo.land_path) {
      html += `<path d="${thGeo.land_path}" fill="none" stroke="rgba(35,48,40,0.75)" stroke-width="1.2" stroke-linejoin="round" />`;
    }

    // 5. 幹線鉄道網（参謀地図スタイル）
    for (const rline of thGeo.railways || []) {
      const rpts = rline.map((pt) => `${pt[0]},${pt[1]}`).join(" ");
      html += `
        <polyline points="${rpts}" fill="none" stroke="rgba(15,23,42,0.75)" stroke-width="2.6" />
        <polyline points="${rpts}" fill="none" stroke="rgba(203,213,225,0.45)" stroke-width="1.4" stroke-dasharray="5,5" />
      `;
    }
  }

  // 戦域タイトルヘッダーボックス
  html += `
    <g pointer-events="none">
      <rect x="14" y="12" width="680" height="52" rx="6" fill="rgba(15,23,42,0.82)" stroke="rgba(148,163,184,0.28)" stroke-width="1" />
      <text x="26" y="34" fill="#f8fafc" font-size="16" font-weight="800">🗺️ 戦時戦術作戦マップ：${theater.name}</text>
      <text x="26" y="53" fill="#94a3b8" font-size="11">${theater.description}</text>
    </g>
  `;

  // デフォルト前線ライン
  if (theater.frontline_default) {
    const fpts = theater.frontline_default.map((pt) => `${pt[0]},${pt[1]}`).join(" ");
    html += `<polyline points="${fpts}" fill="none" stroke="rgba(250,204,21,0.55)" stroke-width="3" stroke-dasharray="10,7" />`;
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
// TAB 3: 軍備編成・師団ビルダー・ショップ（火力ステータス廃止・説明文全文・マイ師団保存・残資金詳細）
// ============================================================================
function computeNationSpentBreakdown(nat) {
  if (!nat || !CATALOG) {
    return { armySpent: 0, navySpent: 0, airSpent: 0, facSpent: 0, totalSpent: 0, remaining: 0, totalAsset: 0 };
  }
  const navMap = {};
  for (const u of CATALOG.naval_units) navMap[u.id] = u;
  const airMap = {};
  for (const u of CATALOG.air_units) airMap[u.id] = u;
  const facMap = {};
  for (const f of CATALOG.facilities) facMap[f.id] = f;

  let armySpent = 0;
  for (const d of nat.divisions || []) {
    armySpent += Number(d.spec?.cost || 0) * Number(d.count || 1);
  }
  let navySpent = 0;
  for (const item of nat.naval_units || []) {
    const u = navMap[item.unit_id];
    if (u) navySpent += u.cost * Number(item.count || 0);
  }
  let airSpent = 0;
  for (const item of nat.air_units || []) {
    const u = airMap[item.unit_id];
    if (u) airSpent += u.cost * Number(item.count || 0);
  }
  let facSpent = 0;
  for (const fItem of nat.facilities || []) {
    const fid = typeof fItem === "string" ? fItem : fItem.facility_id;
    const f = facMap[fid];
    if (f) facSpent += f.cost;
  }

  armySpent = +armySpent.toFixed(1);
  navySpent = +navySpent.toFixed(1);
  airSpent = +airSpent.toFixed(1);
  facSpent = +facSpent.toFixed(1);
  const totalSpent = +(armySpent + navySpent + airSpent + facSpent).toFixed(1);
  const remaining = +Number(nat.budget || 0).toFixed(1);
  const totalAsset = +(remaining + totalSpent).toFixed(1);

  return { armySpent, navySpent, airSpent, facSpent, totalSpent, remaining, totalAsset };
}

function renderMilitaryBudgetDashboard(nat) {
  const dash = document.getElementById("military-budget-dashboard");
  if (!dash || !nat) return;
  const b = computeNationSpentBreakdown(nat);
  const weeklyBonus = Math.min(1000, Number(nat.war_prov_bonus_oku || 0));
  const weeklyTotal = Number(nat.weekly_income || 5000) + weeklyBonus;

  dash.innerHTML = `
    <div style="display:flex;align-items:center;gap:10px;">
      <span style="font-size:24px;">${nat.flag}</span>
      <div>
        <div style="font-size:15px;font-weight:800;color:#f8fafc;">${nat.name} — 国家予算・残資金・軍備使用額</div>
        <div class="muted" style="font-size:11.5px;">兵器・施設は平時いつでも解体して<strong>100%全額返金</strong>されます（配備の組み替え自由）</div>
      </div>
    </div>
    <div class="budget-metrics-row">
      <div class="budget-metric-box" style="border-color:#10b981;">
        <span class="bm-label">💰 現在の残資金（使用可能）</span>
        <span class="bm-val" style="color:#34d399;">${b.remaining.toLocaleString()}億円 <small style="font-weight:400;color:#94a3b8;">(${(b.remaining / 10000).toFixed(2)}兆)</small></span>
      </div>
      <div class="budget-metric-box">
        <span class="bm-label">📊 配備済み軍備・施設総額</span>
        <span class="bm-val" style="color:#fbbf24;">${b.totalSpent.toLocaleString()}億円 <small style="font-weight:400;color:#94a3b8;">(${(b.totalSpent / 10000).toFixed(2)}兆)</small></span>
      </div>
      <div class="budget-metric-box">
        <span class="bm-label">🪖 陸 / ⚓ 海 / ✈️ 空 / 🏰 施設 内訳</span>
        <span class="bm-val" style="font-size:12.5px;color:#e2e8f0;">
          陸 ${b.armySpent.toLocaleString()}億 / 海 ${b.navySpent.toLocaleString()}億 / 空 ${b.airSpent.toLocaleString()}億 / 施 ${b.facSpent.toLocaleString()}億
        </span>
      </div>
      <div class="budget-metric-box">
        <span class="bm-label">🏦 国家総予算規模（残＋配備） / 週収</span>
        <span class="bm-val" style="font-size:13px;color:#38bdf8;">
          計 ${(b.totalAsset / 10000).toFixed(2)}兆円 <small style="color:#fde047;">(+${weeklyTotal.toLocaleString()}億/週)</small>
        </span>
      </div>
    </div>
  `;
}

function getMergedUserTemplates() {
  const serverTpls = APP_STATE?.saved_division_templates || [];
  let localTpls = [];
  try {
    localTpls = JSON.parse(localStorage.getItem("aiwa_saved_div_templates") || "[]");
  } catch (e) {}
  const map = new Map();
  for (const t of [...serverTpls, ...localTpls]) {
    if (t && t.id) map.set(t.id, t);
  }
  return Array.from(map.values());
}

function syncUserTemplatesToLocal(tpls) {
  try {
    localStorage.setItem("aiwa_saved_div_templates", JSON.stringify(tpls || []));
  } catch (e) {}
}

function renderUserSavedTemplates() {
  const listEl = document.getElementById("user-templates-list");
  if (!listEl) return;
  const tpls = getMergedUserTemplates();
  if (tpls.length === 0) {
    listEl.innerHTML = `<div class="muted" style="font-size:11.5px;">まだ保存された「自分用の師団」はありません。下のビルダーで編成を作って『💾 現在の編成を「自分用の師団」に保存』を押すとここに登録され、いつでも1クリックで呼び出せます。</div>`;
    return;
  }

  listEl.innerHTML = "";
  for (const tpl of tpls) {
    const cost = tpl.spec?.cost ?? tpl.official_cost ?? 0;
    const breakdownText = (tpl.spec?.breakdown || []).join(" ＋ ") || tpl.desc || "";
    const item = document.createElement("div");
    item.className = "user-tpl-item";
    item.innerHTML = `
      <div style="flex:1;min-width:0;">
        <div style="font-weight:700;font-size:12.5px;color:#fde047;">⭐ ${tpl.name} <span class="price-tag">（単価 ${cost}億）</span></div>
        <div class="muted" style="font-size:11px;white-space:normal;">${breakdownText}</div>
      </div>
      <div style="display:flex;gap:5px;flex-shrink:0;">
        <button type="button" class="btn btn-xs btn-primary" data-load-utpl="${tpl.id}">📥 ビルダーに読込</button>
        <button type="button" class="btn btn-xs btn-outline" data-del-utpl="${tpl.id}">🗑️</button>
      </div>
    `;

    item.querySelector("[data-load-utpl]").addEventListener("click", () => {
      document.getElementById("div-name").value = tpl.name;
      BUILDER_REGIMENTS = (tpl.regiments || []).map((r) => ({ ...r }));
      BUILDER_ARTILLERY = tpl.artillery_id || "art_none";
      BUILDER_SUPPORTS = (tpl.supports || []).map((s) => ({ ...s }));
      BUILDER_OVERRIDE_COST = tpl.override_cost !== undefined ? tpl.override_cost : null;
      renderDivisionBuilderRows();
      renderDivisionSpecPreview();
      showToast(`⭐ 自分用の師団『${tpl.name}』を読み込みました！`);
    });

    item.querySelector("[data-del-utpl]").addEventListener("click", async () => {
      try {
        const res = await apiPost("/api/military/division", {
          action: "delete_template",
          template_id: tpl.id,
        });
        APP_STATE = res.state;
        const remain = getMergedUserTemplates().filter((x) => x.id !== tpl.id);
        syncUserTemplatesToLocal(remain);
        renderUserSavedTemplates();
        showToast(`『${tpl.name}』をマイ師団から削除しました。`);
      } catch (err) {
        showToast(err.message, true);
      }
    });

    listEl.appendChild(item);
  }
}

function renderArmyCatalogFullReference() {
  const refEl = document.getElementById("army-catalog-full-reference");
  if (!refEl || !CATALOG) return;

  let html = `<div style="font-weight:700;color:#fbbf24;margin-top:2px;">■ ① 基幹連隊（各師団に3〜4個）</div>`;
  for (const r of CATALOG.base_regiments) {
    html += `
      <div class="unit-full-desc">
        <strong>${r.name}</strong> — <span class="price-tag">${r.cost}億</span>${r.can_paradrop ? " <span class='badge badge-ok'>🪂空挺可</span>" : ""}
        <div style="margin-top:3px;">${r.desc}</div>
      </div>
    `;
  }

  html += `<div style="font-weight:700;color:#fbbf24;margin-top:8px;">■ ② 砲兵連隊（各師団に1個まで・砲兵突破連隊含む）</div>`;
  for (const a of CATALOG.artillery_regiments) {
    if (a.id === "art_none") continue;
    html += `
      <div class="unit-full-desc">
        <strong>${a.name}</strong> — <span class="price-tag">${a.cost}億</span>${a.can_paradrop ? " <span class='badge badge-ok'>🪂空挺可</span>" : ""}
        <div style="margin-top:3px;">${a.desc}</div>
      </div>
    `;
  }

  html += `<div style="font-weight:700;color:#fbbf24;margin-top:8px;">■ ③ 補助大隊（各師団に最大4個まで）</div>`;
  for (const s of CATALOG.support_battalions) {
    html += `
      <div class="unit-full-desc">
        <strong>${s.name}</strong> — <span class="price-tag">${s.cost}億</span>
        <div style="margin-top:3px;">${s.desc}</div>
      </div>
    `;
  }

  refEl.innerHTML = html;
}

function renderMilitaryTab() {
  const activeNat = getActiveNation();
  if (!activeNat) return;

  renderMilitaryBudgetDashboard(activeNat);
  renderUserSavedTemplates();
  renderArmyCatalogFullReference();

  // 施設配備プロビンスセレクト
  const facProvSel = document.getElementById("shop-facility-prov");
  if (facProvSel) {
    const prevProv = facProvSel.value;
    facProvSel.innerHTML = "";
    for (const pid of activeNat.province_ids || []) {
      const p = APP_STATE.provinces.find((x) => x.id === pid);
      if (p) {
        const selected = prevProv ? pid === prevProv : pid === activeNat.capital_id;
        const facIcons = getProvinceFacilityIcons(p).map((f) => f.icon).join("");
        const capTag = p.is_capital ? "★首都 " : p.is_city ? "●都市 " : "";
        const coastTag = p.coastal ? "🌊沿岸" : "⛰️内陸";
        facProvSel.innerHTML += `<option value="${pid}" ${selected ? "selected" : ""}>${capTag}${p.name} [${coastTag}] ${facIcons ? `(配備済:${facIcons})` : ""}</option>`;
      }
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
    row.className = "reg-card-row";

    const regSelectHtml = `
      <select data-reg-idx="${idx}" class="sel-reg-type" style="flex:1;">
        ${CATALOG.base_regiments.map((r) => `<option value="${r.id}" ${r.id === item.regiment_id ? "selected" : ""}>${r.name} (${r.cost}億)</option>`).join("")}
      </select>
    `;

    let tankSelectHtml = "";
    let unitCostNote = `${regDef.cost}億`;
    if (regDef.is_tank_unit) {
      const curTank = item.tank_id || regDef.default_tank_id || "su_t34_85";
      const tkObj = allTanks.find((t) => t.id === curTank) || allTanks[0];
      const calcCost = !item.custom_calc && (curTank === "su_t34_85" || curTank === "us_m4_76") ? regDef.cost : +(tkObj.cost * 76 + 10).toFixed(1);
      unitCostNote = `${calcCost}億`;
      tankSelectHtml = `
        <div style="margin-top:5px;">
          <label style="font-size:11px;color:#fde047;">配備戦車選択（76両×単価＋諸経費10億）:</label>
          <select data-tank-reg-idx="${idx}" class="sel-reg-tank" style="margin-top:2px;">
            ${allTanks.map((t) => `<option value="${t.id}" ${t.id === curTank ? "selected" : ""}>[${t.country}] ${t.name} （単価 ${t.cost}億/両 → 76両大隊: ${(t.cost * 76 + 10).toFixed(1)}億）</option>`).join("")}
          </select>
        </div>
      `;
    }

    row.innerHTML = `
      <div class="reg-card-top">
        <span class="badge badge-ok" style="white-space:nowrap;">連隊#${idx + 1}</span>
        ${regSelectHtml}
        <span class="price-tag">${unitCostNote}</span>
        <button type="button" class="btn btn-xs btn-outline" data-del-reg="${idx}" ${BUILDER_REGIMENTS.length <= 3 ? "disabled" : ""} title="この連隊枠を削除">✕</button>
      </div>
      ${tankSelectHtml}
      <div class="unit-full-desc">${regDef.desc}</div>
    `;
    regListEl.appendChild(row);
  });

  // ② 砲兵連隊セレクト＆全文説明文（砲兵突破連隊・自走ロケット砲兵連隊含む）
  const artSel = document.getElementById("builder-artillery");
  artSel.innerHTML = CATALOG.artillery_regiments
    .map((a) => `<option value="${a.id}" ${a.id === BUILDER_ARTILLERY ? "selected" : ""}>${a.name} (${a.cost}億)</option>`)
    .join("");
  const selectedArt = CATALOG.artillery_regiments.find((a) => a.id === BUILDER_ARTILLERY) || CATALOG.artillery_regiments[0];
  const artDescEl = document.getElementById("builder-artillery-desc");
  if (artDescEl && selectedArt) {
    artDescEl.innerHTML = `<strong>${selectedArt.name}（${selectedArt.cost}億）:</strong> ${selectedArt.desc}`;
  }

  // ③ 補助大隊リスト＆全文説明文
  const supListEl = document.getElementById("builder-supports-list");
  supListEl.innerHTML = "";
  if (BUILDER_SUPPORTS.length === 0) {
    supListEl.innerHTML = `<div class="muted" style="font-size:11.5px;padding:4px;">補助大隊なし（『＋ 補助大隊を追加』から最大4個まで追加できます）</div>`;
  }
  BUILDER_SUPPORTS.forEach((item, idx) => {
    const supDef = CATALOG.support_battalions.find((s) => s.id === item.support_id) || CATALOG.support_battalions[0];
    const row = document.createElement("div");
    row.className = "reg-card-row";

    const supSelectHtml = `
      <select data-sup-idx="${idx}" class="sel-sup-type" style="flex:1;">
        ${CATALOG.support_battalions.map((s) => `<option value="${s.id}" ${s.id === item.support_id ? "selected" : ""}>${s.name} (${s.cost}億)</option>`).join("")}
      </select>
    `;

    let tankSelectHtml = "";
    let supCostNote = `${supDef.cost}億`;
    if (supDef.is_tank_unit) {
      const curTank = item.tank_id || supDef.default_tank_id || "su_t34_85";
      const tkObj = allTanks.find((t) => t.id === curTank) || allTanks[0];
      const calcCost = !item.custom_calc && (curTank === "su_t34_85" || curTank === "us_m4_76") ? supDef.cost : +(tkObj.cost * 22).toFixed(1);
      supCostNote = `${calcCost}億`;
      tankSelectHtml = `
        <div style="margin-top:5px;">
          <label style="font-size:11px;color:#fde047;">配備戦車選択（22両×単価）:</label>
          <select data-tank-sup-idx="${idx}" class="sel-sup-tank" style="margin-top:2px;">
            ${allTanks.map((t) => `<option value="${t.id}" ${t.id === curTank ? "selected" : ""}>[${t.country}] ${t.name} （単価 ${t.cost}億/両 → 22両中隊: ${(t.cost * 22).toFixed(1)}億）</option>`).join("")}
          </select>
        </div>
      `;
    }

    row.innerHTML = `
      <div class="reg-card-top">
        <span class="badge badge-warn" style="white-space:nowrap;">補助#${idx + 1}</span>
        ${supSelectHtml}
        <span class="price-tag">${supCostNote}</span>
        <button type="button" class="btn btn-xs btn-outline" data-del-sup="${idx}" title="この補助大隊を削除">✕</button>
      </div>
      ${tankSelectHtml}
      <div class="unit-full-desc">${supDef.desc}</div>
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
      renderDivisionBuilderRows();
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
      renderDivisionBuilderRows();
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
  let minSpeed = 3;
  let canParadrop = true;
  const warnings = [];
  const breakdown = [];

  for (const item of BUILDER_REGIMENTS) {
    const r = regMap[item.regiment_id];
    if (!r) continue;
    minSpeed = Math.min(minSpeed, r.speed_tier || 1);
    if (!r.can_paradrop) canParadrop = false;
    if (r.is_tank_unit) {
      const tk = tankMap[item.tank_id || "su_t34_85"] || tankMap["su_t34_85"];
      const c = !item.custom_calc && (tk.id === "su_t34_85" || tk.id === "us_m4_76") ? r.cost : +(tk.cost * 76 + 10).toFixed(1);
      cost += c;
      breakdown.push(`${r.name}[${tk.name}×76両]: ${c}億`);
    } else {
      cost += r.cost;
      breakdown.push(`${r.name}: ${r.cost}億`);
    }
  }

  const art = artMap[BUILDER_ARTILLERY] || artMap["art_none"];
  if (art && art.id !== "art_none") {
    cost += art.cost;
    breakdown.push(`${art.name}: ${art.cost}億`);
    if ((art.max_speed_tier || 3) < minSpeed) {
      warnings.push(`⚠️ ${art.name}は機械化・機甲部隊に追従できないため機動力が低下します（自走砲兵または自走ロケット砲兵を推奨）`);
    }
    if (!art.can_paradrop) canParadrop = false;
  }

  for (const sItem of BUILDER_SUPPORTS) {
    const s = supMap[sItem.support_id];
    if (!s) continue;
    if (s.is_tank_unit) {
      const tk = tankMap[sItem.tank_id || "su_t34_85"] || tankMap["su_t34_85"];
      const c = !sItem.custom_calc && (tk.id === "su_t34_85" || tk.id === "us_m4_76") ? s.cost : +(tk.cost * 22).toFixed(1);
      cost += c;
      breakdown.push(`${s.name}[${tk.name}×22両]: ${c}億`);
    } else {
      cost += s.cost;
      breakdown.push(`${s.name}: ${s.cost}億`);
    }
  }

  const finalCost = BUILDER_OVERRIDE_COST !== null ? BUILDER_OVERRIDE_COST : +cost.toFixed(1);
  const count = Math.max(1, Number(document.getElementById("div-count")?.value || 1));
  return {
    unitCost: finalCost,
    rawCost: +cost.toFixed(1),
    totalCost: +(finalCost * count).toFixed(1),
    count,
    canParadrop,
    breakdown,
    warnings,
  };
}

function renderDivisionSpecPreview() {
  const spec = computeClientDivisionSpec();
  const activeNat = getActiveNation();
  const curBudget = Number(activeNat?.budget || 0);
  const afterBudget = +(curBudget - spec.totalCost).toFixed(1);
  const isShort = afterBudget < 0;

  const box = document.getElementById("div-preview-box");
  box.innerHTML = `
    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:6px;">
      <span><strong>1個師団単価:</strong> <span class="price-tag">${spec.unitCost.toLocaleString()}億円</span>${BUILDER_OVERRIDE_COST !== null && BUILDER_OVERRIDE_COST !== spec.rawCost ? ` <small class="muted">(公式テンプレ価格適用 / 通常合算:${spec.rawCost}億)</small>` : ""}</span>
      <span><strong>${spec.count}個師団 編成費用:</strong> <span class="price-tag" style="font-size:15px;">${spec.totalCost.toLocaleString()}億円 (${(spec.totalCost / 10000).toFixed(2)}兆円)</span></span>
    </div>
    <div style="margin-top:6px;padding:6px 8px;background:rgba(15,23,42,0.75);border-radius:6px;font-size:12px;">
      <div><strong>📋 編成内訳:</strong> ${spec.breakdown.join(" ＋ ")}</div>
      <div style="margin-top:4px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:6px;">
        <span>💰 <strong>現在残資金:</strong> ${curBudget.toLocaleString()}億円 ➔ <strong>購入後の予想残資金:</strong> <strong style="color:${isShort ? "#f87171" : "#34d399"};">${afterBudget.toLocaleString()}億円 (${(afterBudget / 10000).toFixed(2)}兆円)</strong></span>
        ${spec.canParadrop ? `<span class="badge badge-ok">🪂 全連隊が空挺降下に対応</span>` : ""}
      </div>
      ${isShort ? `<div style="color:#f87171;font-weight:700;margin-top:4px;">⚠️ 残資金が ${Math.abs(afterBudget).toLocaleString()}億円 不足しています（編成師団数を減らすか、既存兵器を解体してください）</div>` : ""}
    </div>
    ${spec.warnings.map((w) => `<div style="color:#fbbf24;font-size:11.5px;margin-top:5px;">${w}</div>`).join("")}
  `;
}

function renderProcurementShop() {
  const countrySel = document.getElementById("shop-country-filter");
  const searchVal = (document.getElementById("shop-search").value || "").trim().toLowerCase();
  const listEl = document.getElementById("shop-items-list");
  const facProvBar = document.getElementById("shop-facility-prov-bar");
  if (facProvBar) {
    facProvBar.style.display = ACTIVE_SHOP_DOMAIN === "facility" ? "block" : "none";
  }

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
    if (searchVal && !`${item.name} ${item.country || ""} ${item.category || ""} ${item.desc || ""}`.toLowerCase().includes(searchVal)) return false;
    return true;
  });

  listEl.innerHTML = "";
  const activeNat = getActiveNation();

  for (const item of filtered) {
    const row = document.createElement("div");
    row.className = "shop-item";
    let subInfo = "";
    if (ACTIVE_SHOP_DOMAIN === "navy") {
      const extra = [];
      if (item.carrier_air) extra.push(`艦載機 ${item.carrier_air}機込（空母の艦載機は値段に含まれます）`);
      if (item.transport_cap) extra.push(item.amphibious ? `1個師団を港のない沿岸へ強襲揚陸可能` : `港から港へ1個師団を海上輸送可能`);
      subInfo = `[${item.country} / ${item.category}]${extra.length ? " — " + extra.join("・") : ""}`;
    } else if (ACTIVE_SHOP_DOMAIN === "air") {
      const extra = [];
      if (item.can_carry_nuke) extra.push(`核兵器搭載可能`);
      if (item.is_nuke) extra.push(`B-29 スーパーフォートレスにのみ搭載可能（1発/月）`);
      subInfo = `[${item.country} / ${item.category}]${extra.length ? " — " + extra.join("・") : ""}`;
    } else {
      subInfo = item.desc || "";
    }

    row.innerHTML = `
      <div style="flex:1;min-width:0;">
        <div class="shop-item-title">${item.name}</div>
        <div class="shop-item-sub" style="white-space:normal;line-height:1.4;">${subInfo}</div>
      </div>
      <div style="display:flex;align-items:center;gap:6px;flex-shrink:0;">
        <span class="price-tag">${item.cost}億</span>
        ${ACTIVE_SHOP_DOMAIN !== "facility" ? `<input type="number" value="${ACTIVE_SHOP_DOMAIN === "air" && !item.is_nuke ? 10 : 1}" min="1" max="500" style="width:58px;" class="shop-qty-input" />` : ""}
        <button class="btn btn-xs btn-primary btn-buy-item">${ACTIVE_SHOP_DOMAIN === "facility" ? "選択プロビンスに配備" : "購入"}</button>
      </div>
    `;

    row.querySelector(".btn-buy-item").addEventListener("click", async () => {
      if (!activeNat) return;
      const qtyInput = row.querySelector(".shop-qty-input");
      const facProvId = document.getElementById("shop-facility-prov")?.value || activeNat.capital_id;
      if (ACTIVE_SHOP_DOMAIN === "facility") {
        const targetP = APP_STATE?.provinces?.find((p) => p.id === facProvId);
        if (["fac_naval_port", "fac_coastal_gun"].includes(item.id) && targetP && !targetP.coastal) {
          showToast(`『${item.name}』は沿岸プロビンスにのみ配備可能です（『${targetP.name}』は内陸です）。`, true);
          return;
        }
      }
      try {
        const payload = {
          nation_id: activeNat.id,
          domain: ACTIVE_SHOP_DOMAIN,
          action: "buy",
          unit_id: item.id,
          count: qty,
        };
        if (ACTIVE_SHOP_DOMAIN === "facility") {
          payload.province_id = facProvId;
        }
        const res = await apiPost("/api/military/procure", payload);
        APP_STATE = res.state;
        if (ACTIVE_SHOP_DOMAIN === "facility") {
          const provName = APP_STATE.provinces.find((p) => p.id === facProvId)?.name.split("(")[0] || facProvId;
          showToast(`${item.name} を『${provName}』に配備しました！`);
        } else {
          showToast(`${item.name} ×${qty} を調達しました！`);
        }
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

  const hasPort = (nat.facilities || []).some((x) => (typeof x === "string" ? x : x.facility_id) === "fac_naval_port");
  const navMap = {};
  for (const u of CATALOG.naval_units) navMap[u.id] = u;
  const airMap = {};
  for (const u of CATALOG.air_units) airMap[u.id] = u;
  const facMap = {};
  for (const f of CATALOG.facilities) facMap[f.id] = f;

  const b = computeNationSpentBreakdown(nat);

  banner.innerHTML = `
    <div class="sub-box" style="border-color:${hasPort ? "#10b981" : "#f59e0b"};">
      <div style="display:flex;justify-content:space-between;align-items:center;">
        <strong>${nat.flag} ${nat.name} 保有戦力・残資金サマリー</strong>
        <span class="price-tag" style="color:#34d399;">残資金: ${b.remaining.toLocaleString()}億円</span>
      </div>
      <div style="font-size:11.5px;margin-top:4px;color:#cbd5e1;">
        使用済み合計: <strong>${b.totalSpent.toLocaleString()}億円</strong> （陸軍 ${b.armySpent.toLocaleString()}億 / 海軍 ${b.navySpent.toLocaleString()}億 / 空軍 ${b.airSpent.toLocaleString()}億 / 施設 ${b.facSpent.toLocaleString()}億）
      </div>
      <div style="font-size:11.5px;margin-top:3px;">
        ⚓ 軍港(500億): ${hasPort ? "<strong style='color:#34d399;'>設置済み（海軍補給・修理有効）</strong>" : "<strong style='color:#fbbf24;'>⚠️ 未設置（海軍を運用する場合は必ず軍港を購入してください！）</strong>"}
      </div>
    </div>
  `;

  listEl.innerHTML = "";

  // 1. 施設
  for (const fItem of nat.facilities || []) {
    const fid = typeof fItem === "string" ? fItem : fItem.facility_id;
    const f = facMap[fid];
    if (!f) continue;
    const provId = typeof fItem === "object" ? fItem.province_id : nat.capital_id;
    const instId = typeof fItem === "object" ? fItem.id : "";
    const provName = APP_STATE.provinces.find((p) => p.id === provId)?.name.split("(")[0] || provId || "首都";
    const el = document.createElement("div");
    el.className = "inv-item";
    el.innerHTML = `
      <div style="flex:1;">
        <div class="shop-item-title">🏰 [施設] ${f.name} <span class="badge badge-ok">📍${provName}</span></div>
        <div class="shop-item-sub" style="white-space:normal;">${f.desc} （解体すると ${f.cost}億円 返金）</div>
      </div>
      <button class="btn btn-xs btn-outline">解体(+${f.cost}億)</button>
    `;
    el.querySelector("button").addEventListener("click", async () => {
      const res = await apiPost("/api/military/procure", {
        nation_id: nat.id,
        domain: "facility",
        action: "disband",
        unit_id: fid,
        instance_id: instId,
        province_id: provId,
        count: 1,
      });
      APP_STATE = res.state;
      showToast(`${f.name}（${provName}）を解体し全額返金しました。`);
      renderAll();
    });
    listEl.appendChild(el);
  }

  // 2. 陸軍師団（構成部隊の説明文全文表示・増減・マイ師団保存・全額返金解体）
  for (const div of nat.divisions || []) {
    const unitCost = Number(div.spec?.cost || 380);
    const refund = +(unitCost * Number(div.count || 1)).toFixed(1);
    const unitDescs = div.spec?.unit_descriptions || [];

    const el = document.createElement("div");
    el.className = "inv-item";
    el.style.flexDirection = "column";
    el.style.alignItems = "stretch";
    el.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:8px;">
        <div style="flex:1;">
          <div class="shop-item-title">🪖 ${div.name} × ${div.count}個師団</div>
          <div class="shop-item-sub" style="margin-top:2px;">1個師団単価: <strong>${unitCost}億</strong> / 小計: <strong style="color:#fbbf24;">${refund.toLocaleString()}億</strong></div>
          <div class="shop-item-sub" style="white-space:normal;margin-top:2px;color:#e2e8f0;">内訳: ${(div.spec?.breakdown || []).join(" ＋ ")}</div>
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:4px;justify-content:flex-end;">
          <button class="btn btn-xs btn-outline" data-adj-div="-1" title="1個師団削減 (+${unitCost}億返金)">-1師団</button>
          <button class="btn btn-xs btn-outline" data-adj-div="1" title="1個師団追加配備 (-${unitCost}億)">+1師団</button>
          <button class="btn btn-xs btn-outline" data-adj-div="5" title="5個師団追加配備 (-${unitCost * 5}億)">+5師団</button>
          <button class="btn btn-xs btn-amber" data-save-div-tpl="${div.id}" title="この師団を『自分用の師団』に保存">💾 マイ師団保存</button>
          <button class="btn btn-xs btn-outline" data-disband-div="${div.id}">全解体(+${refund}億)</button>
        </div>
      </div>
      ${unitDescs.length > 0 ? `
        <details style="margin-top:5px;font-size:11.5px;">
          <summary style="cursor:pointer;color:#38bdf8;">📖 この師団の各連隊・補助大隊の説明文（全文）を見る</summary>
          <div style="margin-top:4px;display:flex;flex-direction:column;gap:4px;">
            ${unitDescs.map((ud) => `<div class="unit-full-desc"><strong>[${ud.slot}] ${ud.name} (${ud.cost}億):</strong> ${ud.desc}</div>`).join("")}
          </div>
        </details>
      ` : ""}
    `;

    el.querySelectorAll("[data-adj-div]").forEach((btn) => {
      btn.addEventListener("click", async () => {
        const delta = Number(btn.getAttribute("data-adj-div"));
        try {
          const res = await apiPost("/api/military/division", {
            nation_id: nat.id,
            action: "adjust_count",
            division_id: div.id,
            delta,
          });
          APP_STATE = res.state;
          showToast(`${div.name} の師団数を ${delta > 0 ? "+" + delta : delta} 変更しました。`);
          renderAll();
        } catch (err) {
          showToast(err.message, true);
        }
      });
    });

    el.querySelector("[data-save-div-tpl]").addEventListener("click", async () => {
      try {
        const res = await apiPost("/api/military/division", {
          action: "save_template",
          nation_id: nat.id,
          name: div.name,
          regiments: div.regiments,
          artillery_id: div.artillery_id,
          supports: div.supports,
          override_cost: div.override_cost,
        });
        APP_STATE = res.state;
        syncUserTemplatesToLocal(APP_STATE.saved_division_templates);
        showToast(`⭐ 『${div.name}』を自分用の師団（マイ師団）に保存しました！`);
        renderAll();
      } catch (err) {
        showToast(err.message, true);
      }
    });

    el.querySelector("[data-disband-div]").addEventListener("click", async () => {
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
        <div class="shop-item-sub">[${u.country} / ${u.category}] 単価 ${u.cost}億 / 合計 ${refund.toLocaleString()}億</div>
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
        <div class="shop-item-sub">[${u.country} / ${u.category}] 単価 ${u.cost}億 / 合計 ${refund.toLocaleString()}億</div>
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
function loadPngWorldMap() {
  const map = window.WORLD_ADMIN1_MAP;
  if (!map) return;
  const canvas = document.getElementById("png-paint-canvas");
  const [, , width, height] = map.viewBox.split(" ").map(Number);
  canvas.width = width * 2;
  canvas.height = height * 2;
  resetPngViewport(canvas);
  pngUndoStack = [];
  pngWorldMap = {
    paths: Object.values(map.provinces)
      .filter((province) => province.path)
      .map((province) => ({ id: province.id, path: new Path2D(province.path) })),
    markers: map.island_markers || [],
    colors: new Map(),
    width,
    height,
  };
  document.getElementById("png-tolerance").disabled = true;
  document.getElementById("btn-png-europe-1914").hidden = !map.europe1914;
  drawPngWorldMap(canvas.getContext("2d"));
}

function drawPngWorldMap(ctx) {
  const { width, height, paths, markers, colors } = pngWorldMap;
  ctx.save();
  ctx.scale(ctx.canvas.width / width, ctx.canvas.height / height);
  ctx.fillStyle = "#182635";
  ctx.fillRect(0, 0, width, height);
  for (const { id, path } of paths) {
    ctx.fillStyle = colors.get(id) || "#f1f0eb";
    ctx.fill(path, "evenodd");
  }
  ctx.strokeStyle = "#64748b";
  ctx.lineWidth = 0.45;
  ctx.lineJoin = "round";
  for (const { path } of paths) ctx.stroke(path);
  ctx.strokeStyle = "#facc15";
  ctx.setLineDash([2, 2]);
  for (const marker of markers) {
    ctx.beginPath();
    ctx.arc(marker.cx, marker.cy, marker.r, 0, 2 * Math.PI);
    ctx.stroke();
  }
  ctx.restore();
}

function resetPngViewport(canvas) {
  canvas.style.width = "";
  canvas.parentElement.scrollTo(0, 0);
}

function setupPngViewport(canvas) {
  const viewport = canvas.parentElement;
  const zoomAt = (factor, clientX, clientY) => {
    const before = canvas.getBoundingClientRect();
    const zoom = (Number.parseFloat(canvas.style.width) || 100) / 100;
    const next = Math.max(1, Math.min(24, zoom * factor));
    if (next === zoom || !before.width || !before.height) return;
    const xRatio = (clientX - before.left) / before.width;
    const yRatio = (clientY - before.top) / before.height;
    canvas.style.width = `${next * 100}%`;
    const after = canvas.getBoundingClientRect();
    viewport.scrollLeft += after.left + xRatio * after.width - clientX;
    viewport.scrollTop += after.top + yRatio * after.height - clientY;
  };
  const zoomFromCenter = (factor) => {
    const rect = viewport.getBoundingClientRect();
    zoomAt(factor, rect.left + viewport.clientWidth / 2, rect.top + viewport.clientHeight / 2);
  };
  document.getElementById("btn-png-zoom-in").addEventListener("click", () => zoomFromCenter(1.5));
  document.getElementById("btn-png-zoom-out").addEventListener("click", () => zoomFromCenter(1 / 1.5));
  document.getElementById("btn-png-zoom-reset").addEventListener("click", () => resetPngViewport(canvas));
  canvas.addEventListener("wheel", (event) => {
    if (event.ctrlKey || event.metaKey || !event.deltaY) return;
    event.preventDefault();
    zoomAt(event.deltaY < 0 ? 1.25 : 1 / 1.25, event.clientX, event.clientY);
  }, { passive: false });

  let drag = null;
  let didPan = false;
  canvas.addEventListener("pointerdown", (event) => {
    if (!event.isPrimary || event.button !== 0) return;
    didPan = false;
    drag = {
      id: event.pointerId,
      x: event.clientX,
      y: event.clientY,
      left: viewport.scrollLeft,
      top: viewport.scrollTop,
    };
  });
  canvas.addEventListener("pointermove", (event) => {
    if (drag?.id !== event.pointerId || !(event.buttons & 1)) return;
    const dx = event.clientX - drag.x;
    const dy = event.clientY - drag.y;
    if (!didPan) {
      if (Math.hypot(dx, dy) < 5) return;
      didPan = true;
      canvas.setPointerCapture(event.pointerId);
      canvas.classList.add("is-panning");
    }
    viewport.scrollLeft = drag.left - dx;
    viewport.scrollTop = drag.top - dy;
  });
  const stopDragging = (event) => {
    if (drag?.id !== event.pointerId) return;
    drag = null;
    canvas.classList.remove("is-panning");
  };
  canvas.addEventListener("pointerup", stopDragging);
  canvas.addEventListener("pointercancel", stopDragging);
  canvas.addEventListener("lostpointercapture", stopDragging);
  canvas.addEventListener("click", (event) => {
    if (didPan) event.stopImmediatePropagation();
  }, true);
}

function initPngPainterCanvas() {
  const canvas = document.getElementById("png-paint-canvas");
  const ctx = canvas.getContext("2d");
  setupPngViewport(canvas);
  loadPngWorldMap();

  canvas.addEventListener("click", (e) => {
    const rect = canvas.getBoundingClientRect();
    const hexColor = document.getElementById("png-fill-color").value;
    const xRatio = (e.clientX - rect.left) / rect.width;
    const yRatio = (e.clientY - rect.top) / rect.height;
    if (pngWorldMap) {
      const { width, height, paths, markers, colors } = pngWorldMap;
      const x = xRatio * width;
      const y = yRatio * height;
      const province = paths.findLast(({ path }) => ctx.isPointInPath(path, x, y, "evenodd"));
      const marker = province ? null : markers.find((m) => Math.hypot(x - m.cx, y - m.cy) <= m.r);
      const id = (province || marker)?.id;
      if (!id || colors.get(id) === hexColor) return;
      pngUndoStack.push({ id, color: colors.get(id) });
      drawPngWorldMapAfterFill(ctx, id, hexColor);
    } else {
      const x = Math.floor(xRatio * canvas.width);
      const y = Math.floor(yRatio * canvas.height);
      const tol = Number(document.getElementById("png-tolerance").value || 32);
      pngUndoStack.push(ctx.getImageData(0, 0, canvas.width, canvas.height));
      floodFillCanvas(ctx, x, y, hexToRgb(hexColor), tol);
    }
    if (pngUndoStack.length > 15) pngUndoStack.shift();
  });
}

function drawPngWorldMapAfterFill(ctx, id, color) {
  if (color) pngWorldMap.colors.set(id, color);
  else pngWorldMap.colors.delete(id);
  drawPngWorldMap(ctx);
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
      renderPeacetimeMap();
    });
  });

  document.getElementById("chk-show-adj").addEventListener("change", renderPeacetimeMap);
  document.getElementById("chk-show-units").addEventListener("change", renderPeacetimeMap);
  document.getElementById("chk-show-terrain")?.addEventListener("change", renderPeacetimeMap);
  document.getElementById("select-peace-map-style")?.addEventListener("change", renderPeacetimeMap);
  document.getElementById("state-search").addEventListener("input", renderStateSearch);
  document.getElementById("state-region-filter").addEventListener("change", renderStateSearch);
  document.getElementById("state-search-results").addEventListener("change", (e) => {
    const p = APP_STATE.provinces.find((state) => state.id === e.target.value);
    if (!p) return;
    if (PEACE_TOOL !== "found") document.querySelector('.map-tool-btn[data-ptool="inspect"]').click();
    const rp = (window.WORLD_ADMIN1_MAP?.provinces?.[p.id] || window.REALISTIC_MAP_DATA?.provinces?.[p.id]);
    PEACE_VB.w = 600;
    PEACE_VB.h = 370;
    PEACE_VB.x = (rp?.cx ?? p.x) - PEACE_VB.w / 2;
    PEACE_VB.y = (rp?.cy ?? p.y) - PEACE_VB.h / 2;
    onPeacetimeProvinceClick(p.id);
  });

  // 平時マップ ズーム・パン
  document.getElementById("btn-peace-zoom-in").addEventListener("click", () => {
    PEACE_VB.x += PEACE_VB.w * 0.1;
    PEACE_VB.y += PEACE_VB.h * 0.1;
    PEACE_VB.w *= 0.8;
    PEACE_VB.h *= 0.8;
    renderPeacetimeMap();
  });
  document.getElementById("btn-peace-zoom-out").addEventListener("click", () => {
    PEACE_VB.x = Math.max(0, PEACE_VB.x - PEACE_VB.w * 0.125);
    PEACE_VB.y = Math.max(0, PEACE_VB.y - PEACE_VB.h * 0.125);
    PEACE_VB.w = Math.min(1600, PEACE_VB.w * 1.25);
    PEACE_VB.h = Math.min(1000, PEACE_VB.h * 1.25);
    renderPeacetimeMap();
  });
  document.getElementById("btn-peace-zoom-reset").addEventListener("click", () => {
    if (APP_STATE && (APP_STATE.world_id === "world_admin1" || APP_STATE.scenario_type === "world_admin1")) {
      PEACE_VB = { x: 0, y: 0, w: 1440, h: 720 };
    } else {
      PEACE_VB = { x: 45, y: 35, w: 1510, h: 930 };
    }
    renderPeacetimeMap();
  });

  const peaceSvg = document.getElementById("peacetime-svg");
  window.peaceDragMoved = false;

  peaceSvg.addEventListener("wheel", (e) => {
    e.preventDefault();
    const isWorld = (APP_STATE.world_id === "world_admin1" || APP_STATE.scenario_type === "world_admin1");
    const rect = peaceSvg.getBoundingClientRect();
    const factor = e.deltaY < 0 ? 0.82 : 1.22;

    if (isWorld) {
      const minW = 60;
      const maxW = 1600;
      const newW = Math.max(minW, Math.min(maxW, PEACE_VB.w * factor));
      const f = newW / PEACE_VB.w;
      const xRatio = (e.clientX - rect.left) / (rect.width || 1);
      const yRatio = (e.clientY - rect.top) / (rect.height || 1);
      PEACE_VB.x += PEACE_VB.w * xRatio * (1 - f);
      PEACE_VB.y += PEACE_VB.h * yRatio * (1 - f);
      PEACE_VB.w = newW;
      PEACE_VB.h = 720 * (newW / 1440);
      peaceSvg.setAttribute("viewBox", `${PEACE_VB.x} ${PEACE_VB.y} ${PEACE_VB.w} ${PEACE_VB.h}`);
    } else {
      const newW = Math.max(260, Math.min(1600, PEACE_VB.w * factor));
      const newH = Math.max(170, Math.min(1000, PEACE_VB.h * factor));
      PEACE_VB.x += (PEACE_VB.w - newW) * 0.5;
      PEACE_VB.y += (PEACE_VB.h - newH) * 0.5;
      PEACE_VB.w = newW;
      PEACE_VB.h = newH;
      renderPeacetimeMap();
    }
  }, { passive: false });

  peaceSvg.addEventListener("pointerdown", (e) => {
    isPeacePanning = true;
    window.peaceDragMoved = false;
    peacePanStart = { x: e.clientX, y: e.clientY, bx: PEACE_VB.x, by: PEACE_VB.y };
  });

  window.addEventListener("pointermove", (e) => {
    if (!isPeacePanning) return;
    const dx = e.clientX - peacePanStart.x;
    const dy = e.clientY - peacePanStart.y;
    if (Math.hypot(dx, dy) > 4) {
      window.peaceDragMoved = true;
    }
    if (window.peaceDragMoved) {
      const rect = peaceSvg.getBoundingClientRect();
      const rw = rect.width || 900;
      const rh = rect.height || 700;
      PEACE_VB.x = peacePanStart.bx - dx * (PEACE_VB.w / rw);
      PEACE_VB.y = peacePanStart.by - dy * (PEACE_VB.h / rh);
      peaceSvg.setAttribute("viewBox", `${PEACE_VB.x} ${PEACE_VB.y} ${PEACE_VB.w} ${PEACE_VB.h}`);
    }
  });

  window.addEventListener("pointerup", () => {
    isPeacePanning = false;
  });

  // 建国フォーム送信
  document.getElementById("btn-found-clear-sel").addEventListener("click", () => {
    FOUND_SELECTION = { capital: null, cities: [], extra: [] };
    updateFoundSelectionUI();
    renderPeacetimeMap();
  });

  document.getElementById("btn-found-austria-1914").addEventListener("click", () => {
    const preset = window.WORLD_ADMIN1_MAP.austriaHungary1914;
    const { provinces } = getFoundSelection();
    const unavailable = preset.provinces.find((id) => !provinces.has(id) || provinces.get(id).owner_id);
    if (unavailable) {
      document.getElementById("found-status").textContent =
        `「${provinces.get(unavailable)?.name || unavailable}」を選べないため、帝国領を一括選択できません。`;
      return;
    }
    const { capital, cities } = preset;
    FOUND_SELECTION = {
      capital,
      cities: [...cities],
      extra: preset.provinces.filter((id) => id !== capital && !cities.includes(id)),
    };
    const name = document.getElementById("found-name");
    if (!name.value.trim()) name.value = "オーストリア＝ハンガリー帝国";
    updateFoundSelectionUI();
    renderPeacetimeMap();
  });

  document.getElementById("btn-found-connect").addEventListener("click", () => {
    const { capital, cities, provinces, selected } = getFoundSelection();
    const connected = getFoundPaths(capital, provinces, (id) => selected.has(id));
    const disconnected = cities.filter((id) => !connected.has(id));
    const paths = getFoundPaths(capital, provinces, (id) => {
      const province = provinces.get(id);
      return province && !province.owner_id;
    });
    if (disconnected.some((id) => !paths.has(id))) {
      document.getElementById("found-status").textContent =
        "空き地だけで首都から両方の都市へつながる経路がありません。首都か都市を選び直してください。";
      return;
    }
    for (const city of disconnected) {
      for (let id = paths.get(city); id; id = paths.get(id)) {
        if (selected.has(id)) continue;
        selected.add(id);
        FOUND_SELECTION.extra.push(id);
      }
    }
    updateFoundSelectionUI();
    renderPeacetimeMap();
  });

  const foundSubmit = document.getElementById("btn-submit-found");
  foundSubmit.addEventListener("click", async () => {
    const status = document.getElementById("found-status");
    const name = document.getElementById("found-name").value.trim();
    if (!name) {
      status.textContent = "国名を入力してください。";
      document.getElementById("found-name").focus();
      return;
    }
    const readiness = getFoundReadiness(getFoundSelection());
    if (!readiness.ready) {
      status.textContent = readiness.message;
      return;
    }
    foundSubmit.disabled = true;
    try {
      const res = await apiPost("/api/nation/found", {
        name,
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
      status.textContent = err.message;
      showToast(err.message, true);
    } finally {
      foundSubmit.disabled = false;
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
    renderDivisionBuilderRows();
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

  // 自分用の師団（マイ師団テンプレート）として保存
  document.getElementById("btn-save-user-template")?.addEventListener("click", async () => {
    const activeNat = getActiveNation();
    const divName = (document.getElementById("div-name").value || "マイ師団").trim();
    try {
      const res = await apiPost("/api/military/division", {
        action: "save_template",
        nation_id: activeNat?.id || "",
        name: divName,
        regiments: BUILDER_REGIMENTS,
        artillery_id: BUILDER_ARTILLERY,
        supports: BUILDER_SUPPORTS,
        override_cost: BUILDER_OVERRIDE_COST,
      });
      APP_STATE = res.state;
      syncUserTemplatesToLocal(APP_STATE.saved_division_templates);
      showToast(`⭐ 『${divName}』を自分用の師団（マイ師団）として保存しました！`);
      renderAll();
    } catch (err) {
      showToast(err.message, true);
    }
  });

  document.getElementById("btn-buy-division").addEventListener("click", async () => {
    const activeNat = getActiveNation();
    if (!activeNat) return;
    const alsoSave = document.getElementById("chk-also-save-tpl")?.checked || false;
    try {
      const res = await apiPost("/api/military/division", {
        action: "create",
        nation_id: activeNat.id,
        name: document.getElementById("div-name").value,
        count: Number(document.getElementById("div-count").value || 1),
        regiments: BUILDER_REGIMENTS,
        artillery_id: BUILDER_ARTILLERY,
        supports: BUILDER_SUPPORTS,
        override_cost: BUILDER_OVERRIDE_COST,
        also_save_template: alsoSave,
      });
      APP_STATE = res.state;
      if (alsoSave) {
        syncUserTemplatesToLocal(APP_STATE.saved_division_templates);
      }
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
        desc: document.getElementById("ct-desc")?.value || "",
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
    for (const fItem of nat.facilities || []) {
      const fid = typeof fItem === "string" ? fItem : fItem.facility_id;
      const f = facMap[fid];
      if (!f) continue;
      const provId = typeof fItem === "object" ? fItem.province_id : nat.capital_id;
      const provName = provById[provId]?.name || provId || "首都";
      totalSpent += f.cost;
      lines.push(`- **${f.name}** [📍${provName}] （${f.cost}億）`);
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
  const selActiveWorld = document.getElementById("select-active-world");
  if (selActiveWorld) {
    selActiveWorld.value = ACTIVE_WORLD_ID;
    selActiveWorld.addEventListener("change", (e) => {
      switchWorld(e.target.value);
    });
  }

  const chkIslandMarkers = document.getElementById("chk-show-island-markers");
  if (chkIslandMarkers) {
    chkIslandMarkers.addEventListener("change", () => {
      renderPeacetimeMap();
    });
  }

  const btnResetWorld = document.getElementById("btn-reset-world");
  if (btnResetWorld) {
    btnResetWorld.addEventListener("click", async () => {
      const res = await apiPost("/api/scenario/reset", { scenario_type: "world_admin1", world_id: "world_admin1" });
      APP_STATE = res.state;
      ACTIVE_WAR_ID = null;
      document.getElementById("modal-scenario").style.display = "none";
      showToast("🌍 世界マップ（全1,527州）で初期化しました！白地プロビンスから建国してください。");
      renderAll();
    });
  }

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
  document.getElementById("btn-png-europe-1914").addEventListener("click", () => {
    if (!pngWorldMap) return;
    pngUndoStack.push({ colors: pngWorldMap.colors });
    if (pngUndoStack.length > 15) pngUndoStack.shift();
    pngWorldMap.colors = new Map([
      ...pngWorldMap.colors,
      ...Object.entries(window.WORLD_ADMIN1_MAP.europe1914),
    ]);
    const canvas = document.getElementById("png-paint-canvas");
    drawPngWorldMap(canvas.getContext("2d"));
  });

  document.getElementById("btn-png-world-map").addEventListener("click", () => {
    document.getElementById("png-file-input").value = "";
    loadPngWorldMap();
  });

  document.getElementById("png-file-input").addEventListener("change", (e) => {
    const file = e.target.files[0];
    if (!file) return;
    const img = new Image();
    const url = URL.createObjectURL(file);
    img.onload = () => {
      URL.revokeObjectURL(url);
      if (e.target.files[0] !== file) return;
      const canvas = document.getElementById("png-paint-canvas");
      canvas.width = img.width;
      canvas.height = img.height;
      resetPngViewport(canvas);
      const ctx = canvas.getContext("2d");
      ctx.drawImage(img, 0, 0);
      pngWorldMap = null;
      pngUndoStack = [];
      document.getElementById("png-tolerance").disabled = false;
      document.getElementById("btn-png-europe-1914").hidden = true;
      showToast(`📂 白地図画像 (${img.width}×${img.height}) を読み込みました！クリックでバケツ塗りできます。`);
    };
    img.onerror = () => URL.revokeObjectURL(url);
    img.src = url;
  });

  document.getElementById("btn-png-undo").addEventListener("click", () => {
    if (pngUndoStack.length === 0) return;
    const canvas = document.getElementById("png-paint-canvas");
    const ctx = canvas.getContext("2d");
    const previous = pngUndoStack.pop();
    if (pngWorldMap && previous.colors) {
      pngWorldMap.colors = previous.colors;
      drawPngWorldMap(ctx);
    } else if (pngWorldMap) drawPngWorldMapAfterFill(ctx, previous.id, previous.color);
    else ctx.putImageData(previous, 0, 0);
  });

  document.getElementById("btn-png-download").addEventListener("click", () => {
    let canvas = document.getElementById("png-paint-canvas");
    if (pngWorldMap) {
      canvas = document.createElement("canvas");
      canvas.width = pngWorldMap.width * 4;
      canvas.height = pngWorldMap.height * 4;
      drawPngWorldMap(canvas.getContext("2d"));
    }
    canvas.toBlob((blob) => {
      if (!blob) {
        showToast("PNGの保存に失敗しました。", true);
        return;
      }
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `aiwa_map_${Date.now()}.png`;
      a.click();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
    }, "image/png");
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
