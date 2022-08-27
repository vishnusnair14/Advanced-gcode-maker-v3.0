# [Part of GCODE-MAKER-3.0 Extension Pack]

# error_informer_framework.py [#robust methodology]

# path = C:\Users\%username%\AppData\Roaming\inkscape\extensions\svg_to_gcode\ugs_automation\
# href = svg_to_gcode.ugs_automation.error_informer_framework

# (C)2021 vishnus_technologies, error_informer_framework.py


''' This framework will check for the possibilities of errors while exporting gcode 
    for both the modes, UGS automation and in GUI parameters. It informs user and 
    inkscape's compiler when any of them occured ''' 

    
# Function Parameters Docs :
# --------------------------
#1  self - returns inkscape self options arguments.
#2  condt - returns true is agreed with all terms and conditions.
#3  wr_check - returns true when 'export gcode as new file' option is selected.
#4  append_check - returns true is append with file option is selected.
#5  ugs_target_directory - returns ugs application directory path.
#6  ugs_redir_write - returns true for opening newly export file in ugs.
#7  ugs_redir_append - returns true for opening appended file in ugs.


import os
import time

def ugs_error_check(self, condt, wr_check, append_check, ugs_target_directory, ugs_redir_write, ugs_redir_append):
    error_occ = 0
# error case 1
    if condt != True:
        self.debug(f"Please agree with our terms and conditions!")
        error_occ += 1

# error case 2
    if (wr_check or append_check) != True:
        self.debug(f"Error in exporting Gcode File!\nPlease select atleast one options from 'Export' tab!")
        error_occ += 1
    
# error case 3    
    if os.path.isfile(ugs_target_directory) != True:
        self.debug(f"Invalid UGS application location.\nPlease enter a valid file location path at 'UGS Target Path' tab and \nTry again!!!")
        error_occ += 1
   
# error case 4   
    if (self.options.ugs_redir_write == 0 and ugs_redir_append == 0):           
        self.debug(f"Select atleast one importing file type option from 'UGS' tab !") 
        error_occ += 1
    elif (ugs_redir_write == 1 and ugs_redir_append == 1):            
        self.debug(f"Select only one importing file type option in 'UGS' tab !")
        error_occ += 1
    
    ''' You can add as many error cases here... (if any) '''
    
    if not error_occ == 0:
        if error_occ == 1:
            self.debug(f"Total no:of error occured  = {error_occ}")
        if error_occ > 1:
            self.debug(f"Total no:of errors occured  = {error_occ}")
        c_time = time.strftime("%d.%m.%Y %H:%M:%S")
        self.debug(f"compiled at = {c_time}")

     
    if error_occ == 0:
        return True
    elif error_occ >= 1:
        return False