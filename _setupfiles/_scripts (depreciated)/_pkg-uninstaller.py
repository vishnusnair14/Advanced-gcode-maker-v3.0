# [Part of GCODE MAKER 3.0 Extension Pack]

# Python package uninstaller v3.0.5.1 [For Gcode-Maker-3.0]
# ---------------------------------------------------------

'''
Python intelligent algorithm for uninstalling packages installed by
GCODE-MAKER-3.0 setup or its dependent, it has several mode of uninstaller, 
user can choose them of their choice. This can also able to install 
pacakges on request, read promt for more...
'''

# Packages :
# keyboard v0.13.5, pywinauto v0.6.8, pyautogui v0.9.52
# inkex v1.0.1, lxml v4.6.2, numpy v1.20.1

# Code by : vishnus_technologies (C)2022
# Created on : 24-02-2022 10:28PM
# File name : _pkg-uninstaller.py
# File version : 3.0.5.1
# -----------------------------------------------------

import sys
import getpass as gp
import pkg_resources
import subprocess
import os
import winsound as ws
import requests

id = '84be4d3fdf0defe6ff259579be7a243c'
modules = ['keyboard', 'pywinauto', 'pyautogui', 'lxml', 'inkex']  #5

msg =f''' 
---------------------------------------------------------------------------------------------
Mode 1: NormalMode:
-------------------
This mode executes simple code, which WILL DELETE ALL THE MAIN SIX PACKAGE
mentioned/pre-defined below, if existing in your system.
[keyboard, pywinauto, pyautogui, lxml, inkex] #{len(modules)}

Mode 2: IntelliMode:
--------------------
While installation, the setup will keep a trace of those packages which are installed 
by the Gcode-Maker-3.0 setup. So this mode will ONLY DELETE THOSE PACKAGES WHICH ARE
INSTALLED BY GCODE-MAKER-3.0 during initial installation process.

Mode 3: UserMode:
-----------------
In this mode, user can input the name of pacakge, for uninstallation. 
[Note: If you press 'N/n' during confirmation, you will be prompted with below options.]

[more options:]
-> use command: [1/abort], to abort the uninstallation process & exit, 
-> use command: [2/st_ins], to abort the current uninstallation process and start installation.
---------------------------------------------------------------------------------------------
'''

#print(os.path.expanduser('~'))
pkg_dir = "C:/Users/"+gp.getuser()+"/p_info.txt"

installed_pkg = sorted(["%s" %(i.key) for i in pkg_resources.working_set])

# class related to web based activity (helper class):
class web_activityListener:
    # function to establish internet connection, (accessed by CLASS: UserMode:3)
    def chk_connection():
        try:
            request = requests.get('https://www.google.com', timeout= 3)
            return True
        except (requests.ConnectionError, requests.Timeout) as exception:
            ch = input("[MSG: No internet connection detected!\n      Connect to the internet & press ENTER :(]\n")
            if ch in ['exit', 'EXIT', 'EXIT()', 'exit()']:
                print("[MSG: Process terminated!]")
                exit()
            return web_activityListener.chk_connection()


class _uninstall_functs:
    # Function for uninstalling requested modules:
    def uninstall_module(_pkg_name):
        subprocess.check_output([sys.executable, "-m", "pip", "uninstall", _pkg_name, "-y"])
        print(f"[successfully uninstalled: {_pkg_name}]")
            
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
        _nof_pkg_unins = 0
        for i in _modules:
            if i in installed_pkg:
                _uninstall_functs.uninstall_module(i)
                _nof_pkg_unins+=1
            else:
                print(f"Package '{i}' not installed!")
        return _nof_pkg_unins


class Uninstaller_Mode:
    # Mode 1:
    # definition for normal-mode functioning:
    def NormalMode():
        nof_pkg_unins = 0
        pkg_not_installed = _uninstall_functs.sepr_pkg()
        
        if len(pkg_not_installed) == len(modules):
            print("[MSG: No requested packages found for uninstallation!]")
        else:
            nof_pkg_unins = _uninstall_functs.unins_config(modules)

        if nof_pkg_unins != 0:
            if nof_pkg_unins != 1:
                print(f"\nMSG : {nof_pkg_unins} packages un-installed successfully")
            elif nof_pkg_unins == 1:
                print(f"\nMSG : {nof_pkg_unins} package un-installed successfully")


    # Mode 2:
    # definition for intelli-mode functioning:
    def IntelliMode():
        nof_pkg_unins = 0
        data = []
    
        if os.path.isfile(pkg_dir):        
            with open(pkg_dir, "r") as re_info:
                data = re_info.read()
            data = data.split("\n")
            while("" in data):
                data.remove("")
            #print(data)
            
            if len(data) != 0:
                nof_pkg_unins = _uninstall_functs.unins_config(data)
                if nof_pkg_unins != 0:
                    if nof_pkg_unins != 1:
                        print(f"\n[MSG : {nof_pkg_unins} packages un-installed successfully]")
                    elif nof_pkg_unins == 1:
                        print(f"\n[MSG : {nof_pkg_unins} package un-installed successfully]")
            else:
                print("[MSG: No packages requested for uninstallation!]")
        else:
            print(f"[Unable to locate package_info file in your system,")
            print(f"[This script will delete all main {len(modules)} pre-defined packages.]\n")
            _conf = input("Do you want to continue [Y/N]?\n")
            if _conf in ['Y', 'y']:
                Uninstaller_Mode.NormalMode()
                data.clear()
            elif _conf in ['n', 'N']:
                print("[MSG: OK, process terminated]")
            else:
                print(f"\n[MSG: Invalid option: {_conf}]")
                sys.exit()
                
        if not len(data) == 0:
            with open(pkg_dir, "w") as wr:
                wr.write("")

    
    # Mode 3:
    # definition for user-mode functioning:
    def UserMode():
        def install_unins_pkg(_pkg_name, mode, opt):
            try:
                if mode == 'install':
                    subprocess.check_output([sys.executable, "-m", "pip", mode, _pkg_name])
            except subprocess.CalledProcessError as e:
                print(f"[ERROR: No package named '{_pkg_name}' found on PyPI database!]")
                print("[MSG: Process terminated!]")
                sys.exit()
            if mode == 'uninstall':
                subprocess.check_output([sys.executable, "-m", "pip", mode, _pkg_name, opt])
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
                pkg_name = input("\nEnter the name of package, which you want to uninstall:\n")
                if checkpkg(pkg_name):
                    install_unins_pkg(pkg_name, "uninstall", "-y")
                else:
                    print(f"[MSG: package '{pkg_name}' not installed!]")
                loop1 = input("\nWant to uninstall more packages [Y/N]?\n->  ")
                if loop1 in ['n', 'N']:
                    print("\n[MSG: OK, process terminated!]")
                    break
                elif loop1 not in ['y', 'Y', 'n', 'N']:
                    print(f"\n[MSG: Invalid entery: {loop1}]\n[Process terminated!]")
                    break       
        elif choice == 'N' or choice == 'n':
            _choice = str(input("\nChoose other commands: [1/abort, 2/st_ins]?\n1. abort: To terminate uninstallation "
                            "& exit\n2. st_ins: To abort current process & start installation\n->  "))
            if _choice in ['st_ins', 'ST_INS', '2']:
                if web_activityListener.chk_connection():
                    print("[MSG: Connection established]\n")
                    while True:
                        pkg_name = input("Enter the name of package, which you want to install:\n")
                        if not checkpkg(pkg_name):
                            print("Installing package...")
                            install_unins_pkg(pkg_name, "install", None)
                        else:
                            print(f"[MSG: Package '{pkg_name}' already installed]")
                        installed_pkg.clear()
                        loop = input("\nWant to install more packages [Y/N]?\n->  ")
                        if loop in ['n', 'N']:
                            print("\n[MSG: OK, process terminated!]")
                            break
                        if loop not in ['y', 'Y', 'n', 'N']:
                            print(f"\n[MSG: Invalid entery: {loop}]\n[Process terminated!]")
                            break
                        print("")
                else:
                    web_activityListener.chk_connection()
            elif _choice in ['abort', 'ABORT', '1', 'abort()']:
                print("\n[MSG: Process aborted!]")
                sys.exit()
            else:
                print(f"\n[MSG: Invalid command: {_choice}]")
        else:
            print(f"\n[MSG: Invalid option: {choice}]")
            #run.loop_again()
            sys.exit()


# main method:
if __name__ == '__main__':
    print("Python Package UnInstaller v3.0.5.1")
    print("[For Gcode-Maker-3.0]")
    print("-----------------------------------")
    print(msg)
    _inp = input("Enter your choice: [1/2/3]?\n1: Normal Mode\n2: Intelli Mode\n3: User Mode\n->  ")
    if _inp == '1':
        print("\n[Mode: Normal-Mode]")
        Uninstaller_Mode.NormalMode()
    elif _inp == '2':
        print("\n[Mode: Intelli-Mode]") 
        Uninstaller_Mode.IntelliMode()
    elif _inp == '3':
        print("\n[Mode: User-Mode]")
        Uninstaller_Mode.UserMode()
    elif _inp == '0':
        ws.Beep(3900,850)
        sys.exit()
    else:
        print(f"\n[MSG: Invalid choice: {_inp}]")
        sys.exit()
        
    #input("\n(press any key to exit)")