@echo off
:: [Part of GCODE MAKER 3.0 Extension Pack]

:: -------------------------------------------------
:: Start-Engine batch script for pkg_uninstaller.py

:: Code by : vishnus_technologies (C)2022
:: Created on : 10-03-2022 | 09:17PM
:: File name : pkg_uninstaller.bat
:: File version : 3.75.7.1
:: -------------------------------------------------

SET execfdir="C:\Program Files\Gcode-Maker-3.0\pkg_uninstaller.py"
SET execfdir2="C:\Users\%username%\Desktop\GcodeMakerUserFile_V3\sourcefiles\pkg_uninstaller.py"

:: Un-comment below lines [~18-28], to prompt for choice.
:::Prompt CONFIRMATION
::echo Please select the src source:
::echo 1. run from C:/Program Files
::echo 2. run from src-desktop folder
::SET /p inp=
::if %inp%==1 (
::goto :EXEC1
::) else if %inp% == 2 (
::goto :EXEC2
::) else (
::goto :EXEC1
::)

:EXEC1
echo [searching at C:/...]
if exist %execfdir% (
echo [MSG: File found]
@echo:
python -u %execfdir%
goto :EXIT
) else (
echo [ERROR: File at {%execfdir%} does not exists!]
@echo:
goto :EXEC2
@echo:
)

:EXEC2
echo [searching at desktop source folder...]
if exist %execfdir2% (
echo [MSG: File found]
@echo:
python -u %execfdir2%
goto :EXIT
) else (
echo path: [ERROR: File at {%execfdir2%} does not exists!, Try again :(]
)

:EXIT