@echo off
:: ---------------------------------------------------------------------------------------------------
:: [Part of GCODE MAKER 3.0 Extension Pack]

:: Start-Engine script for python package uninstaller. [For: 'UnIns_pypacks.py'].
:: This script starts executing after the successfull installation of GCODE-MAKER-3.0 Extension Pack.

:: Code by : vishnus_technologies (C)2022
:: Created on : 29-08-2021 03:52PM
:: File name : UnIns_pkg.bat
:: File version : 3.75.8.0
:: ---------------------------------------------------------------------------------------------------

SET execfdir="C:\Program Files\Gcode-Maker-3.0\UnIns_pkg.py"

:EXECSCRIPT
if not exist %execfdir% (
echo Python Package UnInstaller v3.0.5.1
echo [For Gcode-Maker-3.0]
echo ---------------------------------
@echo:
echo [MSG: Uninstaller core-file is missing on your system] 
@echo:
echo ----------------------------------------------
echo Missing File Name : UnIns_pkg.py
echo Location : C:/Program Files/Gcode-Maker-3.0
echo Download file from : vishnus_technologies.in 
echo ----------------------------------------------
goto :SEARCH_OTHER_LOC
)
if exist %execfdir% (
python %execfdir%
goto :END
)

:SEARCH_OTHER_LOC
echo Want to search in any other location [Y/N]
SET /p inp=
@echo:
if %inp%==y (
goto :PLAN_B 
) else (
goto :END
)

:PLAN_B
echo Enter full path to the file
SET /p loc=
if exist %loc% (
python %loc%
goto :END
)
if not exist %loc% (
echo path '%loc%' does not exists!
goto :END0
)

:END0
@echo:
echo (press any key to terminate)
SET /p abc=

:END
@echo:
exit