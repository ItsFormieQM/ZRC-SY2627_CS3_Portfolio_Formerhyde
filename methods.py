from os import system
from localizer import *
from globalvars import *
if __name__ == "__main__":
    print("pls dont run")
    raise TypeError("run main.py instead")
def account_creator():
    pass
def Exit():
    print("Exiting...")
    exit()
def Clear():
    system("clear")
    system("cls")
def Push():
    os.system("python push_auto.py")
    exit()
def strlenny():
    inp = input("Enter string: ")
    print(f"The length for this string is: {len(inp)}")
    print(f"The length for this string with spacing excluded is: {len(inp.replace(" ",""))}")
def Switch_Language():
    __lang = [
        "en.json",
        "bis.json"
    ]
    print("1. English")
    print("2. Bisaya Cebuano")
    ind = int(input(text_setloc("Select language: ","langsel_1"))) -1
    switch_lang(__lang[ind])
    print(text_setloc(f"Language set to","langsel_2")+" "+lang)
    pass
