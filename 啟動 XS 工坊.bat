@echo off
chcp 65001 >nul
cd /d "%~dp0"
title XS 工坊 XS Studio

echo ============================================================
echo   XS 工坊 XS Studio
echo   啟動中，稍候會自動開啟瀏覽器…
echo.
echo   ※ 保持此視窗開啟＝運行中；關掉這個視窗就結束。
echo ============================================================
echo.

REM 找 python：優先用 py 啟動器，再退回 PATH 上的 python
set "PY="
where py >nul 2>&1 && set "PY=py -3"
if not defined PY ( where python >nul 2>&1 && set "PY=python" )

if not defined PY (
    echo [錯誤] 這台電腦找不到 Python。
    echo.
    echo   請到 https://www.python.org/downloads/ 下載安裝，
    echo   安裝時務必勾選「Add Python to PATH」，裝完再跑一次本程式。
    echo.
    pause
    exit /b 1
)

REM 首次啟動補裝相依套件（已裝過就跳過，不會每次都連網）
%PY% -c "import flask, requests" >nul 2>&1
if errorlevel 1 (
    echo [首次啟動] 安裝必要套件中，這需要一到兩分鐘…
    %PY% -m pip install --disable-pip-version-check -q -r requirements.txt
    if errorlevel 1 (
        echo.
        echo [錯誤] 套件安裝失敗，請確認網路連線後再試一次。
        pause
        exit /b 1
    )
    echo [完成] 套件安裝好了。
    echo.
)

%PY% app.py

echo.
echo XS 工坊已結束。按任意鍵關閉視窗。
pause >nul
