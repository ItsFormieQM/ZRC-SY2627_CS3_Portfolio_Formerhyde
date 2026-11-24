if __name__ == "__main__":
    
    print("dont run it directly")
    raise TypeError("pls run main.py instead")
import os
lang = "en"
text = {}
accounts = []
debug = True
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
langdir = None


