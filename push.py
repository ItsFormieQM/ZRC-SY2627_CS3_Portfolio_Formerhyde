import os
from pathlib import Path
from datetime import datetime

now = datetime.now()

# ripped straight from my game
if False:

    try:

        print("lock removed")
        pass
    except Exception as e:
        if type(e) is FileNotFoundError:
            print("removed already")
        elif type(e) is PermissionError:
            print("close ur ide. if its closed welp smth is locking it or os issue")
        else:
            print("welp u got a big issue")
        pass
    finally:
        print("executing stuff")
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        os.system("git add .")
        msg = input("Enter commit message: ")
        if msg == "":
            msg = "Automated by the Python Script"
        os.system(f'git commit -m "{msg}"')
        os.system("git push origin Chapter-1 --force ")


if True:
    try:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        commit = input("Enter commit message: ")

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
