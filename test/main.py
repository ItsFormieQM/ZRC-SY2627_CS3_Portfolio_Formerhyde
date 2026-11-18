import localizer

localizer.switch_lang("bis.json")
msg = []
msg.append(localizer.text_setloc(
    "You know. I used to hardcode my text before. But now that I started game dev. I've changed for the better. Hehehe",
    "test3"
))
for i in range(len(msg)):
    print(msg[i])