# package_installer.py

'''
python script for installing packages requested from Inkp_config.py script
also detectes internet conn. before installing.  '''

# Code by : vishnus_technologies (C)2022
# Created on : 27-08-2022 | 11:37PM
# File name : pkg_installer.py
# File version : 3.1.5
# ----------------------------------------


import sys
import pkg_resources
import subprocess
import requests
from time import sleep as sl

exit_keySet = ['exit', 'EXIT', 'Exit', 'ESC', 'Esc', 'esc', 'exit()', 'EXIT()', 'Exit()', 'ESC()', 'Esc()', 'esc()']

def install_pkgg(_pkg):
    # to check for active internet conn.
    def chk_connection():
        try:
            request = requests.get('https://www.google.com', timeout= 3)
            return True
        except (requests.ConnectionError, requests.Timeout) as exception:
            ch = input("[MSG: No internet connection detected!\n      Connect to the internet & press ENTER]\n")
            if ch in exit_keySet:
                print("[MSG: OK, Process terminated!]")
                sys.exit()
            return chk_connection()

    # install requested python package from PyPI
    def install_module(_pkg_name):
        subprocess.check_output([sys.executable, "-m", "pip", "install", _pkg_name])
        print(f"[MSG: successfully installed: {_pkg_name}]")


    intMsg = "checking your internet connection..."
    print(intMsg)
    sl(1)
    if chk_connection(): 
        for i in range(len(intMsg)+1):
            print(end="\b")
        print("[MSG: Internet connection established]")
        install_module(_pkg)
    print("\n")
