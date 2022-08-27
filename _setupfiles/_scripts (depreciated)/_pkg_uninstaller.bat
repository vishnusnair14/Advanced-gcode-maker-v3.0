@echo off
:: ---------------------------------------------------------------------------------------------------
:: [Part of GCODE MAKER 3.0 Extension Pack]

:: Code by : vishnus_technologies (C)2021
:: Created on : 25-02-2022 10:30AM
:: File name : _pkg-uninstaller.bat
:: File version : 3.75.8.0
:: ---------------------------------------------------------------------------------------------------

SET execfdir="C:\Program Files\Gcode-Maker-3.0\_pkg-uninstaller.py"
SET execfdir2="_pkg-uninstaller.py"


:RUNPATH1
if exist %execfdir% (
python %execfdir%
goto :EXIT
) else (
echo path '%execfdir%' does not exists
echo searching at desktop core folder...
goto :RUNPATH2
@echo:
)

:RUNPATH2
if exist %execfdir2% (
python %execfdir2%
goto :EXIT
) else (
echo path: '%execfdir2%' does not exists!
)

:EXIT
pause