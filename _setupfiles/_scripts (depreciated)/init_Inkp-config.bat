@echo off
echo Extension Configuration Script v3.20.1.0
echo [For Gcode-Maker-3.0]
echo ----------------------------------------
@echo:
:: ------------------------------------------------------------------------------------------------------
:: [Part of GCODE MAKER 3.0 Extension Pack]

:: Python Start-Engine script for Gcode-Maker-3.0 pre-configuration process. [For: 'Inkp_config.py'].
:: This script starts executing after the successfull installation of GCODE-MAKER-3.0 Extension Pack.
:: [Only if |✔|'Run Extension Configuration Script' option is selected before finishing the setup.exe]

:: Code by : vishnus_technologies (C)2021
:: Created on : 01-09-2021 03:27PM
:: File name : init_Inkp-config.bat
:: File version : 3.9.0.1
:: ------------------------------------------------------------------------------------------------------

SET dir="C:\Program Files\Gcode-Maker-3.0\Inkp_config.py"
SET pydir39="C:\Users\%username%\AppData\Local\Programs\Python\Python310\python.exe"
SET pydir310="C:\Users\%username%\AppData\Local\Programs\Python\Python310\python.exe"

:DEFAULTSTART
if exist %pydir39% (
echo [MSG: Python interpreter found]
goto :EXECSCRIPT
) 
if not exist %pydir39% (
if not exist %pydir310% (
echo [MSG: No python interpreters found on system!]
@echo:
)
)

:SET-USR-PYDIR
SET pydir39="C:\Users\%username%\AppData\Local\Programs\Python\Python39\python.exe"
SET pydir310="C:\Users\%username%\AppData\Local\Programs\Python\Python310\python.exe"
echo Enter user python interpreter location:
SET /p usrpydir= 
echo You have entered : "%usrpydir%"
if exist %usrpydir% ( 
echo [MSG: User python interpreter validated]
@echo:
goto :EXECSCRIPT1
) 
if not exist %usrpydir% ( 
color 04
echo [MSG: You have entered an INVALID python interpreter path!] 
echo [MSG: Retrying with standard path configuration...]
color 06
@echo:
goto :DEFAULTSTART
)


:EXECSCRIPT
if exist %dir% (
echo [MSG: Inkp_config.py file found]
echo [Inkp_config.py [with standard-py-path]]
@echo:
echo ----------------------------------------------------
%pydir39% %dir%
color 02
goto :END
) 
if not exist %dir% ( 
color 04
echo ----------------------------------------------------------------------------------------------
echo ERROR : [Extension configuration script is missing at, 'C:\Program Files\Gcode-Maker-3.0\']
echo Missing File Name : Inkp_config.py
echo Error Type : File missing [ERR-Code : 404]
echo Download this file from : [www.vishnus_technologies.in]
@echo:
echo [Copy the missing file (Inkp_config.py)  the folder, 
echo  Run this script (init_Inkp-config.bat) again from: 'C:\Program Files\Gcode-Maker-3.0\']
echo ----------------------------------------------------------------------------------------------
@echo:
goto :END0 )



:EXECSCRIPT1
if exist %dir% (
echo ----------------------------------------------------
%usrpydir% %dir%
echo [Inkp_config.py [with user-py-path]]
color 02
goto :END
)
if not exist %dir% (
color 04
echo ----------------------------------------------------------------------------------------------
echo ERROR : [Extension configuration script is missing at, 'C:\Program Files\Gcode-Maker-3.0\']
echo Missing File Name : Inkp_config.py
echo Error Type : File missing [ERR-Code : 404]
echo Download this file from : [www.vishnus_technologies.in]
echo [Copy the missing file in the folder, 
echo  Run this script (init_Inkp-config.bat) again from: 'C:\Program Files\Gcode-Maker-3.0\']
echo ----------------------------------------------------------------------------------------------
@echo:
goto :END0
)


:END0
pause

:END
exit
