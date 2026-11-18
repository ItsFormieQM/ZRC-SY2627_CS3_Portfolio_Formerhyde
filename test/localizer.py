from pathlib import Path
import json
import globalvars as globalv

def dumptext(jsonname):
    txt = {}
    jsonname = f"lang/{jsonname}"
    json_ex = Path(jsonname)
    if not json_ex.exists() and json_ex.is_file():
        print(f"error, {jsonname} not found!")
        raise FileNotFoundError
    else:
        
        with open(f"{jsonname}","r",encoding="utf-8") as file:
            txt = json.load(file)
        globalv.text = txt
def text_setloc(entxt,translkey):
    if globalv.lang == "en":
        return entxt
    else:
        try:
            return globalv.text[translkey]
        except KeyError:
            return "missing!"
def switchlang(jsonname):
    actualstr = ""
    for i in range(len(jsonname)):
        if jsonname[i] == ".":
            break
        actualstr += jsonname[i]
    globalv.lang = actualstr
    dumptext(jsonname)
def gettext(translkey):
    return globalv.text
if __name__ == "__main__":
    print("dont run this directly, just import")
    raise TypeError