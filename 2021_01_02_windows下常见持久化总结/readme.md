1、基于注册表：  
reg add hkcu\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v test /t reg_sz /d "c:\test.bat -c c:\test.ini"

2、基于第三方程序：  
@echo off
if %processor_architecture%==AMD64 (
    nssm.exe install "Windows DEVDPCJIN GDK" windows.exe
    nssm.exe start "Windows DEVDPCJIN GDK"
)
if %processor_architecture%==x86 (
    nssm-x86.exe install "Windows DEVDPCJIN GDK" windows.exe
    nssm-x86.exe start "Windows DEVDPCJIN GDK"
)

3、基于任务计划：  
schtasks.exe /create /sc onlogon /tn "Update service for Wracle product" /tr "C:\Users\xcblj\a.exe" /f

4、基于服务：  
sc create type= own start=auto binPath= "c:\test.bat -c c:\test.ini"
