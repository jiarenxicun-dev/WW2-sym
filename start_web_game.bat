@echo off
chcp 65001 > nul
cd /d "%~dp0"
echo ============================================================
echo  🌍 AIWA Web Command (欧州・地中海 国家運営＆戦術ウォーゲーム)
echo ============================================================

if exist "..\discord-antigravity-bot\.venv\Scripts\python.exe" (
    set "PY_EXE=..\discord-antigravity-bot\.venv\Scripts\python.exe"
) else (
    if not exist ".venv\Scripts\python.exe" (
        echo [初回セットアップ] Python仮想環境を作成し、必要なパッケージをインストールしています...
        python -m venv .venv
        ".venv\Scripts\python.exe" -m pip install -r requirements.txt
    )
    set "PY_EXE=.venv\Scripts\python.exe"
)

echo ブラウザで http://localhost:8085 を開いています...
start "" "http://localhost:8085"
"%PY_EXE%" -X utf8 server.py
pause
