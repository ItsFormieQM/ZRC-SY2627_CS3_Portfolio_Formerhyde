import os 
#// pusher
try:
    os.system("git add .")
    msg = input("Enter commit message: ")
    if msg:
        os.system(f"git commit -m \"{msg}\"")
    else:
        os.system("git commit -m \"Auto push\"")
except Exception:
    print("Something went wrong. Press Enter to Abort")
    input("")