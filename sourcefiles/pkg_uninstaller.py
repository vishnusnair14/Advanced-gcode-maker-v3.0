# [Part of GCODE MAKER 3.0 Extension Pack]

# Python intelli-package uninstaller v3.0.5.1
# [For Gcode-Maker-3.0]
# -------------------------------------------

'''
Python intelli-algorithm for uninstalling(& installing) packages installed by
GCODE-MAKER-3.0 setup or its dependent, it has several mode of uninstaller,
user can choose them of their choice. This can also able to install packages
on request, [read promt for more...]
'''

# Packages used:
# keyboard v0.13.5, pywinauto v0.6.8, pyautogui v0.9.52
# inkex v1.0.1, lxml v4.6.2, numpy v1.20.1

# Code by : vishnus_technologies (C)2022
# Created on : 24-02-2022 | 10:28PM
# File name : pkg_uninstaller.py
# File version : 3.0.5.1
# -----------------------------------------------------

# links everything together:
try:
    import sys
    import os
    import pkg_resources
    import subprocess
    import requests
    from time import sleep as sl
except ImportError as IE2:
    print(f"Import Error: {IE2}")
    input("\n( ~ press any key to exit )")
    exit()


id = '84be4d3fdf0defe6ff259579be7a243c'  # Uscript ID:
modules = ['keyboard', 'pywinauto', 'pyautogui', 'lxml', 'inkex']  #5

# pause-and-exit funct.
def PAUSE_AND_EXIT():
    input("\n( ~ press any key to exit )")
    sys.exit()

_consolemsg =f'''
-----------------------------------------------------------------------------------------------
Mode 1: IntelliMode:
--------------------
While installation, the setup will keep a trace of those packages which are installed
by the Gcode-Maker-3.0_setup.exe, so in this mode, it will ONLY DELETE THOSE PACKAGES
WHICH ARE INSTALLED BY GCODE-MAKER-3.0 during initial installation process.

Mode 2: UserMode:
-----------------
In this mode, user can input the name of packages individually, for uninstallation.
[Note: If you press 'N/n' during confirmation, you will be prompted with below options.]

[more options:]
(use below commands:)
-> [1/abort], to abort the uninstallation process & exit,
-> [2/st_ins], to abort current uninstallation and install packages individually.
-> [3/ins_allpkg], start installing all {len(modules)} main packages together.

Mode 3: NormalMode:
-------------------
This mode executes simple code, which WILL DELETE ALL THE {len(modules)} MAIN PACKAGES
mentioned/pre-defined below, if existing in your system.
: {modules} #{len(modules)}
-----------------------------------------------------------------------------------------------
'''

_infofile = f"C:/Users/{os.getenv('username')}/p_info.txt"
installed_pkg = sorted(["%s" %(i.key) for i in pkg_resources.working_set])

exit_keySet = ['exit', 'EXIT', 'Exit', 'ESC', 'Esc', 'esc', 'exit()', 'EXIT()', 'Exit()', 'ESC()', 'Esc()', 'esc()']

# class related to web based activity (helper class):
class web_activityListener:
    # function to establish active internet connection, (accessed by CLASS: UserMode:3)
    # if active IConn.{Return True} :: else{Return False}
    def chk_connection():
        try:
            request = requests.get('https://www.google.com', timeout= 3)
            return True
        except (requests.ConnectionError, requests.Timeout) as exception:
            ch = input("[MSG: No internet connection detected!\n      Connect to the internet & press ENTER]\n")
            if ch in exit_keySet:
                print("[MSG: OK, Process terminated!]")
                PAUSE_AND_EXIT()
            return web_activityListener.chk_connection()


class _uninstall_functs:
    # return 'not-installed-pkg-list' and 'installed-pkg-list'
    def sepr_pkg():
        _pkg_not_installed = []
        _pkg_to_unis = []
        for j in modules:
            if j not in installed_pkg:
                _pkg_not_installed.append(j)
            else:
                _pkg_to_unis.append(j)
        return _pkg_not_installed

    def unins_config(_modules):
        # uninstall requested package:
        def uninstall_module(_pkg_name):
            subprocess.check_output([sys.executable, "-m", "pip", "uninstall", _pkg_name, "-y"])
            print(f"[successfully uninstalled: {_pkg_name}]")
        _nof_pkg_uninsd = 0
        for i in _modules:
            if i in installed_pkg:
                uninstall_module(i)
                _nof_pkg_uninsd+=1
            else:
                print(f"[Package '{i}' not installed!]")
        return _nof_pkg_uninsd

    # show animation with print function [for 'loading', 'calculating', ects. (keywords)]
    def advAnim1(_Fcmd, _symbol, _interval, _itteration, nof_symb_prnt, Fmsg):
        for i in range(_itteration):
            for j in range(nof_symb_prnt+1):
                print(f"{_Fcmd}{_symbol*j}", end="\r")
                sl(_interval)
        if not Fmsg == None:    
            print(Fmsg)


# class contain different modes of uninstaller types:
class Uninstaller_Modes:
    # Mode 1:
    # definition for normal-mode functioning:
    def NormalMode():
        nof_pkg_unins = 0
        pkg_not_installed = _uninstall_functs.sepr_pkg()

        if len(pkg_not_installed) == len(modules):
            print("[MSG: No requested packages found for uninstallation!]")
        else:
            #_uninstall_functs.advAnim1('Attempting to uninstall packages', '.', 0.6, 3, 3, 'uninstalling packages...')
            nof_pkg_unins = _uninstall_functs.unins_config(modules)

        if nof_pkg_unins != 0:
            if nof_pkg_unins != 1:
                print(f"[MSG : {nof_pkg_unins} packages un-installed successfully]")
            elif nof_pkg_unins == 1:
                print(f"[MSG : {nof_pkg_unins} package un-installed successfully]")


    # Mode 2:
    # definition for intelli-mode functioning:
    def IntelliMode():
        nof_pkg_unins = 0
        pkg_data = []

        # fetch pre-installed package names from info-file:
        if os.path.isfile(_infofile):
            with open(_infofile, "r") as re_info:
                pkg_data = re_info.read()
            pkg_data = pkg_data.split("\n")
            while("" in pkg_data):
                pkg_data.remove("")
            #print(pkg_data)

            if len(pkg_data) != 0:
                nof_pkg_unins = _uninstall_functs.unins_config(pkg_data)
                if nof_pkg_unins != 0:
                    if nof_pkg_unins != 1:
                        print(f"\n[MSG : {nof_pkg_unins} packages un-installed successfully]")
                    elif nof_pkg_unins == 1:
                        print(f"\n[MSG : {nof_pkg_unins} package un-installed successfully]")
            else:
                print("[MSG: No packages requested for uninstallation!]")
        else:
            print(f"[Unable to locate package_info file in your system,")
            print(f"[let script delete all {len(modules)} pre-defined packages...?]\n")
            _conf = input("Do you want to continue [Y/N]?\n")
            if _conf in ['Y', 'y']:
                Uninstaller_Modes.NormalMode()
                pkg_data.clear()
            elif _conf in ['n', 'N']:
                print("[MSG: OK, process terminated!]")
            else:
                print(f"\n[MSG: Invalid option: {_conf}]")
                PAUSE_AND_EXIT()

        # clears package-info file:
        if not len(pkg_data) == 0:
            with open(_infofile, "w") as wr:
                wr.write("")
                print("[MSG: info-file cleared successfully]")


    # Mode 3:
    # definition for user-mode functioning:
    def UserMode():
        RTunins_Index = []  # runtime uninstalled package index
        RTins_Index = []  # runtime installed package index
        r = 0
        def install_unins_pkg(_pkg_name, mode, opt):
            try:
                if mode == 'install':
                    subprocess.check_output([sys.executable, "-m", "pip", mode, _pkg_name])
                    RTins_Index.append(_pkg_name)
            except subprocess.CalledProcessError as e:
                print(f"[ERROR: No package named '{_pkg_name}' found on PyPI database!]")
                print("[MSG: Process terminated!]")
                PAUSE_AND_EXIT()
            if mode == 'uninstall':
                subprocess.check_output([sys.executable, "-m", "pip", mode, _pkg_name, opt])
                RTunins_Index.append(_pkg_name)
            print(f"[MSG: successfully {mode}ed: {_pkg_name}]")

        # function for validating requested packages:
        def checkpkg(_pkg):
            if _pkg in installed_pkg:
                return True
            else:
                return False

        choice = str(input("CONFIRMATION: PROCEED WITH UNINSTALLATION [Y/N]?\n->  "))
        if choice == 'Y' or choice == 'y':
            while True:
                pkg_name = input("\nEnter the name of package, which you want to uninstall:\n[send 'esc/exit' to kill process..]\n->  ")
                if pkg_name in exit_keySet:
                    print("[MSG: OK, process terminated!]")
                    break
                if not pkg_name in RTunins_Index:
                    if checkpkg(pkg_name):
                        install_unins_pkg(pkg_name, "uninstall", "-y")
                    else:
                        print(f"[MSG: package '{pkg_name}' not installed!]")
                else:
                    print(f"[MSG: package '{pkg_name}' has already uninstalled before!]")
                '''
                loop1 = input("\nWant to uninstall more packages [Y/N]?\n->  ")
                if loop1 in ['n', 'N']:
                    print("\n[MSG: OK, process terminated!]")
                    break
                elif loop1 not in ['y', 'Y', 'n', 'N']:
                    print(f"\n[MSG: Invalid entery: {loop1}]\n[Process terminated!]")
                    break
                '''
        elif choice == 'N' or choice == 'n':
            _choice = str(input("\nChoose other commands: [1/abort, 2/st_ins, 3/ins_allpkg]?\n1. abort: To terminate uninstallation "
                                "& exit\n2. st_ins: To abort current process & start installation\n"
                                f"3. ins_allpkg: To install all main {len(modules)} packages\n->  "))
            if _choice in ['2', 'st_ins', 'ST_INS']:
                #_uninstall_functs.advAnim1('checking internet connection', '.', 0.6, 2, 3, None)
                print("\nchecking internet connection...")
                sl(1.5)
                if web_activityListener.chk_connection():
                    print("[MSG: Connection established]")
                    while True:
                        pkg_name = input("\nEnter the name of package, which you want to install:\n[send 'esc/exit' to kill process..]\n->  ")
                        if pkg_name in exit_keySet:
                            print("[MSG: OK, process terminated!]")
                            break
                        if not pkg_name in RTins_Index:
                            if not checkpkg(pkg_name):
                                print(f"Installing package: {pkg_name}")
                                install_unins_pkg(pkg_name, "install", None)
                            else:
                                print(f"[MSG: Package '{pkg_name}' already installed]")
                        else:
                            print(f"[MSG: package '{pkg_name}' has already installed before!]")                            
                        '''
                        loop = input("\nWant to install more packages [Y/N]?\n->  ")
                        if loop in ['n', 'N']:
                            print("\n[MSG: OK, process terminated!]")
                            break
                        if loop not in ['y', 'Y', 'n', 'N']:
                            print(f"\n[MSG: Invalid entery: {loop}]\n[Process terminated!]")
                            break
                        print("")
                        '''
                else:
                    if not web_activityListener.chk_connection():
                        print("[MSG: Tried all the way long, unable to stabalize internet. Try again!]")
                        PAUSE_AND_EXIT()
            elif _choice in ['1', 'ABORT', 'ABORT()', 'abort', 'abort()']:
                print("\n[MSG: Process aborted!]")
                PAUSE_AND_EXIT()
            elif _choice in ['3', 'ins_allpkg', 'INS_ALLPKG']:
                print("")
                if web_activityListener.chk_connection():
                    print("[MSG: Internet connection detected :)]")
                    for z in modules:
                        if not checkpkg(z):
                            install_unins_pkg(z, 'install', None)
                            r+=1
                    if r != 0:
                        print(f"\n[MSG: {r} package(s) installed successfully]")
                    else:
                        print(f"[MSG: All {len(modules)} main packages have already installed!]")
            else:
                print(f"\n[MSG: Invalid command: {_choice}]")
        else:
            print(f"\n[MSG: Invalid option: {choice}]")
            #run.loop_again()
            PAUSE_AND_EXIT()


# main method:
if __name__ == '__main__':
    print("Python Package Un-Installer v3.0.5.1")
    print("[For Gcode-Maker-3.0]")
    print("------------------------------------")
    _preconf = str(input(f"CONFIRMATION:\nContinue with uninstalling all below {len(modules)} packages: [Y/N]?\n{modules}\n->  "))
    if _preconf == 'y' or _preconf == 'Y':
        Uninstaller_Modes.NormalMode()
    elif _preconf == 'n' or _preconf == 'N':
        print(_consolemsg)
        _inp = str(input("Choose your mode: [1/2/3]?\n1: Intelli Mode\n2: User Mode\n3: Normal Mode\n->  "))
        if _inp == '1':
            print("\n[Mode: Intelli-Mode]")
            Uninstaller_Modes.IntelliMode()
        elif _inp == '2':
            print("\n[Mode: User-Mode]")
            Uninstaller_Modes.UserMode()
        elif _inp == '3':
            print("\n[Mode: Normal-Mode]")
            Uninstaller_Modes.NormalMode()
        elif '0' in _inp:
            import winsound as ws
            ws.Beep(3900,850) #[frequency(hz), time(ms)]
            PAUSE_AND_EXIT()
        else:
            print(f"\n[MSG: Invalid choice: {_inp}]")
            PAUSE_AND_EXIT()
    else:
        print(f"\n[MSG: Invalid option: {_preconf}]")
        PAUSE_AND_EXIT()

    # pause on exit
    PAUSE_AND_EXIT()