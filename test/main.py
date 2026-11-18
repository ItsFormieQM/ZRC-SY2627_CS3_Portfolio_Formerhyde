import localizer

localizer.switch_lang("en.json")
msg = []
print(localizer.text_setloc("Yo, former!","test1"))
print(localizer.text_setloc("You picked up the pieces the lorem ipsum on the ground.","test2"))
msg.append(localizer.text_setloc("Hello!","test3"))
for i in range(len(msg)):
    print(msg[i])