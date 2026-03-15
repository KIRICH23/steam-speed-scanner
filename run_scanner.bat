@echo off
chcp 65001 >nul 2>&1
echo Steam Download Region Speed Scanner
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed!
    echo Download Python from: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python found
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt -q
if %errorlevel% neq 0 (
    echo Failed to install dependencies
    pause
    exit /b 1
)

echo Dependencies installed
echo.
echo Starting speed test...
echo.

REM Run scanner
python steam_speed_scanner.py

echo.
pause
