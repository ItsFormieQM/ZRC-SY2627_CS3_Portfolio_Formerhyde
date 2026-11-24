import os
from pathlib import Path
from datetime import datetime

now = datetime.now()

# ripped straight from my game
# take that **** out
if True:
    try:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        commit = "Pushed via main.py"

        lognamefile = "logs/pushlogs/log.txt"
        check_txtlog = Path(f"{lognamefile}")
        if check_txtlog.is_file() and check_txtlog.exists():
            with open(lognamefile, "a") as file:
                file.writelines(f"TIME: {now} - Success\n")
        else:
            with open(lognamefile, "w") as file:
                file.writelines(f"TIME: {now} - Success\n")
    except Exception:
        if check_txtlog.is_file() and check_txtlog.exists():
            with open(lognamefile, "a") as file:
                file.writelines(f"TIME: {now} - Fail\n")
        else:
            with open(lognamefile, "w") as file:
                file.writelines(f"TIME: {now} - Fail\n")

    finally:
        os.system("git add .")
        os.system(f"git commit -m \"{commit}\"")
        os.system("git push")
        print("\npushed successfully")
