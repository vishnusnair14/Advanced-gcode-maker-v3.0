# module_importer.py
# [Part of GCODE-MAKER-3.0 Extension Pack]

''' Sub script for safetly importing python modules for inkp_config.py script '''
# //srcf/bin/inkp_config.py

# NB: Internet connection required!

# Code by: vishnustechnologies (C)2021
# Created on : 15-11-2021 10:14PM

import subprocess, sys
import webbrowser


ModulesInUse = ['fileinput', 'os','subprocess','sys','getpass','requests','pkg_resources']
ErrorModules = []

# Function for importing core-modules:
def importmodule():
    try:
        import fileinput    #1
    except ModuleNotFoundError as ER1:
        ErrorModules.append(ER1.name)
    try:
        import os   #2
    except ModuleNotFoundError as ER2:
        ErrorModules.append(ER2.name)
    try:
        import subprocess   #3
    except ModuleNotFoundError as ER3:
        ErrorModules.append(ER3.name)
    try:
        import sys #4
    except ModuleNotFoundError as ER4:
        ErrorModules.append(ER4.name)
    try:
        import getpass  #5
    except ModuleNotFoundError as ER5:
        ErrorModules.append(ER5.name)
    try:
        import requests  #6
    except ModuleNotFoundError as ER6:
        ErrorModules.append(ER6.name)
    try:
        import pkg_resources    #7
    except ModuleNotFoundError as ER7:
        ErrorModules.append(ER7.name)
    print(ErrorModules)

# Redirects to respective url passed with:
def redirect(url):
    webbrowser.open(url, new=1)

# Function that make sure all the core-python-modules are available for further processings:
def config_modules():
    import pkg_resources
    installed_packages_list = sorted(["%s" % (i.key) for i in pkg_resources.working_set])
    for  module in ErrorModules:
        if module not in installed_packages_list:
            install_module(module)
        else:
            print(f"Module named {module} is already installed, may it be an ImportError\n Refer https://docs.python.org/3/library/exceptions.html")
            conf = input("Want to open Reference Manual in external web browser? optn:[y/n]")
            if conf == 'y' or conf =='Y':
                redirect('https://docs.python.org/3/library/exceptions.html') # internet connection required!
            
# NB: Internet connection required for this function.  
# Function for downloading/installing core modules, not installed before, using 'pip' command 
# visit https://pip.pypa.io/en/stable/ for more...
def install_module(package_name):
    try:
        subprocess.check_output([sys.executable, "-m", "pip", "install", package_name])
        print(f"Successfully installed: {package_name}")
    except:
        print("Some error occured! [pip], [Refer system-error-codec section]")
        
if __name__ == '__main__':
    importmodule()
    config_modules()
    #sanitycheck()           