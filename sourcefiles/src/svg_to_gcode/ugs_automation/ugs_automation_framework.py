# [Part of GCODE-MAKER-3.0 Extension Pack]

# ugs_automation_framework.py

# path = C:\Users\%username%\AppData\Roaming\inkscape\extensions\svg_to_gcode\ugs_automation\
# href = svg_to_gcode.ugs_automation.ugs_automation_framework

# (C)2021 vishnus_technologies, ugs_automation_framework.py

''' Automation code for Universal Gcode Sender [UGS] goes here! 
    Opens universal gcode sender automatically with the required 
    gcode import instantly from Inkscape '''

# Function Parameters Docs :
# --------------------------
#1  self - returns inkscape self.options arguements.
#2  ugs_auto_serv - returns binary, if service enabled or not. [bool]
#3  ugs_target_directory - returns ugs application path.
#4  ugs_redir_write - returns binary for opening newly export file in ugs.
#5  ugs_redir_append - for opening appended file in ugs.
#6  ugs_process_delay - returns boot time of UGS application window.
#7  ugs_state - returns the state of UGS Application [whether runing or not].
#8  skey_connect - returns short key used for establishing connection with arduino in UGS.
#9  skey_open - returns short key used for opening file from PC. [.gcode file type] 
#10 directory - returns the directory of exporting as new file type.
#11 filename - returns file of the newly exporting file.
#12 append_directory - returns directory of appending type file.
#13 append_filename - returns filename of appending file.
#14 wr_check - returns true when 'export gcode as new file' option is selected.
#15 append_check - returns true when 'append gcode with file' option is selected.
#16 append_directory - returns the path directory of appending file.
#17 append_filename - returns the filename of appending file.


import time
import os
from pywinauto.application import Application
import pyautogui as pg
import keyboard
import winsound as UgsSoundHandler


# ***Definition of python UGS-Automation API Module*** 
# ----------------------------------------------------
# Opens 'UGS' Platform automatically with specific g-code file on request from inkscape 
# interface after the successful generation of gcode data].[inkscape ver => 1.0 x64 [or greater]]

# External python - Modules in use:- [keyboard.py,[pywinauto{comtype.py, win32API, 
#                                     comTypes, win32, pillow}], pyAutoGui, lxml, numpy]
# Note: This automation modules works only with UGS versions [2.0.0 snapshots Apr 17-2019]| and 
#                                                            [2.0.7 snapshots Dec 11-2021]
   
   
def ugs_auto(self, ugs_auto_serv, ugs_target_directory, ugs_redir_write, ugs_redir_append, ugs_process_delay, 
             ugs_state, skey_connect, skey_open, directory, filename, wr_check, append_check, append_directory,
             append_filename):
  
            if ((ugs_redir_append==0 and ugs_redir_write==1) or (ugs_redir_append==1 and ugs_redir_write==0)):  
                if ugs_redir_write:
                    if  wr_check != True:                   
                        pg.alert("You have not selected 'Export as a new gcode file' option from 'Export' tab. You will return with an error message while importing gcode file in 'UGS' window!, present loaded gcode data will be lost!")
                        return False
                        #time.sleep(4.7)
                    if  ugs_state == "nrun":        # if 'UGS' on.click().isConnect(): [returns 'True' if satisfies]
                        app = Application().start(cmd_line=ugs_target_directory)
                        sunawtframe = app.SunAwtFrame           # creates object for Target Application class.
                        time.sleep(0.5)
                        click_err_cmd = click_scrn_cntr() # clicks at screen center co-ordinates .  [TaskBar Loc.[x=1151,y=1063]]]
                        time.sleep(ugs_process_delay)  # processing time for 'UGS'.[depends on the system architecture and perfomance.] 
                        sunawtframe.maximize()         # maximizes 'UGS' Window.
                        sunawtframe.set_focus()        # set focus to 'UGS' window.
                        time.sleep(0.4)
                        keyboard.press(skey_connect)          # define the shortkey used for 'connect' in UGS to Establish connection with arduino on available default COM Port.
                        time.sleep(3.0)                # delay time (in 's')
                        keyboard.press(skey_open)            # define the shortkey used for 'open gcode file' in UGS.
                        time.sleep(0.6)
                        keyboard.press('BACKSPACE')
                        time.sleep(0.2)                # delay time (in 's')
                        pg.typewrite(directory+filename,0.05)         # writes gcode path on 'UGS import' window.
                        keyboard.press('ENTER')
                        UgsSoundHandler.Beep(3000,500)         #file opened alert sound
                    elif ugs_state == "yrun":      # else def. if target application is already running.      
                        time.sleep(0.2)
                        try:
                            app = Application().connect(path=ugs_target_directory)
                            sunawtframe = app.SunAwtFrame    # creates object for Target Application class.
                            time.sleep(0.5)
                            sunawtframe.maximize()     # maximizes 'UGS' Window.
                            sunawtframe.set_focus()    # set focus to 'UGS' window.
                            time.sleep(1.1)
                        except:                        #exception handling def. if connect() returns with an error.
                            app = Application().start(cmd_line=ugs_target_directory)
                            sunawtframe = app.SunAwtframe     # creates object for Target App class.
                            time.sleep(0.5)
                            click_err_cmd = click_scrn_cntr() # clicks at screen center co-ordinates .  [TaskBar Loc.[x=1151,y=1063]]]
                            time.sleep(ugs_process_delay) 
                            sunawtframe.maximize()     # maximizes 'UGS' Window.
                            sunawtframe.set_focus()    # set focus to 'UGS' window.
                            time.sleep(0.4)
                            keyboard.press(skey_connect)      # Establishing connection with arduino on available default COM Port.
                            time.sleep(3.0)                                                      
                        keyboard.press(skey_open)            # defined shortkey used for 'open gcode file' in UGS.
                        time.sleep(0.6)
                        keyboard.press('BACKSPACE')    # clears the text field before writing gcode file path.
                        time.sleep(0.2)                # delay time (in 's')
                        pg.typewrite(directory+filename,0.05)         # writes gcode path on 'UGS import' window.
                        time.sleep(0.5)
                        keyboard.press('ENTER')
                        UgsSoundHandler.Beep(3000,500)
                elif ugs_redir_append:
                    if append_check != True:
                        pg.alert("You have not selected appending gcode option from 'Export' tab. The present generated gcode data will not be reflected into append file.!")  
                        return False
                        #time.sleep(4.7)
                    if ugs_state == "nrun":
                        app = Application().start(cmd_line=ugs_target_directory)   # UGS application target file.
                        sunawtframe = app.SunAwtFrame        # creates object for Target Application class. 
                        time.sleep(0.2)
                        click_err_cmd = click_scrn_cntr()   # clicks at screen center co-ordinates .  [TaskBar Loc.[x=1151,y=1063]]]
                        time.sleep(ugs_process_delay)      # processing time. [depends on the system architecture and perfomance.] 
                        sunawtframe.maximize()         # maximizes 'UGS' Window.
                        sunawtframe.set_focus()        # set focus to 'UGS' window.
                        time.sleep(0.4)
                        keyboard.press(skey_connect)         # defines shortkey used for 'connect' in UGS to establish connection with arduino on available default COM Port.
                        time.sleep(3.0)                      # delay time (in 's')
                        keyboard.press(skey_open)            # defines shortkey used for 'open gcode file' in UGS.
                        time.sleep(0.6)
                        keyboard.press('BACKSPACE')
                        time.sleep(0.2)
                        pg.typewrite(append_directory+"APND_"+append_filename,0.05)    # writes gcode path on 'UGS import' window.
                        keyboard.press('ENTER')
                        UgsSoundHandler.Beep(3000,500)
                    elif ugs_state == "yrun":     # else def. if target application is already running.                    
                        time.sleep(0.2)
                        try:
                            app = Application().connect(path=ugs_target_directory)
                            sunawtframe = app.SunAwtFrame      # creates object for Target Application class.
                            time.sleep(0.5)
                            sunawtframe.maximize()     # Maximizes 'UGS' window  
                            sunawtframe.set_focus()    # set focus to 'UGS' window.
                            time.sleep(1.1)
                        except:                        #exception handling def. for connect(), if returns with an error.
                            app = Application().start(cmd_line=ugs_target_directory)   # UGS application target file.
                            sunawtframe = app.SunAwtFrame       # creates object for Target Application class.    
                            time.sleep(0.2)
                            click_err_cmd = click_scrn_cntr()         # clicks at screen center co-ordinates .  [TaskBar Loc.[x=1151,y=1063]]]
                            time.sleep(ugs_process_delay)      
                            sunawtframe.maximize()      # maximizes 'UGS' Window.
                            sunawtframe.set_focus()     # set focus to 'UGS' window.
                            time.sleep(0.4)   
                            keyboard.press(skey_connect)       # define the shortkey used for 'connect' in UGS to establish connection with arduino on available default COM Port.
                            time.sleep(3.0)
                        keyboard.press(skey_open)             # define the shortkey used for 'open gcode file' in UGS.
                        time.sleep(0.6)
                        keyboard.press('BACKSPACE')                   
                        time.sleep(0.5)
                        pg.typewrite(append_directory+"APND_"+append_filename,0.05)    # writes gcode path on 'UGS import' window.
                        keyboard.press('ENTER')
                        UgsSoundHandler.Beep(3000,500)          
               
            elif (ugs_redir_write == 0 and ugs_redir_append == 0):            #error ♦1024, if no option selected under 'import type' option.
                self.debug(f"Select atleast one importing file type option from 'UGS' tab !")
                return False
                
            elif (ugs_redir_write == 1 and ugs_redir_append == 1):            #error ♦1025, if both the options are selected.
                self.debug(f"Select only one importing file type option in 'UGS' tab !")
                return False  



def click_scrn_cntr():
    try:
        height, width = pg.size()
        x_center = height/2
        y_center = width/2
        pg.click(x_center,y_center,2,1.5,'left')
        csc_err_cmd = 1
        csc_err_cmd = str(csc_err_cmd)
    except:
        csc_err_cmd = 0
        x_center = 0
        y_center = 0
        csc_err_cmd = str(csc_err_cmd)
    return csc_err_cmd
        
#       ----------------------------*Python UGS-Automation-API definition ends here*------------------------------------
