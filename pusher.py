import os 
from datetime import datetime
from pathlib import Path
#// pusher
def log():
    rn = datetime.now()
    rn = rn.strftime("%B %d, %Y and %I:%M:%S %p")
    fp = Path("history.txt")
    if fp.is_file():
        print("test")
        with open("history.txt","a") as file:
            file.write(f"\nProgram ran with date: {rn}")
    else:
        with open("history.txt","w") as file:
            file.write(f"Program ran with date: {rn}")
try:
    log()
    os.system("git add .")
    msg = input("Enter commit message: ")
    if msg:
        os.system(f"git commit -m \"{msg}\"")
    else:
        os.system("git commit -m \"Auto push\"")
    os.system("git push")
    os.system("cls")
    print("worked")
except Exception:
    log()
    fp = Path("history.txt")
    if fp.is_file():
        print("test")
        with open("history.txt","a") as file:
            file.write(f" - FAILED")
    print("Something went wrong. Press Enter to Abort")
    input("")
