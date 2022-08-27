# [Part of GCODE-MAKER-3.0 Extension Pack]

# _update.pyw

# vishnus_technologies (C) 2022 
# Created on: 18-09-2021 | 09:53PM

''' Updates recent compile information about 'Gcode-Maker-3.0' folder
    and its sub files/folders, whenever this script is called.
    Updates information in update_log.txt file at same directory. '''
    
# file path = "\\GcodeMakerUserFile_V3\update_log.txt"
    
import time as t
import fileinput
import sys

info = t.strftime("\n\nRecently saved at:\nDate: %d-%b-%Y [%A] \nTime: %I:%M:%S %p")
header_text = '''[Part of GCODE-MAKER-3.0 Extension Pack]
----------------------------------------

GCODE-MAKER-3.0 
A controller software for writing bot. 

[vishnus_technologies TM (R) (C)2022]'''

# search for target string in file:
def srch_string(_string):
    fnd_flag = 0
    try:
        with open("update_log.txt", "r") as read_obj:
            for line in read_obj:
                if _string in line:
                    fnd_flag = 1
    except FileNotFoundError as err:
        print("[MSG: File: update_log.txt not found, auto created!")
        fnd_flag = 0
    if fnd_flag == 1:
        #print(fnd_flag)
        return True
    else:
        #print(fnd_flag)
        return False

# replace string at target file:
def chg_string():
    str_found = 0
    with open("update_log.txt", "r") as read_txt:
        for line in read_txt:
            if 'Recently' in line:
                str_found = 1
    if str_found == 1:
        for line in fileinput.input("update_log.txt", inplace=1):
            if 'Recently' in line:
                line = line.replace('Recently', 'File')
            sys.stdout.write(line)
        fileinput.close()
        
        
# opens a file, updates informations:
def UpdateFile(_WrtInfo, _mode):
        try:
            with open("update_log.txt", _mode) as obj:
                obj.write(f"{_WrtInfo}\n")
            if not len(_WrtInfo) == 0:
                print(f"Information updated. [ @IST {t.strftime('%I:%M:%S%p')} ]")
        except:
            print("[MSG: Error creating information file! Try again]")
 
 
if __name__ == "__main__":
    if srch_string('A controller software for writing bot.'):
        chg_string()
        UpdateFile(info, 'a')
    else:
        print("[MSG: File seems to be empty, updated with headers!]")
        UpdateFile(header_text+info, 'w')