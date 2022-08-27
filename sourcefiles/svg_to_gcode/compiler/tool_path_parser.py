# [Part of GCODE-MAKER-3.0 Extension Pack]

# tool_path_parser.py

# path = C:\Users\%username%\AppData\Roaming\inkscape\extensions\svg_to_gcode\compiler\
# href = svg_to_gcode.compiler.tool_path_parser

# pre-defined tool path system location :
# header = '\\AppData\Roaming\inkscape\extensions\svg_to_gcode\tool_paths\user_path_header.txt'
# footer = '\\AppData\Roaming\inkscape\extensions\svg_to_gcode\tool_paths\user_path_footer.txt'

''' NOTE : When compiler unable to find gcode file for tool path header and footer, it will check 
for pre-defined files and if unable to find those too, it will create automatically at the above 
respective system locations. You can go edit the file as you want. 

NB : Define appropriate gcode command for taking a pen and keeping it back in two different files
[user_path_header.txt] and [user_path_footer.txt] as mentioned. 

vishnus_technologies (C) will not be responsible for further editing in this file, if they harm or spoil your
printer at any cost  '''

# (C)2021 vishnus_technologies, tool_path_parser.py

''' This page contain pre-defined paths for different colored pens, 
    you can change the respective gcode of each colored pen with 
    respect to the pen's position. '''


import os 
import time 
import warnings

_username = os.getenv('username')
_appdata = os.getenv('APPDATA').replace('\\', '/')

# for header [takes pen from respective place]
# htp : 'header tool path'

def htp(self, _tp1_head, _color, _gcodef_head, _attach_cus_file): 
    add_header_comments = '''(# Default page for custom tool path gcode )
    
(# Default custom pen path gcode starts here [user_path_header.txt].)
(# Moves to a respective pen's location to take it before writing.) '''  

    # respective colored pen's gcode definition goes here:
    none_path = ['(takes no pen [use current pen])']
    black_path = ['(take black pen)']
    blue_path = ['(take blue pen)']
    red_path = ['(take red pen)']
    green_path = ['(take green pen)']
    custom_pen_path = [_tp1_head+"\n"]
    usrdef_path = []
   
    pre_path = f"{_appdata}/inkscape/extensions/svg_to_gcode/tool_paths/user_path_header.txt"
    if os.path.isfile(_gcodef_head):
        work_dir = _gcodef_head
    elif os.path.isfile(pre_path):
        work_dir = pre_path
    else:
        cr = open(pre_path, 'w')
        cr.write(add_header_comments)
        cr.close()
        work_dir = pre_path
        self.debug(f"File not found. File created automatically.\nAdd a valid gcode at this recently created file.\n[svg_to_gcode/tool_paths/user_path_header.txt]")
        
    with open(work_dir, 'r') as read_cust_gcode:
        read_cust_gcode.seek(46)
        custom_gcode_path = read_cust_gcode.read().splitlines()
        
    if _attach_cus_file:
        usrdef_path = custom_gcode_path
    else:
        usrdef_path = custom_pen_path
        usrdef_path = custom_pen_path
    
    if _color == "none":
        return none_path
    elif _color == "black":
        return black_path
    elif _color == "blue":
        return blue_path
    elif _color == "red":
        return red_path
    elif _color == "green":
        return green_path
    elif _color == "usrdef":
        return usrdef_path
    
    
# ---------------------------------------------------------------------------------------------------------------------


# for footer [keeps pen back at respective place]
# ftp : 'footer tool path'

def ftp(self, ret_tp1_foot, ret_color, ret_gcodef_foot, ret_attach_cus_file):         
    add_footer_comments = '''(# Default page for custom tool path gcode )
    
(# Default custom pen path gcode starts here [user_path_footer.txt])
(# Moves to the respective pen's location to keep it after writing.) '''

    # respective colored pen's gcode definition goes here:
    _none_path = ['(return no pen [go home with same pen]])']
    ret_black_path = ['(keep black pen back)']
    ret_blue_path = ['(keep blue pen back)']
    ret_red_path = ['(keep red pen back)']
    ret_green_path = ['(keep green pen back)']
    ret_custom_pen_path = [ret_tp1_foot+"\n"]
    ret_usrdef_path = []

    pre_path1 = f"{_appdata}/inkscape/extensions/svg_to_gcode/tool_paths/user_path_footer.txt"
    if os.path.isfile(ret_gcodef_foot):
        _work_dir = ret_gcodef_foot
    elif os.path.isfile(pre_path1):
        _work_dir = pre_path1
    else:
        crr = open(pre_path1, "w")
        crr.write(add_footer_comments)
        crr.close()
        _work_dir = pre_path1
        self.debug(f"File not found. File created automatically.\nAdd a valid gcode at this recently created file.\n[svg_to_gcode/tool_paths/user_path_footer.txt]")
    
    with open(_work_dir, 'r') as _read_cust_gcode:
        _read_cust_gcode.seek(46)
        ret_custom_gcode_path = _read_cust_gcode.read().splitlines()
            
    if ret_attach_cus_file:
        ret_usrdef_path = ret_custom_gcode_path
    else :
        ret_usrdef_path = ret_custom_pen_path
        
    if ret_color == "none":
        return _none_path
    elif ret_color == "black":
        return ret_black_path
    elif ret_color == "blue":
        return ret_blue_path
    elif ret_color == "red":
        return ret_red_path
    elif ret_color == "green":
        return ret_green_path
    elif ret_color == "usrdef":
        return ret_usrdef_path


# --------------------------------------------------------------------------------------------------------------------

def check_for_readme():
    readme_loc = f"{_appdata}/inkscape/extensions/svg_to_gcode/tool_paths/readme.txt"
    readme_text = '''# THIS IS AN INFORMATION FILE BASED ON TOOL PATH [FOR COLORED PENS] *BETA

# NOTE : When compiler unable to find gcode file for tool path header and footer, it will check 
# for pre-defined files and if unable to find those too, it will create automatically at the above 
# respective system locations. You can go edit the file as you want. 
# NB : Define appropriate gcode command for taking a pen and keeping a pen back in two different files
# [user_path_header.txt] and [user_path_footer.txt] as mentioned. 

---------------------------------------------------------------------------------------------------------------

# user_path_header.txt 
# custom pen path gcode file [header] 
# This gcode is for moving to a respective pen to take it before writing. 
# [ONLY DEFINE GCODE FOR TAKING PEN BEFORE WRITING WITH IT] 


---------------------------------------------------------------------------------------------------------------

# user_path_footer.txt 
# custom pen path gcode file [footer] 
# This gcode is for moving to a respective pen to take it before writing. 
# [ONLY DEFINE GCODE FOR KEEPING PEN BACK AFTER WRITING WITH IT] 

---------------------------------------------------------------------------------------------------------------

# vishnus_technologies(C)2021 will not have any responsibilities for any 
  dis-functionality happened to your machine.\n\n\n\n''' 
    readme_text_abstracts = '''Abstracts:-
# Last updated with : Windows OS
# Platform ID : ABU975:405.12
# Last updated on : '''
   
    if not os.path.isfile(readme_loc):
        cr_readme = open(readme_loc, "w")
        cr_readme.write(readme_text+readme_text_abstracts+time.strftime("%d-%h-%Y")+time.strftime("  %I:%M %p"))
        cr_readme.close()
    
    
# --------------------------------------------------------------------------------------------------------------------

# Abstracts :- 
# Last updated with : Windows OS
# Platform ID : ABU975:405.12
# Last updated on : 21.08.2021 08:49PM