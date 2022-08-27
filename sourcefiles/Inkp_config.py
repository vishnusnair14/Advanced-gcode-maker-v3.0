# [Part of GCODE-MAKER-3.0 Extension Pack] **[main_config_script]**

# Gcode-Maker-3.0 extension configuration script
# ----------------------------------------------

# [ Advanced algorithm v3.0 ]

''' Python script for allocating external 'python v3.10' as default python interpreter
    for inkscape v1.1 x64, adding several keyboard short-cuts for extensions under
    Gcode-Maker Utilities and also for installing required python packages  '''

# [NB: Only compatible with x64bit systems, windows-7 & above]

# Code by : vishnus_technologies (C)2022
# Created on :  28-08-2021 | 04:22PM
# Last updated: 14-07-2022 | 11:00PM
# File name : Inkp_config.py
# File version : 3.20.1.1
# --------------------------------------------

import pkg_installer as pi

# linking main libraries:
try:
    import os
    import fileinput
    import subprocess
    import shutil
    import time
    import sys
    import requests
    import pkg_resources
    import keyboard
except ImportError as IE:
    print(f"[MSG: {IE}]")
    pi.install_pkgg(IE.name)

# absolute path declaration:
_username = os.getenv('username')  # this guy fetches system user-name
_appdata = os.getenv('APPDATA').replace('\\', '/')     # fetch system appdata path
pref_src =  f"{_appdata}/inkscape/preferences.xml"
skeys_src = f"{_appdata}/inkscape/keys/default.xml"

exit_keySet = ['exit', 'EXIT', 'Exit', 'ESC', 'Esc', 'esc', 'exit()', 'EXIT()', 'Exit()', 'ESC()', 'Esc()', 'esc()']
abort_keySet = ['abort', 'ABORT', 'Abort', 'abort()', 'ABORT()', 'Abort()']

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


# pause-and-exit funct.
def PAUSE_AND_EXIT():
    input("\n( ~ press any key to exit )")
    sys.exit()

# class for configuring python-interpreter for this process.
class CompilerConfigurations:
    def validate_pyInpt(self):
        # standard py Inptr path pattern across all windows-OS system:
        _pypath39 = f"{_appdata.replace('Roaming', 'Local')}/Programs/Python/Python39/pythonw.exe"
        _pypath310 = f"{_appdata.replace('Roaming', 'Local')}/Programs/Python/Python310/pythonw.exe"

        # function for assigning interpreter version, when executable not found,
        # for setting user input python interpreter as choice:
        def set_usr_pyinpt():
            global _vrsn
            _vrsn = ""
            _consolemsg = f'''***************************************************************************************************
[MSG: NO VALID python interpreter found on your system.]
Please choose the python version which you want to continue with.
[NB: Choose the python version accordingly which you will install later.
     So that the script automatically will assign the default path according to your choice,
     that path will be reflected across the script, mainly in the preferences script by default.
     visit: https://www.python.org for more...]\n
Default path for versions as follow:-
-------------------------------------
v3.9:- {_pypath39}
v3.10:- {_pypath310}
***************************************************************************************************'''
            print(_consolemsg)
            ans = int(input("CONFORMATION:- [1/2]?\n-> Press 1 for assigning python v3.9\n-> Press 2 for assigning python v3.10\n"))
            print("")
            if ans == 1:
                py_choice = py_exec + '"' + _pypath39 + '"'
                py_choice1 = py_exec1 + '"' + _pypath39 + '"' + " />"
                _vrsn = f"v3.9\n     default path: {_pypath39}"
            elif ans == 2:
                py_choice = py_exec + '"' + _pypath310 + '"'
                py_choice1 = py_exec1 + '"' + _pypath310 + '"' + " />"
                _vrsn = f"v3.10\n     default path: {_pypath310}"
            else:
                py_choice = py_exec + '"' + _pypath39 + '"'
                py_choice1 = py_exec1 + '"' + _pypath39 + '"' + " />"
                _vrsn = f"v3.9\n     default path: {_pypath39}"
            return py_choice, py_choice1

        # validates python interpreter's location in system
        _version = "[NOT AVAILABLE]" 
        py_exec = "python-interpreter="
        py_exec1 = "python-interpreter="
        python_dir = sys.executable
        python_dir = python_dir.replace('python.exe', 'pythonw.exe')

        if os.path.isfile(python_dir):
            py_exec = py_exec + '"' + python_dir + '"'
            py_exec1 = py_exec1 + '"' + python_dir + '"' + " />"
            try:
                _version = str("v" + str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2]))
            except (SyntaxError, ValueError, IndexError, AttributeError, AssertionError, TypeError, NameError):
                pass
            #if len(_version) == 0:
                #_version = "[NOT AVAILABLE]"
            # prints final information regarding py-compiler:
            print("Python compiler informations:-\n------------------------------")
            print(f"Python interpreter validated:    YES\n"
                  f"Path validated:                  YES\n"
                  f"Python path:                     {python_dir}\n"
                  f"Python version:                  {_version}\n"
                  f"System architecture:             {os.getenv('processor_architecture')}\n")
        else:
            Ichoice1, Ichoice2 = set_usr_pyinpt()
            py_exec = Ichoice1
            py_exec1 = Ichoice2
            print("Python compiler informations:-\n------------------------------")
            print(f"Python interpreter validated:    NO\n"
                  f"Path validated:                  NO\n"
                  f"Python path:                     {python_dir}\n"
                  f"Python version:                  [NOT AVAILABLE]\n"
                   "**************************************************************************************\n"
                   "MSG: Unable to detect python-interpreter automatically on your system, It seems you \n"
                  f"     have not installed python. As per conformation from the user, assigned with {_vrsn}\n"
                   "**************************************************************************************")
        return py_exec, py_exec1


# [ Extension Preference Configuration ]
# class for configuring preferences.xml file. [~Inkscape file]
class ExtensionPrefConfig:
    # sub main function
    def exec_config(self, pref_xml, srch_val1A, srch_val1B, _py_exec, _py_exec1):
        f1 = 0
        stringFound1 = 0
        found_flag1 = 0
        found_pystring = 0
        bin_dir = f"{os.getenv('programfiles')}/Gcode-Maker-3.0/"
        # reccursive function for creating/reminding, if not found preferences.xml file at Appdata:
        def create_pref():
            try:
                r_pf = open(bin_dir+"preferences.xml", "r")
                obj_data = r_pf.read()
                r_pf.close()
                wr_pf = open(pref_xml, "w")
                wr_pf.write(obj_data)
                wr_pf.close()
            except FileNotFoundError:
                input("ERROR: Unable to locate main preferences.xml file at :\n" + os.getcwd() + "\n[Please add"
                      "the script at the above directory and press Enter]\n")
                create_pref()

        # for replacing strings:
        def repl_string(file_name, searchExp1, replaceExp1):
            for line in fileinput.input(file_name, inplace=1):
                if searchExp1 in line:
                    line = line.replace(searchExp1, replaceExp1)
                sys.stdout.write(line)
            fileinput.close()

        # for adding insertation point, if not found!:
        def addInsertion():
            found_ins = 0
            with open(pref_xml, "r") as read_obj:
                for line in read_obj:
                    if '</inkscape>' in line:   #insertation keyword '</inkscape>'
                        found_ins = 1
            if found_ins == 1:
                repl_string(pref_xml, '</inkscape>', '  <group\n\tid="extensions" />\n</inkscape>')
                return True
            else:
                create_pref()
                print("**************************************************************\n"
                      "MSG: No tag_Id: 'extensions' found, Unable to create tag_ID.\n"
                      "      {</inkscape>} end-tag missing, re-created file!\n"
                      "**************************************************************")
                return False
        # preferences config. final summary:
        print("\npreferences.xml file configuration summary:-\n"
              "--------------------------------------------")
        if not os.path.isfile(pref_xml):
            try:
                r_pf = open(bin_dir+"preferences.xml", "r")
                obj_data = r_pf.read()
                r_pf.close()
                if os.path.isfile(bin_dir+"preferences.xml"):
                    wr_pf = open(pref_xml, "w")
                    wr_pf.write(obj_data)
                    wr_pf.close()
                print("File exists on system:   NO (automatically created with defaults!)")
                f1 = 1
            except FileNotFoundError:
                input(f"ERROR: Unable to locate preferences.xml file at :\n{os.getcwd()}\n[Please add the "
                            "script at the above directory and press Enter]\n")
                create_pref()

        if os.path.isfile(pref_xml):
            if not f1 == 1:
                print("File exists on system:\t\t YES")
            if os.stat(pref_xml).st_size == 0:
                create_pref()
                print("*************************************************\n"
                      "MSG: preferences.xml file is empty, no tags found\n"
                      "     automatically created new file with defaults!\n"
                      "*************************************************")
            else:
                # check if 'id="extensions"' or 'id="extensions" />' line found or not:
                with open(pref_xml, "r") as read_xml1:
                    for line in read_xml1:
                        if srch_val1A in line or srch_val1B in line:
                            stringFound1 = 1
                if stringFound1 != 1:
                    if addInsertion():
                        print("********************************************\n"
                              "MSG: No tag_ID: 'extensions' found on file,\n"
                              "     automatically created tag_ID!\n"
                              "********************************************")

        # check for python path already assigned or not:
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
                repl_string(pref_xml, srch_val1A, srch_val1A + "\n\t " + _py_exec)
                print("Python path already assigned:    NO\n"
                     f"Found pattern:\t\t {srch_val1A}\n"
                      "Pattern type:                    type-2 (not normal)\n"
                      "Python path assigned:            YES\n"
                     f"Assigned path line:              [{_py_exec}]\n"
                      "Status:                          SUCCESS\n")
            elif found_flag1 == '2B':
                repl_string(pref_xml, srch_val1B, srch_val1A + "\n\t " + _py_exec1)
                print("Python path already assigned:    NO\n"
                     f"Found pattern:                   {srch_val1B}\n"
                      "Pattern type:                    NORMAL\n"
                      "Path assigned by script:         YES\n"
                     f"Assigned path line:              [{_py_exec1}]\n"
                      "Status:                          SUCCESS\n")
            else:
                addInsertion()
        else:
            print("Python path already assigned:    YES\n")


# class for configuring default.xml (inkscape's short-key script) file.
class PreAppdataConfig:
    def validate_keys(self, default_xml, srch_val2):
        stringFound2 = 0
        f2 = 0
        stringFound3 = 0
        default_svg = f"{_appdata}/inkscape/templates/"
        _default_svg = "C:/Program Files/Gcode-Maker-3.0/default.svg"
        found_skey = 0
        _gcode_c = 0
        _hatch_fill = 0
        _hershey_text = 0
        _extsn_al_asgnd = []
        _extsn_asgnd = []

        # in-built definition for replacing strings occasionally:
        def key_repl(_filename, searchExp2, replaceExp2):
            for line in fileinput.input(_filename, inplace=1):
                if searchExp2 in line:
                    line = line.replace(searchExp2, replaceExp2)
                sys.stdout.write(line)
            fileinput.close()

        def write_header_script(_script):
            k = open(default_xml, "w")
            k.write(_script)
            k.close()

        # re-creates default.svg file:
        def create_dxf_svg():
            if not os.path.exists(default_svg):
                os.mkdir(default_svg)
            if os.path.isfile(_default_svg):
                with open(_default_svg, "r") as r_svg:
                    svg_rdata = r_svg.read()
                with open(default_svg+"default.svg", "w") as w_svg:
                    w_svg.write(svg_rdata)
            else:
                print(f"ERROR: Unable to locate default.svg file at :\n{_default_svg}")

        # calculates num-percentage of total value:
        def calc_numto_percnt(_total, _num):
            if _num <= _total: percentage = round(((_num/_total)*100), 2)
            else: percentage = '*'
            return percentage

        # header short-key script to be added when default.xml is created fresh:
        header_script = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<keys
  name="User Shortcuts">
</keys> '''

        print("\ndefault.xml file configuration summary:-\n"
              "----------------------------------------")
        if not os.path.isfile(default_xml):
            write_header_script(header_script)
            print("\nFile exists on system:             NO (automatically created)")
            f2 = 1
        if os.path.isfile(default_xml):
            if not f2 == 1:
                print("File exists on system:\t\t   YES")
            if os.stat(default_xml).st_size == 0:
                write_header_script(header_script)
                print("*******************************************************\n"
                      "MSG: default.xml file is empty, no script/tags found,\n"
                      "     automatically created with headers!\n"
                      "*******************************************************")
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
                        key_repl(default_xml, '<keys', '<keys\n' + srch_val2)
                        print("********************************************************\n"
                              "MSG: No section-name: 'User Shortcuts' found on file,\n"
                              "     automatically created section!\n"
                              "********************************************************")
                    # if not found: insertation slot '<keys':
                    elif stringFound3 == 0:
                        # re-creates 'default.xml' file in default:
                        with open("default.xml", "r") as read_xml1:
                            _content = read_xml1.read()
                        with open(default_xml, "w") as write_xml1:
                            write_xml1.write(_content)
                        print("***************************************************************************\n"
                              "MSG: No section name: 'User-Shortcuts' found. Unable to create section:\n"
                              "     {<keys} start-tag missing, re-created file!\n"
                              "***************************************************************************")

        # checks if short-keys already assigned or not:
        with open(default_xml, "r") as read_obj:
            for line in read_obj:
                if 'action="vishnus_technologies.gcodemaker3.0"' in line: _gcode_c = 1
                if 'action="vishnus_technologies.hatch"' in line: _hatch_fill = 1
                if 'action="vishnus_technologies.text.hershey"' in line: _hershey_text = 1

        # search and start assigning shortkeys from here, if needed:
        if _gcode_c == 0:
            key_repl(default_xml, srch_val2, srch_val2 + "\n" + gcode_c)
            _extsn_asgnd.append('Gcode-Maker-3.0')
        else:
            _extsn_al_asgnd.append('Gcode-Maker-3.0')
        if _hatch_fill == 0:
            key_repl(default_xml, srch_val2, srch_val2 + "\n" + hatch_fill)
            _extsn_asgnd.append('Hatch-Fill')
        else:
            _extsn_al_asgnd.append('Hatch-Fill')
        if _hershey_text == 0:
            key_repl(default_xml, srch_val2, srch_val2 + "\n" + hershey_text)
            _extsn_asgnd.append('Hershey-Text')
        else:
            _extsn_al_asgnd.append('Hershey-Text')
        # prints short-cuts keys, already assigned:
        if not len(_extsn_al_asgnd) == 0:
            print("Shortcuts already assigned:       ", *_extsn_al_asgnd, sep= " ")
            print(f"Pre-installation rate:\t\t   {calc_numto_percnt(3, len(_extsn_al_asgnd))}%")
        else:
            print("Shortcuts already assigned for:  None")
        #print(f"\b [{calc_numto_percnt(3, len(_extsn_al_asgnd))}%]")

        # print short-cuts keys, assigned by script:
        if not len(_extsn_asgnd) == 0:
            print("Shortcuts assigned now:\t\t  ", *_extsn_asgnd, sep=' ')
        else:
            print("Shortcuts assigned now:\t\t   None")

        # cares about default.svg file:
        if os.path.isfile(default_svg+"default.svg"):
            print("Found default.svg file:\t\t   YES")
            if os.stat(default_svg+"default.svg").st_size == 0:
                create_dxf_svg()
                print("**************************************\n"
                      "MSG: default.svg file is empty,\n"
                      "     automatically created new file!\n"
                      "**************************************")
            elif not os.stat(default_svg+"default.svg").st_size > 1100:
                create_dxf_svg()
                print("*************************************************\n"
                      "MSG: default.svg file contain invalid script,\n"
                      "     automatically re-created the file!\n"
                      "*************************************************")
            else:
                print("default.svg file check:\t\t   SUCCESS")
        if not os.path.isfile(default_svg+"default.svg"):
            create_dxf_svg()
            print("Found default.svg file:\t\t   NO (automatically created!)")


''' Packages required:
keyboard v0.13.5, pywinauto v0.6.8, pyautogui v0.9.52
inkex v1.0.1, lxml v4.6.2, numpy v1.20.1 '''

# deals with python packages related processess.
def pkg_configurations():
    # processing/printing, message animations:
    def advAnim1(_Fcmd, _symbol, _interval, _itteration, nof_symb_prnt, Fmsg):
        for i in range(_itteration):
            for j in range(nof_symb_prnt+1):
                print(f"{_Fcmd}{_symbol*j}", end="\r")
                time.sleep(_interval)
        if not Fmsg == None:
            print(Fmsg)
        # advAnim1("clac", '.', 1, 2, 3, 'ok')    # funct. call ex:

    # notify, when no internet connection after pinging 3000ms
    def internet_estb():
        try:
            request = requests.get(ping_url, timeout=_tout)
            config_pkg(modules, installed_pkg)
        except (requests.ConnectionError, requests.Timeout) as exception:
            ch = input("[MSG: No internet connection detected! Retry again]\n")
            if ch in exit_keySet:
                print("[MSG: OK, Process terminated!]")
                PAUSE_AND_EXIT()
            internet_estb()

    # function for installing requested modules:
    def install_pkg(_pkg_name):
        print(f"-> Installing package: {_pkg_name}", end="\r")
        subprocess.check_output([sys.executable, "-m", "pip", "install", _pkg_name])
        print(f"[MSG: Package {_pkg_name} installed successfully]")
        ins_pkg_now.append(_pkg_name)
        
    # module configuration definition:
    def config_pkg(_modules, _installed_pkg):
        # print("installing packages...")
        advAnim1("installing packages", '.', 0.5, 2, 3, None)
        for module in _modules:
            if module not in _installed_pkg:
                install_pkg(module)

    # create summary-file about installed packages:
    def create_info():
        if not len(pkg_to_install) == 0:
            _filep = f"{os.getenv('userprofile')}/p_info.txt"
            try:
                with open(_filep, "a") as _infofile:
                    for _name in pkg_to_install:
                        _infofile.write(_name + "\n")
                    print("[MSG: Info-file created successfully]")
            except FileNotFoundError:
                print(f"\n[MSG: Path '{_filep}' not exists.\n"
                       "      Created at: C:/Users/p_info.txt]\n")
                with open("C:/Users/p_info.txt", "w") as wr_inf:
                    for _name in pkg_to_install:
                        wr_inf.write(_name + "\n")
            except PermissionError as pE:
                print("[Error: Unable to access info file: Permission denied!]")

            # Uncomment below line to make info-file {_filep} hidden:
            # os.system("attrib +h " + _filep)

   # calculates num-percentage of total value:
    def calc_numto_percnt2(_total, _num):
        if _num <= _total:
            percentage = round(((_num/_total)*100), 2)
        else:
            percentage = '*'
        return percentage

    pkg_to_install = []     # packages to be installed
    pkg_al_installed = []   # packages already installed on system
    ins_pkg_now = []
    ping_url = "https://www.google.com"
    # google dns-server address:
    dns_server_addr1 = ['8.8.8.8']
    dns_server_addr2 = ['8.8.4.4']
    _tout = 3  #[in secs]
    modules = ['keyboard', 'pywinauto', 'pyautogui', 'lxml', 'inkex', 'numpy']  # 6
    installed_pkg = sorted(["%s" % (i.key) for i in pkg_resources.working_set])
    # fetch installed_pkgs & to_install_pkgs separatly:
    for i in modules:
        if i not in installed_pkg:
            pkg_to_install.append(i)
        else:
            pkg_al_installed.append(i)
    try:
        # check for internet connection:
        request = requests.get(ping_url, timeout=_tout)
        if not len(pkg_to_install) == 0:
            ins_cnf = input(f"\n[CONFIRMATION: {len(pkg_to_install)} package(s) not installed, would like to install now [Y/N]?]\n-> ")
            if ins_cnf in ['n', 'no', 'N', 'NO']:
                PAUSE_AND_EXIT()
            print("\n\nInternet connection detected:      YES")
            config_pkg(modules, installed_pkg)
            create_info()   # creates info-file right after installing packages.
        print("\n\nPackage configuration summary:-\n"
              "-------------------------------")
        print(f"No:of package(s) already installed: {len(pkg_al_installed)}")
        print("Packages already installed:        ", *pkg_al_installed)
        print(f"Pre-installation rate:\t\t\t{calc_numto_percnt2(len(modules), len(pkg_al_installed))}%")
        if not len(pkg_to_install) == 0:
            print(f"No:of package(s) installed now:\t{len(ins_pkg_now)}")
        if not len(ins_pkg_now) == 0:
            print("Packages installed now:               ", *ins_pkg_now)
        else:
            print("Packages installed now:\t\t\tNone")
    except (requests.ConnectionError, requests.Timeout) as exception:
        if not len(pkg_to_install) == 0:
            if len(pkg_to_install) > 1:
                _packg = 'packages'
            else:
                _packg = 'package'
            print(f"\n\n[MSG: No internet connection detected!]\nUnable to install {len(pkg_to_install)} {_packg}: {pkg_to_install}")
            input("Connect to the internet and press enter!\n")
            internet_estb()     # function call: internet establisher cum pkg installer.
            create_info()   # creates info-file right after installing packages.
            # prints summary, after recovering with active internetConn.
            print("\nPackage configuration summary:-\n"
                  "-------------------------------")
            print(f"No:of package(s) already installed: {len(pkg_al_installed)}")
            print("Packages already installed:        ", *pkg_al_installed)
            print(f"Pre-installation rate:\t\t\t{calc_numto_percnt2(len(modules), len(pkg_al_installed))}%")
            if not len(pkg_to_install) == 0:
                print(f"No:of package(s) installed now:\t{len(ins_pkg_now)}")
            if not len(ins_pkg_now) == 0:
                print("Packages installed now:               ", *ins_pkg_now)
            else:
                print("Packages installed now:\t\t\tNone")

        if len(pkg_to_install) == 0:
            print(f"No:of package(s) already installed:\t  {len(pkg_al_installed)}\n"
                   "Required packages already satisfied:  YES\n"
                   "Internet Connection detected:\t        NO")


# function for checking all scripts and libraries at extensions folder [inkscapes']
def _checksrc():
    # Globals:
    _libs_copied = []; _libs_tocopy = []
    _scripts_copied = []; _scripts_tocopy = []
    src_notfound_lib = []; src_notfound_scrpt = []

    # predefined variable constants provided by ISSCP.preprocessors:
    # [ DO NOT ALTER BELOW VARIABLE CONSTANTS! ]
    _appdata = os.getenv('appdata').replace('\\', '/')
    _pfGM3src = f"{os.getenv('ProgramFiles')}/Gcode-Maker-3.0/src".replace('\\', '/')
    #print(_pfGM3src)

    # all source directories:
    src_svg_to_gcode = f"{_pfGM3src}/svg_to_gcode//"
    src_axidraw_deps = f"{_pfGM3src}/axidraw_deps//"
    src_custom_HF = f"{_pfGM3src}/custom_HF//"

    # all destination directories:
    _extension_dir = f"{_appdata}/inkscape/extensions"  # inkscape's extensions directory
    dst_svg_to_gcode = f"{_extension_dir}/svg_to_gcode//"
    dst_axidraw_deps = f"{_extension_dir}/axidraw_deps//"
    dst_custom_HF = f"{_extension_dir}/custom_HF//"

    # scripts for GM3-extension:
    # full path for script: '''{_pfGM3src}+{_scriptname}'''
    _scriptname = ['/dxf_input.py',
    '/dxf_input.inx',
    '/gcode_3.py',
    '/gcode_3.inx',
    '/hatch.py',
    '/hatch.inx',
    '/hershey.py',
    '/hershey.inx',
    '/plot_utils_import.py']

    # funct. for checking all necessary scripts at Inkscapes' appdata folder,
    # if not found, this funct. will copy all missing scripts.
    def check_scripts():
        for _name in _scriptname:
            if not os.path.isfile(_extension_dir+_name):
                _scripts_tocopy.append(_name) # contains name of scripts , not found!

        # copying scripts, if not found:
        if not len(_scripts_tocopy) == 0:
            for _script_name in _scripts_tocopy:
                _src = f"{_pfGM3src}{_script_name}"
                _dst = f"{_extension_dir}{_script_name}"
                if os.path.exists(_src):
                    try:
                        shutil.copy(_src, _dst)
                        _scripts_copied.append(_script_name.replace('/', ''))
                    except:
                         print("[MSG: Error copying files.]")
                else:
                    #Beep(3565,150)
                    src_notfound_scrpt.append(_script_name.replace('/', ''))

    # function validates all libraries at appdata:
    def check_libs():
        # function for copy all contents of folder:
        def copy_allcontents(_srch, _dstn, file_name):
            try:
                shutil.copytree(_srch, _dstn)
                _libs_copied.append(file_name)
                #print(f"[MSG: copied {file_name} lib to Inkscape appdata folder]")
            except FileNotFoundError as _printException:
                src_notfound_lib.append(file_name.replace('/', ''))

        if not os.path.exists(dst_svg_to_gcode):
            _libs_tocopy.append('svg_to_gcode')
            copy_allcontents(src_svg_to_gcode, dst_svg_to_gcode, 'svg_to_gcode')

        if not os.path.exists(dst_axidraw_deps):
            _libs_tocopy.append('axidraw_deps')
            copy_allcontents(src_axidraw_deps, dst_axidraw_deps, 'axidraw_deps')

        if not os.path.exists(dst_custom_HF):
            _libs_tocopy.append('custom_HF')
            copy_allcontents(src_custom_HF, dst_custom_HF, 'custom_HF')

    # prints final summary:
    def _Fsummary():
        print("\n------------------------------------------")
        print("[:sripts & libraries checked successfully]\n------------------------------------------\n[:summary]")
        # script section:
        print("[:scripts-section]")
        if not len(_scripts_tocopy) == 0:
            print(f"No:of scripts not found:    {len(_scripts_tocopy)}")
        if not len(_scripts_tocopy)-len(_scripts_copied) == 0: 
            print(f"No:of un-copied scripts:    {len(_scripts_tocopy)-len(_scripts_copied)}")

        if not len(_scripts_copied) == 0:
            print("Scripts copied now:       [ ", end= "\b")
            print(*_scripts_copied, sep= ", ", end= "]\n")

        if (len(_scripts_tocopy)-len(_scripts_copied)) == 0 and len(_scripts_copied) == 0:
            print("[MSG: All necessary scripts already exists at extension folder]\n[status: PASS]")

        if (len(_scripts_tocopy)-len(_scripts_copied)) == 0 and len(_scripts_copied) != 0:
            print(F"[MSG: All {len(_scripts_copied)} missing scripts have been copied successfully]")

        if len(src_notfound_scrpt) != 0:
            print("**********************************************************************")
            print("[Remark: Unable to copy missing script at appdata, source not found!]\n"
                 f"Source missing at:    [{_pfGM3src}]")
            print("Source not found for: [ ", end= "\b")
            print(*src_notfound_scrpt, sep= ", ", end= "]\n")
            print("**********************************************************************")


        #library section:
        print("\n[:library-section]")
        if not len(_libs_tocopy) == 0 :
            print(f"No:of libraries not found:  {len(_libs_tocopy)}")
            
        if not len(_libs_tocopy)-len(_libs_copied) == 0:
            print(f"No:of un-copied libraries:  {len(_libs_tocopy)-len(_libs_copied)}")

        if not len(_libs_copied) == 0:
            print("Libraries copied now:     [ ", end="\b")
            print(*_libs_copied, sep= ", ", end= "]\n")

        if (len(_libs_tocopy)-len(_libs_copied)) == 0 and len(_libs_copied) == 0:
            print("[MSG: All necessary libraries already exists at extension folder]\n[status: PASS]")

        if (len(_libs_tocopy)-len(_libs_copied)) == 0 and len(_libs_copied) != 0:
            print(F"[MSG: All {len(_libs_copied)} missing libraries have been copied successfully]")

            # prints error infos:
        if len(src_notfound_lib) != 0:
            print("************************************************************************")
            print("[Remark: Unable to copy missing libraries at appdata, source not found!]\n"
                 f"Source missing at:    [{_pfGM3src}]")
            print("Source not found for: [ ", end= "\b")
            print(*src_notfound_lib, sep= ", ", end= "]\n")
            print("************************************************************************")

        if len(src_notfound_lib) or len(src_notfound_scrpt) != 0:
            print("\n*************************************************************************\n"
                  "[MSG: Extension may misbehave. Install all missing files and try again!]\n"
                  "*************************************************************************")

        # creates error log at: \\%USERPROFILE%\console_log.txt
        _eCLog = f"C:/Users/{os.getenv('username')}/console-log.txt"
        if len(src_notfound_scrpt) != 0 or len(src_notfound_lib) != 0:
            with open(_eCLog, 'a') as cnslog:
                cnslog.write("-------------------------------------------\n")
                cnslog.write(time.strftime("%A %d-%b-%Y | %I:%M:%S %p\n"))
                cnslog.write("\nScripts source not found for:-\n------------------------------\n")
                for i in src_notfound_scrpt:
                    cnslog.write(f"{src_notfound_scrpt.index(i)+1}. {i}\n")
                cnslog.write("\nLibrary source not found for:-\n------------------------------\n")
                for j in src_notfound_lib:
                    cnslog.write(f"{src_notfound_lib.index(j)+1}. {j}\n")
                cnslog.write("-------------------------------------------\n\n")
                print(f"\n[Successfully created CLog file at:\n{_eCLog}]")
        else:
            if not os.stat(_eCLog).st_size == 0:
                with open(_eCLog, 'w') as cnslog:
                    cnslog.write("")
                print("\n[Successfully cleared error-CLog file!]")

        # Uncomment below line to make 'console_log.txt' file {_eCLog} hidden:
        # os.system("attrib +h " + _eCLog)

    # auto create folder:extensions under inkscape:appdata, if not found!
    if not os.path.isdir(_extension_dir):
        os.makedirs(_extension_dir)
        print("[MSG: Inkscape-extension directory not found, auto created!]\n")

    # function call  (inside 'runcheck()'):
    check_libs()
    check_scripts()
    _Fsummary()


# restart prompt main definition:
def restart_prompt():
    _sec = 'seconds'
    _ifrsrt = 0
    _err = 0
    _dly = []
    delim = [',', ' ', '.', '|', '/']
    _rs = input("\n\nRESTART PROMPT:\nWant to restart the system [Y/N, exit/esc]?\ncmd: [Mode[Y/N], restart delay[in sec <10]]\n->")
    if _rs in exit_keySet:
        PAUSE_AND_EXIT()
        
    for c in range(len(delim)):
        _rs = _rs.replace(delim[c], " ")
    _rs = _rs.split()

    # detects mode [Y/yes or N/no]
    for j in _rs:
        if j in ['Yes', 'yes', 'YES', 'y', 'Y']:
            _ifrsrt = 1 # if{yes}:else{no}

    # detects restart delay
    for i in range(len(_rs)):
        try:
            _rs[i] = int(_rs[i])
            if (isinstance(_rs[i], int)):
                _dly.append(_rs[i])
        except:
            None

    try:
        _dly = min(_dly)
    except: 
        _dly = 0
    # print(_dly)
    
    if _ifrsrt == 1:
        if _dly>=1:
            if _dly<=10:
                if _dly == 1: _sec = 'second'
                else: _sec = 'seconds'
            else:
                print(f"[MSG: Restart delay {_dly}, must be less than or equal to 10s, try again.]")
                restart_prompt()
                _err = 1
        else:
            if _ifrsrt == 1:
                print(f"[MSG: Restart delay {_dly}, must be non negative, should be greater or equal to 1s, try again.]")
                restart_prompt()
                _err = 1

        if _err == 0:
            while _dly>0:
                if _dly == 1: _sec = 'second'
                print("MSG: system will attempt to restart in", _dly, _sec, end="\r")
                time.sleep(1)
                _dly-=1
            #time.sleep(_dly)
            
            print("[MSG: Restarting system now!]")
            time.sleep(1)
            # cmd system restart command:
            #os.system(f'shutdown /r /t {_dly}')
    else:
        print("[MSG: ok, The changes will take place after the next restart!]")



# Main method:
if __name__ == '__main__':
    print("Extension configuration summary:-\n"
          "---------------------------------\n" 
          "[For Gcode-Maker-3.0]")
    print(time.strftime("%A %d-%b-%Y | %I:%M:%S %p\n"))
    if not os.getenv('processor_architecture') == 'AMD64':
        print(f"\b[ERROR MSG: This script is not compatible with the current architecture: {os.getenv('processor_architecture')}]"
               "\n[Install and try with AMD64/64bit system!] ")
        PAUSE_AND_EXIT()
        

    # call PYTHONCOMPILERCHECK class:
    pref_object0 = CompilerConfigurations()
    py_exec, py_exec1 = pref_object0.validate_pyInpt()

    # call INTERPRETERDATACONFIG class:
    pref_object1 = ExtensionPrefConfig()
    pref_object1.exec_config(pref_src, 'id="extensions"', 'id="extensions" />', py_exec, py_exec1)

    # call PREAPPDATACONFIG class:
    key_object2 = PreAppdataConfig()
    key_object2.validate_keys(skeys_src, 'name="User Shortcuts">')

    # call PKGCONFIGURATIONS class:
    pkg_configurations()

    # call check source definition:
    print()
    _checksrc()

    # RESTART PROMPT: [restart the system in x second(s)]:
    # pattern: [Mode[~Y/N/Yes/No], restart_delay[~in sec]]
    # supported delimeters: {.} {,} {|} {\s ~whitespace}
    # eg: [{Yes.34} {YES,34} {y.2} {Y.23.45,7,3,14} {No}] [~excluded of curely braces]
    ''' NB: In the second last example (too many int convertable values), code auto
        detects lowest integer as restart delay[3 in that case] '''
    # Comment below line, if restart prompt, not required after installation:
    restart_prompt()

    PAUSE_AND_EXIT()