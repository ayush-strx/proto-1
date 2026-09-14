import os
import glob
import difflib
import subprocess

# Windows ke built-in apps jo Start Menu mein shortcut nahi rakhte
BUILTIN_APPS = {
    # Basic tools
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "command prompt": "cmd.exe",
    "terminal": "wt.exe",
    
    # File/System management
    
    "file explorer": "explorer.exe",
    "task manager": "taskmgr.exe",
    "control panel": "control.exe",
    "explorer": "explorer.exe",
    
    # Accessibility/Utility
    "snipping tool": "snippingtool.exe",
    "magnifier": "magnify.exe",
    "sticky notes": "stikynot.exe",
    
    # Media
    "volume mixer": "sndvol.exe",
    
    # Settings
    "settings": "ms-settings:",
}


def scan_installed_apps():
    """Start Menu se saare app shortcuts scan karta hai"""
    apps = {}
    
    start_menu_paths = [
        os.path.join(os.environ["ProgramData"], "Microsoft", "Windows", "Start Menu", "Programs"),
        os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs"),
    ]
    
    for path in start_menu_paths:
        for shortcut in glob.glob(os.path.join(path, "**", "*.lnk"), recursive=True):
            app_name = os.path.splitext(os.path.basename(shortcut))[0]
            apps[app_name.lower()] = shortcut
    
    return apps


# Program start hote hi ek baar scan ho jayega
installed_apps = scan_installed_apps()


def find_and_open_app(app_name):
    app_name = app_name.lower().strip()
    
    # Step 1: Built-in Windows apps mein exact match
    if app_name in BUILTIN_APPS:
        target = BUILTIN_APPS[app_name]
        if target.startswith("ms-settings:") or target.endswith(".msc") or target.endswith(".cpl"):
            os.system(f"start {target}")
        else:
            subprocess.Popen(target)
        return f"Opening {app_name}."
    
    # Step 2: Start Menu shortcuts mein exact match
    if app_name in installed_apps:
        os.startfile(installed_apps[app_name])
        return f"Opening {app_name}."
    
    # Step 3: SUBSTRING match - "microsoft" jaise generic words ke liye
    substring_matches = [name for name in installed_apps.keys() if app_name in name]
    
    if len(substring_matches) == 1:
        os.startfile(installed_apps[substring_matches[0]])
        return f"Opening {substring_matches[0]}."
    elif len(substring_matches) > 1:
        options = ", ".join(substring_matches)
        return f"I found multiple matches: {options}. Please be more specific."
    
    # Step 4: Fuzzy match - typos/spelling mistakes ke liye (jab substring match na mile)
    matches = difflib.get_close_matches(app_name, installed_apps.keys(), n=3, cutoff=0.7)
    
    if len(matches) == 1:
        os.startfile(installed_apps[matches[0]])
        return f"Opening {matches[0]}."
    elif len(matches) > 1:
        options = ", ".join(matches)
        return f"I found multiple matches: {options}. Please be more specific."
    
    # Step 5: Built-in apps mein fuzzy match
    builtin_matches = difflib.get_close_matches(app_name, BUILTIN_APPS.keys(), n=1, cutoff=0.7)
    if builtin_matches:
        best_match = builtin_matches[0]
        subprocess.Popen(BUILTIN_APPS[best_match])
        return f"Opening {best_match}."
    
    return f"Sorry, I couldn't find an app called {app_name}."