#// wrapper cuz idk
def sdm(inp):
    print(inp)
def str_canbeint(inp):
    try:
        inp = str(inp)
        return True
    except ValueError:
        return False    
def sign(number):
    if number < 0:
        return -1
    elif number == 0:
        return 0
    elif number > 0:
        return 1
    else:
        raise Exception
def str_toarray(inp):
    temparr = []
    for i in range(len(inp)):
        temparr.append(inp[i])   
    return temparr 
def instance_exists(object):
    try:
        print(object)
        return True
    except NameError:
        return False