# [Part of GCODE-MAKER-3.0 Extension Pack] [main_config_script]

# Gcode-Maker-3.0 extension configuration script
# ----------------------------------------------

# [ Advanced algorithm v3.0 ]

''' Python script for allocating external 'python v3.10' as default python interpreter
    for inkscape v1.1 x64, adding several keyboard short-cuts for extensions under
    Gcode-Maker Utilities and also for installing required python packages  
'''

# [ This script is only compatible with AMD64/64bit system ]

# Code by : vishnus_technologies (C)2022
# Created on : 28-08-2021 04:22PM
# File name : Inkp_config.py
# File version : 3.20.1.0
# ------------------------------------------------------------

import fileinput
import os
import subprocess
import sys
import requests
import pkg_resources

id = '6bdb138eceaa9f57a6eeb0bcc090d993'
_username = os.getenv('username')  # this guy fetches system user-name

# short-key scripts for extensions under this pack.
# [below script supports only on Inkscape >v1.1]
shortcut_script = '''  <bind
     key="A"
     action="vishnus_technologies.gcodemaker3.0" />
  <bind
     key="F"
     action="vishnus_technologies.hatch" />
  <bind
     key="T"
     action="vishnus_technologies.text.hershey" />
  <bind
     key="a"
     action="vishnus_technologies.gcodemaker3.0"
     display="true" />
  <bind
     key="f"
     action="vishnus_technologies.hatch"
     display="true" />
  <bind
     key="t"
     action="vishnus_technologies.text.hershey"
     display="true" /> '''

gcode_c = '''  <bind
     key="A"
     action="vishnus_technologies.gcodemaker3.0" />
  <bind
     key="a"
     action="vishnus_technologies.gcodemaker3.0"
     display="true" />'''

hatch_fill = '''  <bind
     key="F"
     action="vishnus_technologies.hatch" />
  <bind
     key="f"
     action="vishnus_technologies.hatch"
     display="true" /> '''

hershey_text = '''  <bind
     key="T"
     action="vishnus_technologies.text.hershey" />
  <bind
     key="t"
     action="vishnus_technologies.text.hershey"
     display="true" /> '''

# absolute path declaration:
_appdata = os.getenv('APPDATA').replace('\\', '/')
pref_src =  f"{_appdata}/inkscape/preferences.xml"
skeys_src = f"{_appdata}/inkscape/keys/default.xml"

# standard python interpreter path pattern across all windows-OS system:
_pypath39 = f"C:/Users/{_username}/AppData/Local/Programs/Python/Python39/pythonw.exe"
_pypath310 = f"C:/Users/{_username}/AppData/Local/Programs/Python/Python310/pythonw.exe"


# class for configurating preferences.xml file.
class InterpreterDataConfig:
    # sub main function
    def exec_config(self, pref_xml, srch_val1A, srch_val1B):
        py_exec = "python-interpreter="
        py_exec1 = "python-interpreter="
        found_flag1 = 0
        found_pystring = 0

        # reccursive function for creating/reminding, if not found preferences.xml file at Appdata:
        def create_pref():
            try:
                r_pf = open("preferences.xml", "r")
                obj_data = r_pf.read()
                r_pf.close()
                wr_pf = open(pref_xml, "w")
                wr_pf.write(obj_data)
                wr_pf.close()
            except FileNotFoundError:
                input("ERROR: Unable to locate main preferences.xml file at :\n" + os.getcwd() + "\n[Please add"
                      "the script at the above directory and press Enter]\n")
                create_pref()

        # function for replacing strings occasionally:
        def string_repl(file_name, searchExp1, replaceExp1):
            for line in fileinput.input(file_name, inplace=1):
                if searchExp1 in line:
                    line = line.replace(searchExp1, replaceExp1)
                sys.stdout.write(line)
            fileinput.close()

        # returning latest info about installed interpreter:
        def inptr_functs():
            inpts = []
            # returns max py installed version:
            def get_max_pyver(pydir, pyver):
                if os.path.isfile(pydir):
                    print(f"MSG: Python interpreter v{pyver} found")
                    inpts.append(pyver)
                else:
                    print(f"MSG: Python interpreter v{pyver} not found!")
                Max = 0
                for i in inpts:
                    if i > Max:
                        Max = i
                return Max
            
            # function for assigning interpreter version, when executable not found,
            # for setting user input python interpreter as choice:
            def set_usr_pyinpt():
                _consolemsg = '''Please choose the python version which you want to continue with [1/2]?
[NB: Choose the python version accordingly which you will install later, 
     the path will be assigned differently for each versions in extension 
     preferences script by default. visit: https://www.python.org for more...]
'''
                print(_consolemsg)
                ans = int(input("-> Press 1 for Python version 3.9\n-> Press 2 for Python version 3.10\n"))
                if ans == 1:
                    py_choice = py_exec + '"' + _pypath39 + '"'
                    py_choice1 = py_exec1 + '"' + _pypath39 + '"' + " />"
                elif ans == 2:
                    py_choice = py_exec + '"' + _pypath310 + '"'
                    py_choice1 = py_exec1 + '"' + _pypath310 + '"' + " />"
                else:
                    py_choice = py_exec + '"' + _pypath39 + '"'
                    py_choice1 = py_exec1 + '"' + _pypath39 + '"' + " />"
                return py_choice, py_choice1

            return set_usr_pyinpt()

        # function for adding insertation point, if not found!:
        def addInsertion():
            found_ins = 0
            with open(pref_xml, "r") as read_obj:
                for line in read_obj:
                    if '</inkscape>' in line:   #insertation keyword '</inkscape>'
                        found_ins = 1
            if found_ins == 1:
                string_repl(pref_xml, '</inkscape>', '  <group\n\tid="extensions" />\n</inkscape>')
                return True
            else:
                create_pref()
                print("[MSG: No tag_Id: 'extensions' found, Unable to create tag_ID:\n"
                      "      {</inkscape>} end-tag missing, re-created file!]\n")
                return False
                
        # validates python interpreter's location in system
        _version = ""
        stringFound1 = 0
        python_dir = sys.executable
        python_dir = python_dir.replace('python.exe', 'pythonw.exe')
        if os.path.isfile(python_dir):
            try:
                _version = str("v" + str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2]))
            except (SyntaxError, ValueError, IndexError, AttributeError, AssertionError, TypeError, NameError):
                _version = ""
            if len(_version) == 0:
                _version = "interpreter"
            print(f"[Found python {_version} on your system]\n{python_dir}\n")
            py_exec = py_exec + '"' + python_dir + '"'
            py_exec1 = py_exec1 + '"' + python_dir + '"' + " />"
        else:
            print("[Unable to locate python-interpreter on your system,\n It seems you have not installed python!]\n")
            Ichoice1, Ichoice2 = inptr_functs()
            py_exec = Ichoice1
            py_exec1 = Ichoice2

        if not os.path.isfile(pref_xml):
            try:
                r_pf = open("preferences.xml", "r")
                obj_data = r_pf.read()
                r_pf.close()
                if os.path.isfile("preferences.xml"):
                    wr_pf = open(pref_xml, "w")
                    wr_pf.write(obj_data)
                    wr_pf.close()
                print("[preferences.xml file not found. (automatically created!)]")
            except FileNotFoundError:
                input(f"ERROR: Unable to locate preferences.xml file at :\n{os.getcwd()}\n[Please add the"
                            "script at the above directory and press Enter]\n")
                create_pref()

        if os.path.isfile(pref_xml):
            if os.stat(pref_xml).st_size == 0:
                create_pref()
                print("[MSG: preferences.xml file is empty, no tags found\n      automatically created new file!]\n")
            else:
                # check if 'id="extensions"' or 'id="extensions" />' line found or not:
                with open(pref_xml, "r") as read_xml1:
                    for line in read_xml1:
                        if srch_val1A in line or srch_val1B in line:
                            stringFound1 = 1
                if stringFound1 != 1:
                    if addInsertion():
                        print("[MSG: No tag_ID: 'extensions' found on file,\n      automatically created tag_ID!]\n")

        # checks if python path already assigned or not:
        with open(pref_xml, "r") as read_obj:
            for line in read_obj:
                if 'python-interpreter' in line:
                    found_pystring = 1

        if not found_pystring == 1:
            # check for pattern : 'id="extensions" />':
            with open(pref_xml, "r") as read_obj:
                for line in read_obj:
                    if srch_val1A in line:
                        found_flag1 = '1A'
                    if srch_val1B in line:
                        found_flag1 = '2B'

            if found_flag1 == '1A':
                print(f"Found normal pattern : {srch_val1A}")
                string_repl(pref_xml, srch_val1A, srch_val1A + "\n\t " + py_exec)
                print("[MSG: Python path assigned successfully]\n")   
            elif found_flag1 == '2B':
                print(f"Found pattern : {srch_val1B}")
                string_repl(pref_xml, srch_val1B, srch_val1A + "\n\t " + py_exec1)
                print("[MSG: Python path assigned successfully]\n")
            else:
                addInsertion()
        else:
            print("[MSG: Python path already assigned : preferences.xml]\n")


# class for configurating default.xml (inkscape's short-key script) file.
class PreAppdataConfig:
    def validate_keys(self, default_xml, srch_val2):
        stringFound2 = 0
        stringFound3 = 0
        default_svg = f"{_appdata}/inkscape/templates/default.svg"
        found_skey = 0
        _gcode_c = 0
        _hatch_fill = 0
        _hershey_text = 0
        _extsn = []

        # in-built definition for replacing strings occasionally:
        def key_repl(_filename, searchExp2, replaceExp2, ext_name):
            for line in fileinput.input(_filename, inplace=1):
                if searchExp2 in line:
                    line = line.replace(searchExp2, replaceExp2)
                sys.stdout.write(line)
            fileinput.close()
            if not ext_name == None:
                print(f"Shortkey for '{ext_name}' assigned successfully")

        def write_header_script(_script):
            k = open(default_xml, "w")
            k.write(_script)
            k.close()

        # re-creates default.svg file:
        def create_dxf_svg():    
            if os.path.isfile("default.svg"):
                with open("default.svg", "r") as r_svg:
                    svg_rdata = r_svg.read() 
                with open(default_svg, "w") as w_svg:
                    w_svg.write(svg_rdata)
            else:
                print(f"ERROR: Unable to locate default.svg file at :\n{os.getcwd()}\n")

        # header short-key script to be added when default.xml is created fresh:
        header_script = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<keys
  name="User Shortcuts"> 
</keys> '''

        if not os.path.isfile(default_xml):
            write_header_script(header_script)
            print("\n[MSG: default.xml file not found! (automatically created!)]")
        if os.path.isfile(default_xml):
            if os.stat(default_xml).st_size == 0:
                write_header_script(header_script)
                print("[MSG: default.xml file is empty, no script/tags found,\n      automatically created with headers!]\n")
            else:
                # check if: {name="User Shortcuts">} line found or not
                with open(default_xml, "r") as read_xml:
                    for line in read_xml:
                        if srch_val2 in line:   #srch_val2:{name="User Shortcuts">}
                            stringFound2 = 1

                # if not found section: {name="User Shortcuts">}:
                if stringFound2 == 0:
                    # add section: {User Shortcuts}
                    with open(default_xml, "r") as read_xml: 
                        for line in read_xml:
                            if '<keys' in line:
                                stringFound3 = 1
                    # if found: insertation slot '<keys':
                    if stringFound3 == 1:
                        key_repl(default_xml, '<keys', '<keys\n' + srch_val2, None)
                        print("[MSG: No section-name: 'User Shortcuts' found on file,\n      automatically created section!]\n")
                    # if not found: insertation slot '<keys':
                    elif stringFound3 == 0:
                        # re-creates 'default.xml' file in default:
                        with open("default.xml", "r") as read_xml1:
                            _content = read_xml1.read()
                        with open(default_xml, "w") as write_xml1:
                            write_xml1.write(_content)
                        print("[MSG: No section name: 'User-Shortcuts' found. Unable to create section:\n"
                              "      {<keys} start-tag missing, re-created file!]\n")

        # checks if short-keys already assigned or not:
        with open(default_xml, "r") as read_obj:
            for line in read_obj:
                if 'action="vishnus_technologies.gcodemaker3.0"' in line: _gcode_c = 1
                if 'action="vishnus_technologies.hatch"' in line: _hatch_fill = 1
                if 'action="vishnus_technologies.text.hershey"' in line: _hershey_text = 1
        
        # search and start assigning shortkeys from here, if needed:
        if _gcode_c == 0:
            key_repl(default_xml, srch_val2, srch_val2 + "\n" + gcode_c, 'Gcode-Maker-3.0')
        else:
            _extsn.append('Gcode-Maker-3.0')
        if _hatch_fill == 0:
            key_repl(default_xml, srch_val2, srch_val2 + "\n" + hatch_fill, 'Hatch-Fill')
        else:
            _extsn.append('Hatch-Fill')
        if _hershey_text == 0:
            key_repl(default_xml, srch_val2, srch_val2 + "\n" + hershey_text, 'Hershey-Text')
        else:
            _extsn.append('Hershey-Text')

        if len(_extsn) != 0:
            print("[Shortcuts already assigned for: ")
            for arr in _extsn:
                print(arr+", ", end="")
            print("\b\b]")

        # cares about default.svg file: 
        if not os.path.isfile(default_svg):
            create_dxf_svg()
            print("\n[MSG: default.svg file not found. (automatically created!)]")
        if os.path.isfile(default_svg):
            if os.stat(default_svg).st_size == 0:
                create_dxf_svg()
                print("\n[MSG: default.svg file is empty,\n      automatically created new file!]")
            if not os.stat(default_svg).st_size > 1100:
                create_dxf_svg()
                print("\n[MSG: default.svg file contain invalid script,\n      automatically re-created the file!]")


''' Packages required:
keyboard v0.13.5, pywinauto v0.6.8, pyautogui v0.9.52
inkex v1.0.1, lxml v4.6.2, numpy v1.20.1 ''' 

# function for installing required python packages.
def pkg_configurations():
    # notify, when no internet connection after ping-time 3000ms
    def internet_estb():
        try:
            request = requests.get(ping_url, timeout=_timeout)
            print("\nstarting installer...")
            config_pkg(modules, installed_pkg)
        except (requests.ConnectionError, requests.Timeout) as exception:
            ch = input("[MSG: No internet connection detected! Retry again :(]\n")
            if ch in ['exit()', 'exit', 'EXIT', 'EXIT()']:
                exit()
            internet_estb()

    # module configuration definition:
    def config_pkg(_modules, _installed_pkg):
        # print(installed_pkg)
        for module in _modules:
            if module in _installed_pkg:
                print(f"[Requirement already satisfied: {module}]")
            else:
                install_pkg(module)

    # function for installing requested modules:
    def install_pkg(_pkg_name):
        subprocess.check_output([sys.executable, "-m", "pip", "install", _pkg_name])
        print(f"Successfully installed: {_pkg_name}")

    pkg_to_install = []
    ping_url = "https://www.google.com"
    _timeout = 3  #[in secs]
    modules = ['keyboard', 'pywinauto', 'pyautogui', 'lxml', 'inkex', 'numpy']  # 6
    installed_pkg = sorted(["%s" % (i.key) for i in pkg_resources.working_set])
    for i in modules:
        if i not in installed_pkg:
            pkg_to_install.append(i)
    try:
        # checking internet connection:
        request = requests.get(ping_url, timeout=_timeout)
        if not len(pkg_to_install) == 0:
            print("\nstarting installer...")
            config_pkg(modules, installed_pkg)
            if len(pkg_to_install) == 1:
                print(f"\n[MSG: Successfully installed {len(pkg_to_install)} package]")
            elif len(pkg_to_install) > 1:
                print(f"\n[MSG: Successfully installed {len(pkg_to_install)} packages]")
        else:
            print("\n[MSG: Required packages are already installed!]")
    except (requests.ConnectionError, requests.Timeout) as exception:
        if not len(pkg_to_install) == 0:
            if len(pkg_to_install) > 1:
                _packg = 'packages'
            else:
                _packg = 'package'
            print(f"\n[MSG: No internet connection detected!]\nUnable to install {len(pkg_to_install)} {_packg}: {pkg_to_install}")
            input("Connect to the internet and press enter!\n")
            internet_estb()
        if len(pkg_to_install) == 0:
            print("\n[MSG: Required packages are already installed!]")
            print("[NB : No Internet Connection!]")

    # create info-file about installed packages at :
    if not len(pkg_to_install) == 0:
        filep = f"{os.getenv('userprofile')}\p_info.txt"
        try:
            _infofile = open(filep, "w")
            for _name in pkg_to_install: 
                _infofile.write(_name + "\n")
            _infofile.close()
        except FileNotFoundError:
            print(f"\n[MSG: Path '{filep}' not exists.\n      Created at:C:/Users/p_info.txt]")
            with open("C:/Users/p_info.txt", "w") as wr_inf:
                for _name in pkg_to_install: 
                    wr_inf.write(_name + "\n")




# Main method:
if __name__ == '__main__':
    print("Extension Configuration Script v3.20.1.0")
    print("[For Gcode-Maker-3.0]")
    print("----------------------------------------\n")
    if not os.getenv('processor_architecture') == 'AMD64':
        print(f"[MSG: This script is not compatible with current architecture: {os.getenv('processor_architecture')}]"
               "\n[Install and try with AMD64/64bit system!] ")
        sys.exit()
    
    # call INTERPRETERDATACONFIG class:
    pref_object1 = InterpreterDataConfig()
    pref_object1.exec_config(pref_src, 'id="extensions"', 'id="extensions" />')
    print("-----------------------------------------------------\n")

    # call PREAPPDATACONFIG class:
    key_object2 = PreAppdataConfig()
    key_object2.validate_keys(skeys_src, 'name="User Shortcuts">')
    print("\n-----------------------------------------------------")

    # call PKGCONFIGURATIONS class:
    pkg_configurations()


    #input("\n(press any key to exit)")