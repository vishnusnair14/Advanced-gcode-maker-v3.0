# [Part of GCODE-MAKER-3.0 Extension Pack]

''' Python scirpt for checking all extensions, required
    scripts and libraries at Inkscape appdata folder. '''


# Total script-files to check : 9
# Total lib-folder to check   : 3

# Code by : vishnus_technologies (C)2022
# Created on : 28-03-2022 11:53AM
# File name : _checksrc.py
# File version : 3.0.2.0
# -------------------------------------------------------

import os
import shutil
import time
#from winsound import Beep as bB

# Globals:
_libs_copied = []; _libs_tocopy = []
_scripts_copied = []; _scripts_tocopy = []
src_notfound_lib = []; src_notfound_scrpt = []

# predefined variable contaning constants provided by ISSCP.preprocessors:
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
# full path for script: {_pfGM3src}+{_scriptname}
_scriptname = ['/dxf_input.py',
'/dxf_input.inx',
'/gcode_3.py',
'/gcode_3.inx',
'/hatch.py',
'/hatch.inx',
'/hershey.py',
'/hershey.inx',
'/plot_utils_import.py']


def runcheck():
    # function validates main python scripts at appdata:
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
    def print_Fsummary():
        print("Summary:-\n---------")
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

        # print error infos:
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
                print(f"\n[successfully created c-log file at:\n{_eCLog}]")
        else:
            if not os.stat(_eCLog).st_size == 0:
                with open(_eCLog, 'w') as cnslog:
                    cnslog.write("")
                print("\n[successfully cleared c-log file!]")

        # Uncomment below line to make 'console_log.txt' file {_eCLog} hidden:
        # os.system("attrib +h " + _eCLog)

    if not os.path.isdir(_extension_dir):
        os.makedirs(_extension_dir)
        print("[MSG: Inkscape-extension directory not found, auto created!]\n")

    # function call:
    check_libs()
    check_scripts()
    print_Fsummary()


# main method:
if __name__ == '__main__':
    runcheck()

    #input("(~ press any key to exit)")