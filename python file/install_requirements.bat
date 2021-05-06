@echo off  


if not exist "C:\Users\Public\JunkFileCleaner" mkdir "C:\Users\Public\JunkFileCleaner"
if not exist "C:\Users\Public\JunkFileCleaner\Cleaner.py" ( copy "%cd%\Cleaner.py" "C:\Users\Public\JunkFileCleaner\Cleaner.py" >nul )
if not exist "C:\Users\Public\JunkFileCleaner\install_requirements.bat" ( copy "%cd%\install_requirements.bat" "C:\Users\Public\JunkFileCleaner\install_requirements.bat" >nul )

      
:: BatchGotAdmin        
:-------------------------------------        
REM  --> Check for permissions  
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"  
REM --> If error flag set, we do not have admin.  
if '%errorlevel%' NEQ '0' (    echo Requesting administrative privileges...    goto UACPrompt) else ( goto gotAdmin )  
:UACPrompt  
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"  
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"  
    "%temp%\getadmin.vbs"  
    exit /B
:gotAdmin  


:: To install Python Libraries
pip install psutil
pip install colored


echo .
echo .
echo .
echo Installing Libraries successful...

cd "C:\Users\Public\JunkFileCleaner"

python Cleaner.py
pause

