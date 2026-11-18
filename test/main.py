import localizer

localizer.switch_lang("bis.json")
localizer.reset_lang()
print(localizer.text_setloc("Yo, former!","test1"))
print(localizer.text_setloc("You picked up the pieces the lorem ipsum on the ground.","test2"))