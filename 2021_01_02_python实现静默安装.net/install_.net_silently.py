import _winreg
import subprocess

def main():
    try:
        target_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Client");
    except WindowsError:
        subprocess.call(["dotNetFx40_Client_setup.exe", "/q", "/norestart"]);

if __name__ == "__main__":
    main()
