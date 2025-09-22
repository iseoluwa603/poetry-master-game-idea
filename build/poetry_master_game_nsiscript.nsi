# this is the name shown in the installer window title.
# below is the installer file name. the out file 
Name "Poetry Master Game v1.0"
OutFile "PoetryMasterGame_v1.0_Setup.exe"

# This is the default  folder location
InstallDir "$PROGRAMFILES\Poetry Master Game"

# Request for admin rights and privileges 
RequestExecutionLevel admin

# Version Info
VIProductVersion "1.0.0.0"
VIAddVersionKey "ProductName" "Poetry Master Game"
VIAddVersionKey "FileDescription" "Installer for Poetry Master Game"
VIAddVersionKey "CompanyName" "Badipe Iseoluwa"
VIAddVersionKey "LegalCopyright" "© 2025 Badipe Iseoluwa"
VIAddVersionKey "FileVersion" "1.0.0.0"
VIAddVersionKey "ProductVersion" "1.0.0.0"

# Pages for the installer wizard
!include "MUI2.nsh"
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_LANGUAGE "English"

# Installer Section
Section "Install"
    SetOutPath "$INSTDIR"

    ; Copy everything from cx_Freeze output folder
    File /r "exe.win-amd64-3.13\*.*"

    ; Create Start Menu folder + shortcuts
    CreateDirectory "$SMPROGRAMS\Poetry Master Game"
    CreateShortcut "$SMPROGRAMS\Poetry Master Game\Poetry Master Game.lnk" "$INSTDIR\poetry_master_game.exe"
    CreateShortcut "$SMPROGRAMS\Poetry Master Game\Uninstall.lnk" "$INSTDIR\Uninstall.exe"

; Write uninstaller
WriteUninstaller "$INSTDIR\Uninstall.exe"

#To add uninstall information to Windows "Programs and Features"
WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PoetryMasterGame" "DisplayName" "Poetry Master Game v1.0 (by Badipe Iseoluwa)"
WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PoetryMasterGame" "UninstallString" "$INSTDIR\Uninstall.exe"
WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PoetryMasterGame" "Publisher" "Badipe Iseoluwa"
WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PoetryMasterGame" "DisplayVersion" "1.0"
WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PoetryMasterGame" "InstallLocation" "$INSTDIR"
WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PoetryMasterGame" "NoModify" 1
WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PoetryMasterGame" "NoRepair" 1
SectionEnd

; Uninstaller Section
Section "Uninstall"
    ; Remove installed files
    RMDir /r "$INSTDIR"

    ; Remove Start Menu folder
    RMDir /r "$SMPROGRAMS\Poetry Master Game"

    ; Remove uninstall entry from registry
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\PoetryMasterGame"
SectionEnd
