import localizer

localizer.dumptext("test.json")
localizer.switchlang("test.json")
print(localizer.text_setloc("Yo, former!","test1"))