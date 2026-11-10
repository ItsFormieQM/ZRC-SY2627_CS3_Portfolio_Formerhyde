import os 
from datetime import datetime
#// pusher
try:
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
    print("Something went wrong. Press Enter to Abort")
    input("")
finally:
    rn = datetime.now()
    with open("history.txt","w") as file:
        file.write(f"\nProgram ran with date: {rn}")