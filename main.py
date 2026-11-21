from localizer import *
from ext import clamp
from globalvars import *
from methods import *
while True:
    
    msg = []
    class Account:
        def __init__(self,name,age,pin):
            self.name = name
            self.age = age
            self.pin = pin
        pass
    cmds = [
        text_logic_setloc("Exit","ui_exit","Exit"),
        text_logic_setloc("Switch Language","ui_sellang","Switch_Language"),
        text_logic_setloc("Clear Terminal","ui_clear", "Clear"),
        text_logic_setloc("Run Custom Code","ui_ccode","ev")
    ]
    if debug:
        cmds.append(text_logic_setloc("Push changes to GitHub","ui_debug_push","Push"))
    print(text_setloc("---Bank with OOP + translation---","intro_1"))
    def execute_ind(indnum):
        if indnum >= len(cmds) or indnum < 0:
            print("Command doesn't exist!\n")
            return
        print(f"{text_setloc("Selected", "selected")} {cmds[indnum][0]}")
        eval(cmds[indnum][2] + "()")
    print(text_setloc("Command List","cmdls_1"))
    for i in range(len(cmds)):
        print(f"{i+1}. {cmds[i][0]}")
    
    ind = int(input(text_setloc("Enter your index: ","indexsel_1")))-1
    execute_ind(ind)
