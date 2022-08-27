# [ .pyc auto compiler algorithm ]


''' python advanced auto compiler algorithm for compiling
.py scripts to .pyc script (converts HLL into compiled python byte codes)
NOTE: So each time when the scripts run, compiler do not need to fetch 
libraries and prefetches, on converting them into byte code, compilation 
time, system load will be lesser. '''


# Code by : vishnus_technologies (C)2022
# Created on : 09-04-2022 | 08:16PM
# File name : _pyc_compiler.pyw
# File version : 3.20.2.1
# ----------------------------------------

import py_compile as _pc
import os

# globals
_username = os.getenv('username')
_GM3src = f"C:/Users/{_username}/Desktop/GcodeMakerUserFile_V3/sourcefiles"

# compile script paths:
loc = [f"{_GM3src}/Inkp_config.py",
f"{_GM3src}/pkg_uninstaller.py",
f"{_GM3src}/_checksrc.py"]

i=0
for path_to_file in loc:
    _pc.compile(path_to_file)
    i+=1
if i == len(loc):    
    if i == 1:
        print(f"[MSG: successfully compiled {i} python script]")
    else:    
        print(f"[MSG: successfully compiled {i} python scripts]")