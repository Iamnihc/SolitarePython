from random import randint

def assign(mfrom, mto, numb):
    for i in range(0, numb):
        move = randint(0, len(mfrom)-1)
        mto.append(mfrom[move])
        mfrom.pop(move)

def convertnum(convertin):
    convertin=str(convertin)
    if convertin[0] == "K":
        convertin = "13"+convertin[1]
    if convertin[0] == "Q":
        convertin = "12"+convertin[1]
    if convertin[0] == "J":
        convertin = "11"+convertin[1]
    if convertin[0] == "T":
        convertin = "10"+convertin[1]
    return convertin

def convertletter(convertin):
    convertin = str(convertin)
    if convertin == "13":
        convertin = "K"
    if convertin == "12":
        convertin = "Q"
    if convertin == "11":
        convertin = "J"
    if convertin == "10":
        convertin = "T"
    return convertin

def checkres(responce):
    while True:
        if responce != "":
            responce = responce.upper()
            while responce.__class__ is not str:
                responce=input("Try again")
            else:
                if len(responce) == 1:
                    # Filter the valid letter responces
                    if responce == "C" or responce == "H" or responce == "S" or responce == "D" or responce == "N" or responce == "A":
                        # return true, exit the loop
                        return responce
                    # Rerun if the responces are not integers at this point
                    elif not responce.isdigit():
                        # breaks out of the loop by using this positon
                        responce = False
                    elif int(responce)<7:
                        return int(responce)
                else:
                    responce = False


def findsuite(card):
    return card[-1]


def color(card):
    if findsuite(card) == "♡" or findsuite(card) == "♢":
        return "red"
    else:
        return "black"


# Finds the rules
def checkplace(topcard, newtop):
    topcard=convertnum(str(topcard))
    newtop=convertnum(newtop)
    if topcard == "EMPTY" or topcard.__class__ is int:
        if newtop[0:2] == "13":
            return True
    elif not topcard.isdigit():
        topval = (int(topcard[:-1])-1)
        newval = (int(newtop[:-1]))
        if topcard is not int:
            if topval == newval and color(topcard) != color(newtop):
                return True
            else:
                return False

def findnum(card):
    card=convertnum(card)
    if len(card) == 2:
        val = (int(card[0]))
    if len(card) == 3:
        val = (int(card[0]+card[1]))

    return val


def lettersuit(card):
    if findsuite(card) == "♣":
        return "C"
    if findsuite(card) == "♡":
        return "H"
    if findsuite(card) == "♠":
        return "S"
    if findsuite(card) == "♢":
        return "D"


def checkfinal(array, newtop):
    topcard = array[-1]
    topcard=convertnum(topcard)
    newtop=convertnum(newtop)
    if len(array) > 1:
        topval= findnum(topcard)
        newval=findnum(newtop)
        if not topcard == "":
            if topval == newval-1 and findsuite(topcard) == findsuite(newtop):
                return True
            else:
                return False
    else:
        if newtop[0] == '1' and lettersuit(newtop)==array[0]:
            return True
        else:
            return False


def replace(changeArray, pos, changeByVal):
    valIn=changeArray[pos]+changeByVal
    changeArray.pop(pos)
    changeArray.insert(pos, valIn)


# Add one to a value on an arrary

# Check if the player has won yet-
def haswon(final):
    # Do you have 14 cards in each final stack
    for i in final:
        if len(i) != 14:
            # if you dont have 14 in any of the piles return False
            return False
    # Otherwise return True
    return True

def tryagain():
    keepgoing=input("Try again?")
    if keepgoing[0].lower()=="y":
        return True
    else:
        return False

