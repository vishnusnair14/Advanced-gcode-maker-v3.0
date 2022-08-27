; [Part of GCODE-MAKER-3.0 Extension Pack]

; Script for generating windows MSI.  
; [ packs everything together ]
; Last code updated on : 02/05/2022 | 08:30PM

#define MyAppName "Gcode-Maker-3.0"                                                                                  
#define MyAppVersion "3.0"
#define MyAppPublisher "vishnus_technologies"
#define MyAppURL "https://www.vishnus_technologies.co.in"                                                                                
#define DesktopCore "C:\Users\Lilly\Desktop\GcodeMakerUserFile_V3"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
; [ DO NOT ALTER BELOW CONSTANTS ]
AppId={{3DD00BE7-24F2-415B-8E92-477F80412CCF}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf64}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
CloseApplications=yes
LicenseFile={#DesktopCore}\_setupfiles\licenseFile.txt
InfoBeforeFile={#DesktopCore}\_setupfiles\beforeInfoFile.txt
InfoAfterFile={#DesktopCore}\_setupfiles\afterInfoFile.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir={#DesktopCore}\_build
OutputBaseFilename=GM3_setup
SetupIconFile={#DesktopCore}\_setupfiles\logo_gm.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern
WindowResizable=yes
WizardSizePercent=100,100
WizardImageFile={#DesktopCore}\_setupfiles\WizImg.bmp
WizardImageStretch=yes
AppReadmeFile={app}\readme.txt
Password=2022 
Encryption=yes
ArchitecturesInstallIn64BitMode=x64 arm64
UninstallDisplayIcon={app}\logo.ico
UninstallDisplayName="GcodeMaker3.0 (x64bit)"
UninstallRestartComputer=yes
AppComments="An Inkscape extension for 2D plotters. (c)2022 vishnus_technologies.org"

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Components]
Name: "custinkp"; Description: "Install Inkscape v1.1-x64 [Installer]"; Types: full compact 
Name: "custugs"; Description: "Install UGS Platform-[Dec 02 2021] [Portable]"; Types: full  

[Files]
Source: "{#DesktopCore}\sourcefiles\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#DesktopCore}\sourcefiles\src\*"; DestDir: "C:\Users\{username}\AppData\Roaming\inkscape\extensions"; Flags: ignoreversion recursesubdirs createallsubdirs
;Source: "D:\FILE  ACCESSORIES\software SETUPS\inkscape-1.1-x64.exe"; DestDir:"{app}\softwares\Inkscape-v1.1-[installer-x64]"; Components: custinkp
;Source: "C:\Program Files\ugsplatform-win-2.0.7\*"; DestDir:"{app}\softwares\UGS-Platform-v2.0.7-[portable-x64]"; Components: custugs; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"

[Run]
Filename: "python.exe"; Description: "Run extension configuration script [required]"; Parameters: "Inkp_config.py"; WorkingDir: "{app}"; Flags: shellexec postinstall waituntilterminated
Filename: "{app}\GcodeMaker-3.0_UserManual.pdf"; Description: "View software manual"; Flags: shellexec postinstall runascurrentuser 

[UninstallRun]
Filename: "{app}\Run-pkg_uninstaller.bat"; RunOnceID:"Uninstallgm2" ; Flags: runascurrentuser shellexec waituntilterminated

