import subprocess

def open_notepad():
    subprocess.Popen("notepad.exe")

def open_calculator():
    subprocess.Popen("calc.exe")

def open_explorer():
    subprocess.Popen("explorer.exe")

def open_control():
    subprocess.Popen("control.exe")

def open_task():
    subprocess.Popen("taskmgr.exe")

def open_cmd():
    subprocess.Popen("cmd.exe")

def open_snip():
    subprocess.Popen("snippingtool.exe")

def open_word():
    subprocess.Popen("winword.exe")
    
def open_paint():
    subprocess.Popen("mspaint.exe")

def open_chrome():
    subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

def open_excel():
    subprocess.Popen(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")

def open_powerpoint():
    subprocess.Popen(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")