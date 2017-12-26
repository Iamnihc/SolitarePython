from solitairebasics import *
from time import sleep
def enable():
    aion=0
    while aion==0:
        ans = input("Enable PyAi?")
        if ans.lower()[0] == "y":
            aion = True
            return True
        else:
            aion = False
            return False


def aichoose(deck, finalarr, midarr, fromto):
    fromcard="N"
    finalcards=[]
    for i in finalarr:
        finalcards.append(i[-1])
    nextfinal=[]
    for i in finalcards:
        if len(i) > 1:
            nextnum=str(int(findnum(i))+1)
            suite=str(findsuite(i))
            nextcard=nextnum+suite
            nextfinal.append(nextcard)
    if str(findnum(deck[-1])) == "1":
        fromcard="0"
        tocard=str(lettersuit(deck[-1]))
    for stack in midarr:
        if len(stack)>1:
            print("checking card "+stack[-1])
            sleep(.1)
            # What to do if you cant do something
            # Find any empty stacks
            if stack[-1].__class__ is int:
                print(deck[-1])
                print("Empty Stack at "+ str(stack[-1]))
                if deck[-1][0] == "K":
                    print("Found king to move")
                    sleep(.5)
                    fromcard == "0"
                    tocard=str(stack+1)
                for couldbeking in midarr:
                    # If you find a king in the piles:
                    if couldbeking[-1][0] == "K":
                        fromcard=str(couldbeking+1)
                        tocard=str(stack+1)
                        print("Found king to move")
            #if it is a 1 (ace)
            elif stack[-1][0] == "1":
                fromcard=str(midarr.index(stack)+1)
                tocard=str(lettersuit(stack[-1]))
            # If it is the next card in final stacks
            elif stack[-1] in nextfinal :
                movecard=stack[-1]
                tocard = str(lettersuit(movecard))
                fromcard = str(midarr.index(stack) + 1)
            #if you can move a card from the deck
            elif deck[-1] in nextfinal:
                movecard=deck[-1]
                tocard=str(lettersuit(movecard))
                fromcard="0"
            elif checkplace(stack[-1],deck[-1]):
                fromcard=str(deck[0])
                tocard=str(stack[0])
            #check if you can move a card from the midstacks
            else:
                for i in range(1,6):
                    if stack!=midarr[i] and checkplace(stack[-1],midarr[i][-1]):
                        tocard=str(stack[0])
                        fromcard=str(i+1)
                        numcards=1
                        fromto

    if fromcard == "N":
        print("No moves found, Choosing Next card")
    if fromto=="F":
        print("output: "+fromcard)
        return fromcard
    elif fromto=="N":
        return str(numcards)
    else:
        print("output:"+tocard)
        return tocard

def findtransfer():
    pass