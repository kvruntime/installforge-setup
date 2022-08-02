# InstallForgeSetup

freeze python application & build a window setup

## Purpose
- freeze python application  
- use installforge to create an installer  
- installed application is set to winreg  
- application recognize some kinds of extensions (*.dap, etc.)  
- application can be lanched from recognized extensions files
- recognized files have application icon
 

## Tools
- python
- installforge

## How
using essentially windows registry files.  

- HKEY_CLASS_/.dap/[key]dapfile (the .dap extension have key that point to dapfile subkey)  

- dapfile (the dapfile subkey contains the folowing keys)  
   1. DefaultIcon/[key] -> /file.exe (main.exe app or any icon)
   2. shell/open/command/[key] -> /file.exe (the main.exe or any other command)
