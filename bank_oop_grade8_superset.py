import os
from wrappers import *
class Account_Normal:
    def __init__(self,name,age,pin):
        self.pin = pin
        self.name = name
        self.age = name
accounts = []
available_cmd = {
    0:"Exit",
    1:"Create Account",
}
def createacc_seq():
    usr = None
    age = 0
    pin = None
    while True:
        print("---Account Maker---")
        usr = input("Enter username: ")

        while True:
            try:

                age = int(input("Enter age: "))
                break
            except ValueError:
                print("Please input a whole number")
        while True:
            try: 
                pin = int(input("Enter PIN: "))
                break
            except ValueError:
                print("Please input whole numbers")

        acc = Account_Normal(usr,age,pin)
        accounts.append(acc)
        print("Account created!")
        break

    pass
def list_cmd():
    for i,j in available_cmd.items():
        print(f"{i}. {j}")
def execute_cmd(inp):
    ind = -666
    try:
        ind = int(inp)
    except ValueError:
        print("error")
        return
    match ind:
        case 0:
            exit()
        case 1:
            createacc_seq()
        case _:
            exit(-66)


def show_intro():
    print("---Bank with OOP i guess---")
    print("Author: Formerhyde - Lead Developer of Experience")
    list_cmd()
    while True:
        usp = input("Enter Index: ")
        execute_cmd(usp)
def main_seq():
    show_intro()

    pass
if __name__ == "__main__":
    main_seq()
    pass