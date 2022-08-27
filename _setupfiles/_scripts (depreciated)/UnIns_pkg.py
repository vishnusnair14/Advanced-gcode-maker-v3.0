# [Part of GCODE MAKER 3.0 Extension Pack]

# Python package uninstaller v3.0.5.1 [For Gcode-Maker-3.0]
# ---------------------------------------------------------

'''
Python code for uninstalling packages depended by extension,
installed by extension setup of Gcode-Maker-3.0
Note: This script will uninstall all the six packages
'''

# Packages :
# keyboard v0.13.5, pywinauto v0.6.8, pyautogui v0.9.52
# inkex v1.0.1, lxml v4.6.2, numpy v1.20.1

# Code by : vishnus_technologies (C)2022
# Created on : 24-02-2022 10:28PM
# File name : UnIns_pkg.py
# File version : 3.0.5.1
# -----------------------------------------------------

import sys
import getpass as gp
import pkg_resources
import subprocess
import os
import winsound as ws
import requests

msg =''' 
---------------------------------------------------------------------------------------------
Mode 1: NormalMode:
-------------------
This mode executes simple code, which WILL DELETE ALL THE MAIN SIX PACKAGE
mentioned/pre-defined below, if existing in your system.
[keyboard, pywinauto, pyautogui, lxml, inkex, numpy] #6

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

id = '84be4d3fdf0defe6ff259579be7a243c'

modules = ['keyboard', 'pywinauto', 'pyautogui', 'lxml', 'inkex']  #5
pkg_dir = "C:/Users/"+gp.getuser()+"/p_info.txt"

installed_pkg = sorted(["%s" %(i.key) for i in pkg_resources.working_set])

class web_activityListener:
    # internet connection establisher, need only for class UserMode:3
    def chk_connection():
        try:
            request = requests.get('https://www.google.com', timeout= 3)
            return True
        except (requests.ConnectionError, requests.Timeout) as exception:
            ch = input("[MSG: No internet connection detected!\n      Connect to the internet & press ENTER :(]\n")
            if ch in ['exit', 'EXIT', 'exit()', 'EXIT()']:
                print("[MSG: Process terminated!]")
                sys.exit()
            return web_activityListener.chk_connection()


class NormalMode:
    def py_uninstall_pkg(self):
        nof_unispkg = 0
        pkg_not_installed = []

        # Function for uninstalling requested modules:
        def uninstall_module(_pkg_name):
            subprocess.check_output([sys.executable, "-m", "pip", "uninstall", _pkg_name, "-y"])
            print(f"[successfully uninstalled: {_pkg_name}]")

        for j in modules:
            if j not in installed_pkg:
                pkg_not_installed.append(j)

        if len(pkg_not_installed) == len(modules):
            print("[MSG: No requested packages found for uninstallation!]")
        else:
            for i in modules:
                if i in installed_pkg:
                    uninstall_module(i)
                    nof_unispkg+=1
                else:
                    print(f"Package '{i}' not installed!")
 
        if nof_unispkg != 0:
            if nof_unispkg != 1:
                print(f"\n[MSG: Successfully uninstalled {nof_unispkg} packages]")
            elif nof_unispkg == 1:
                print(f"\n[MSG: Successfully uninstalled {nof_unispkg} package]")


class IntelliMode:
    def py_uninstall_pkg2(self):
        No_of_UninsPkg = 0
        f = 0
        data = []
    
        # Function for uninstalling requested modules.   
        def uninstall_pkg(_pkg_name):
            subprocess.check_output([sys.executable, "-m", "pip", "uninstall", _pkg_name, "-y"])
            print(f"[successfully uninstalled: {_pkg_name}]")
    
        if os.path.isfile(pkg_dir):        
            with open(pkg_dir, "r") as re_info:
                data = re_info.read()
            data = data.split("\n")
            while("" in data):
                data.remove("")
            for i in data:
                if i in installed_pkg:
                    uninstall_pkg(i)
                    No_of_UninsPkg+=1
                else:
                    print(f"Package '{i}' not installed")
                    
            if not No_of_UninsPkg == 0:
                print(f"\nSuccessfully uninstalled {No_of_UninsPkg} packages.")
            elif No_of_UninsPkg == 0:
                print("[MSG: No requested packages found for uninstallation!]")
        else:
            print(f"\n[Unable to locate package_info file in your system,")
            print("[This script will delete all main six pre-defined packages.]\n")
        
            for j in modules:
                if j in installed_pkg:
                    uninstall_pkg(j)
                    f+=1
                else:
                    print(f"Package {j} not installed")
            print(f"\nSuccessfully uninstalled {f} package(s)!")
            data.clear()


class UserMode:
    # Function for uninstalling user requested modules.   
    def usermodeconfig(self):
        # function for installing/uninstalling pacakges:
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
                            print("\n[MSG: Process terminated!]")
                            break
                        if loop not in ['y', 'Y', 'n', 'N']:
                            print(f"\n[MSG: Invalid entery: {loop}]\n[Process terminated!]")
                            break
                        print("")
                else:
                    web_activityListener.chk_connection()
            elif _choice in ['abort', 'ABORT', '1']:
                print("\n[MSG: Process terminated!]")
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
        # creates global object for UNINSTALLALLPACKAGES class:
        obj1 = NormalMode()
        print("\n[Mode: Normal-Mode]")
        # call UNINSTALLALLPACKAGES class:
        obj1.py_uninstall_pkg()
    elif _inp == '2':
        # create global object for UNINSINTELLIMODE class:
        obj2 = IntelliMode()
        print("\n[Mode: Intelli-Mode]")      
        # call UNINSINTELLIMODE class:
        obj2.py_uninstall_pkg2()
        # removes uninstalled pacakges names from list [for IntelliMode]
        with open(pkg_dir, "w") as wr:
            wr.write("")
    elif _inp == '3':
        # create global object for UNINSUSERMODE class:
        obj3 = UserMode()
        print("\n[Mode: User-Mode]")
        obj3.usermodeconfig()
    elif _inp == '0':
        ws.Beep(3900,850)
        sys.exit()
    else:
        print(f"\n[MSG: Invalid choice: {_inp}]")
        sys.exit()

    #input("\n(press any key to exit)")