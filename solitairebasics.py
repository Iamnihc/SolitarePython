from random import randint



def assign(mfrom, mto, numb):
    for i in range(0, numb):
        move=randint(0, len(mfrom)-1)
        mto.append(mfrom[move])
        mfrom.pop(move)


def checkres():
    responce = input("Pick a stack:")
    if len(responce) == 1:
        if responce == "C" or responce == "H" or responce == "S" or responce == "D" or responce == "N":
            return responce
        if responce.isdigit():
            return int(responce)


def findsuite(card):
    return card[-1]


def color(card):
    if findsuite(card) == "♡" or findsuite(card) == "♢":
        return "red"
    else:
        return "black"


# Finds the rules
def checkplace(topcard, newtop):
    if topcard[0] =="K":
        topcard="13"+topcard[1]
    if topcard[0] =="Q":
        topcard="12"+topcard[1]
    if topcard[0] =="J":
        topcard="11"+topcard[1]
    if topcard[0] =="T":
        topcard="10"+topcard[1]
    if newtop[0] =="K":
        newtop="13"+newtop[1]
    if newtop[0] =="Q":
        newtop="12"+newtop[1]
    if newtop[0] =="J":
        newtop="11"+newtop[1]
    if newtop[0] =="T":
        newtop="10"+newtop[1]
    topval=(int(topcard[:-1])-1)
    newval=(int(newtop[:-1]))
    print(topval)
    print(newval)
    print(topcard[1])
    print(color(topcard))
    print(color(newtop))
    if not topcard is int:
        if topval==newval and color(topcard) != color(newtop):
            print("works")
            return True
        else:
            return False
    else:
        print("this doesnt work yet")
        return False



def checkfinal(array, newtop):
    topcard=array[-1]
    if topcard[0] =="K":
        topcard="13"+topcard[1]
    if topcard[0] =="Q":
        topcard="12"+topcard[1]
    if topcard[0] =="J":
        topcard="11"+topcard[1]
    if topcard[0] =="T":
        topcard="10"+topcard[1]
    if newtop[0] =="K":
        newtop="13"+newtop[1]
    if newtop[0] =="Q":
        newtop="12"+newtop[1]
    if newtop[0] =="J":
        newtop="11"+newtop[1]
    if newtop[0] =="T":
        newtop="10"+newtop[1]
    print(topcard)
    print(newtop)
    if len(array)>1:
        if len(topcard)==2:
            topval = (int(topcard[0]))
            newval = (int(newtop[0]))
        if len(topcard)==3:
            topval = (int(topcard[0,2]))
            newval = (int(newtop[0,2]))
        if not topcard == "":
            if topval==newval-1 and findsuite(topcard) == findsuite(newtop):
                return True
            else:
                return False
    else:
        if newtop[0]=='1':
            return True
        else: return False



def replace(changearray, pos,valin):
    changearray.pop(pos)
    changearray.insert(pos, valin)


def addarray(changearray, pos):
    val=changearray[pos]
    replace(changearray,pos, val+1)


def haswon(final):
    for i in final:
        if len(i) != 14:
            return False
    return True