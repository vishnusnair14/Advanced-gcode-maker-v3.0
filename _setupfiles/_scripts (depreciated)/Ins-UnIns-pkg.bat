:: [Part of GCODE-MAKER-3.0 Extension Pack]

@echo off
ECHO Python-Module Installer/Uninstaller v2.1.45.8
ECHO [vishnus_technologies (C) 2021]
ECHO ---------------------------------------------
@echo:

:: -----------------------------------------------------------------------------
:: [THIS IS A SUB BATCH FILE ASSOCIATED WITH GCODE-MAKER-2.0 EXTENSION PACK]

:: Script for installing/uninstalling python-modules 

:: Code by : vishnus_technologies (C)2021
:: Created on : 08-06-2021 01:42PM
:: File name : Ins-Unins-pkg.bat
:: File version : 2.1.45.8
:: ----------------------------------------------------------------------------

ECHO -----------------------------------------------------------
ECHO Checking connection, please wait...
ECHO -----------------------------------
PING -n 3 www.google.com |find "Reply from " >NUL
IF NOT ERRORLEVEL 1 goto :SUCCESS-1A
IF     ERRORLEVEL 1 goto :TRYAGAIN-1A

:TRYAGAIN-1A
color 06
ECHO STATUS : FAILED!
:TRYAGAIN-2A
color 06
@echo:
ECHO Retrying a bit more, please wait...
@echo off
PING -n 3 www.google.com|find "Reply from " >NUL
IF NOT ERRORLEVEL 1 goto :SUCCESS-2A
IF     ERRORLEVEL 1 goto :TRYIP

:TRYIP
ECHO STATUS : FAILED!
@echo:
ECHO Checking DNS...
ECHO Trying to connect by IP address...
@echo off
ping -n 3 192.168.43.12|find "Reply from " >NUL
IF NOT ERRORLEVEL 1 goto :SUCCESSDNS
IF     ERRORLEVEL 1 goto :TRYROUTER

:TRYROUTER
ECHO STATUS : FAILED!
@echo:
ECHO Lets try pinging the router....
ping -n 3 192.168.1.1|find "Reply from " >NUL
IF NOT ERRORLEVEL 1 goto :ROUTERSUCCESS
IF     ERRORLEVEL 1 goto :NETDOWN

:ROUTERSUCCESS
ECHO It appears that you can reach the router, but internet is unreachable.
goto :FAILURE

:NETDOWN
ECHO STATUS : FAILED!
ECHO It appears that you are having network issues, the router cannot be reached.
goto :FAILURE

:SUCCESSDNS
ECHO It appears that you are having DNS issues.
ECHO STATUS : FAILED!
goto :FAILURE

:SUCCESS-1A
color 02
ECHO [SUMMARY]
ECHO [You have an active Internet connection.] 
ECHO STATUS : SUCCESS [Connection Detected]
ECHO CHECK  : PASSED
ECHO MSG : Redirecting to python module configuration window...
ECHO -----------------------------------------------------------
timeout /t 2 /nobreak >NUL
goto :DEFAULTSTART

:SUCCESS-2A
color 02
ECHO --------------------------------------------------------------------------
ECHO You have an active internet connection but some packet loss was detected !
ECHO Redirecting to python module configuration window...
ECHO --------------------------------------------------------------------------
timeout /t 2 /nobreak >NUL
goto :DEFAULTSTART

:FAILURE
@echo:
color 04
ECHO ------------------------------------------------------------------------------------------
ECHO You do not have an active Internet connection !
ECHO STATUS : FAILED [No Connection Detected]
ECHO Unable to start python module installation window, connect to the internet and try again !
ECHO ------------------------------------------------------------------------------------------
pause
color 06
goto :TRYAGAIN-2A

::-------------------------------------------------------------------------------------------------------------

:DEFAULTSTART
@echo:
color 07
@echo:

:RET-MAIN-WIN
ECHO **************************************
ECHO --------------------------------------
ECHO * MAIN WINDOW                        
ECHO # Choose your options to continue:- 
ECHO   Press 1 to start Installer window, 
ECHO   Press 2 to start Uninstaller window.
ECHO --------------------------------------
ECHO **************************************
SET /p usrch=

if %usrch%==1 (
goto :PYMODL-INS-CONFG
) else if %usrch%==2 (
goto :PYMODL-UNINS-CONFG 
) else (
goto :EXIT2
)

:PYMODL-INS-CONFG
@echo:
ECHO ------------------------------------
ECHO Checking installer configurations...
timeout /t 1 >NUL 
ECHO STATUS : SUCCESS [check passed]
ECHO ------------------------------------
@echo:
timeout /t 1 >NUL
ECHO Welcome to python module installer 
ECHO -----------------------------------

:PYMODL-INS-AGAIN
ECHO Enter name of Python Module you want to INSTALL:
SET /p ins-m-nam=
SET sdir=cd C:/Users/%username%/AppData/Local/Programs/Python/Python39/Scripts
::SET inscmd=pip install --no-deps -U "%ins-m-nam%"
SET inscmd=pip install "%ins-m-nam%"
ECHO Starting Installer...
%sdir%
%inscmd%
@echo:
ECHO -----------------------------------------
ECHO # Choose an option:-
ECHO   Press 0 for installing more modules ?
ECHO   Press 1 to start uninstallation window,
ECHO   Press 2 to exit,
ECHO -----------------------------------------
SET /p incont=
if %incont%==0 (
@echo:
goto :PYMODL-INS-AGAIN
) else if %incont%==1 (
goto :PYMODL-UNINS-CONFG
) else if %incont%==2 (
goto :EXIT1
) else ( 
goto :EXIT2
)

::--------------------------------------------------------------------------------------------------

:PYMODL-UNINS-CONFG
@echo:
ECHO --------------------------------------
ECHO Checking uninstaller configurations...
timeout /t 2 >NUL
ECHO STATUS : SUCCESS [check passed]
ECHO --------------------------------------
@echo:
timeout /t 1 >NUL
ECHO Welcome to python module uninstaller 
ECHO -------------------------------------

:PYMODL-UNINS-AGAIN
ECHO Enter name of Python Module you want to UNINSTALL:
SET /p unins-m-nam=
SET sdir1=cd C:/Users/%username%/AppData/Local/Programs/Python/Python39/Scripts
SET uninscmd=pip3 uninstall "%unins-m-nam%" -y
ECHO Starting uninstaller...
%sdir1%
%uninscmd%
@echo:
ECHO -----------------------------------------
ECHO # Choose an option:-
ECHO   Press 0 for uninstalling more modules ?
ECHO   Press 1 to start installation window
ECHO   Press 2 to exit,
ECHO -----------------------------------------
SET /p uncont=
if %uncont%==0 (
@echo:
goto :PYMODL-UNINS-AGAIN
) else if %uncont%==1 (
@echo:
goto :CHK-CONN-FORINS
) else if %uncont%==2 (
goto :EXIT1
) else (
goto :EXIT2
)


:CHK-CONN-FORINS
ECHO Checking connection, please wait...
PING -n 3 meet.google.com|find "Reply from " >NUL
IF NOT ERRORLEVEL 1 goto :SUCCESS-1B
IF     ERRORLEVEL 1 goto :TRYAGAIN-1B

:TRYAGAIN-1B
color 06
ECHO STATUS : FAILED!
:TRYAGAIN-2B
color 06
@echo:
ECHO Retrying a bit more, please wait...
@echo off
PING -n 4 meet.google.com|find "Reply from " >NUL
IF NOT ERRORLEVEL 1 goto :SUCCESS-2B
IF     ERRORLEVEL 1 goto :TRYIP2

:TRYIP2
ECHO STATUS : FAILED!
@echo:
ECHO Checking DNS...
ECHO Trying to connect by IP address...
@echo off
ping -n 3 216.239.37.99|find "Reply from " >NUL
IF NOT ERRORLEVEL 1 goto :SUCCESSDNS2
IF     ERRORLEVEL 1 goto :FAILURE2

:SUCCESSDNS2
color 04
ECHO It appears that you are having DNS issues.
ECHO STATUS : FAILED!
goto :FAILURE2

:SUCCESS-1B
color 02
ECHO ----------------------------------------------------
ECHO You have an active Internet connection. 
ECHO STATUS : SUCCESS [Connection Detected]
ECHO CHECK  : PASSED
ECHO Redirecting to python module Installation window...
ECHO ----------------------------------------------------
timeout /t 2 /nobreak >NUL
@echo:
goto :PYMODL-INS-AGAIN

:SUCCESS-2B
color 02
ECHO --------------------------------------------------------------------------
ECHO You have an active internet connection but some packet loss was detected !
ECHO Redirecting to python module configuration window...
ECHO --------------------------------------------------------------------------
@echo:
@echo:
timeout /t 2 /nobreak >NUL
goto :PYMODL-INS-AGAIN

:FAILURE2
@echo:
color 04
ECHO ------------------------------------------------------------------------------------------
ECHO You do not have an active Internet connection !
ECHO STATUS : FAILED [No Connection Detected]
ECHO Unable to start python module installation window, connect to the internet and try again !
ECHO ------------------------------------------------------------------------------------------
pause
color 06
goto :TRYAGAIN-2B

:EXIT1 
:: exit entry if {by program}
:: JSON def^ {IF %ranprp_12% ( :call :: EXIT1/EXIT2) end}
@echo:
ECHO exiting... [user requested]
ECHO exit status : 0
timeout /t 3 /nobreak >NUL
goto :EXIT0

:EXIT2 
:: exit entry if {error any}
@echo:
ECHO exiting... [Invalid Entry !]
ECHO exit status : 1
timeout /t 3 /nobreak >NUL

:EXIT0
pause


