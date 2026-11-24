import localizer
import globalvars
import ext
import methods
localizer.switch_lang("bis.json")
def main():
    hi = localizer.text_setloc("Hello World","placeholder_msg_1")
    print(hi)
if __name__ == "__main__":
    main()