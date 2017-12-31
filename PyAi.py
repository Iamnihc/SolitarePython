from solitairebasics import *
from time import sleep
global delay
delay=0
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


def aichoose(deck, finalarr, midarr,revarr, fromto,lastcard):
    fromcard="N"
    finalcards=[]
    for i in finalarr:
        finalcards.append(i[-1])
    nextfinal=[]
    for i in finalcards:
        if len(i) > 1:
            nextnum=str(convertletter(int(findnum(i))+1))
            suite=str(findsuite(i))
            nextcard=nextnum+suite
            nextfinal.append(nextcard)
    # move aces from the deck
    if len(deck)>1 and str(findnum(deck[-1])) == "1":
        fromcard="0"
        tocard=str(lettersuit(deck[-1]))

    for stack in midarr:
        if len(stack)>1:
            print("checking card "+stack[-1])
            sleep(delay)
            # What to do if you cant do something
            # Find any empty stacks
            if stack[-1].__class__ is int:
                print("Empty Stack at "+ str(stack[-1]))
                if len(deck)>1 and deck[-1][0] == "K":
                    print("Found king to move")
                    sleep(delay)
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
            elif len(deck)>1 and deck[-1] in nextfinal:
                movecard=deck[-1]
                tocard=str(lettersuit(movecard))
                fromcard="0"
            elif len(deck)>1 and checkplace(stack[-1],deck[-1]):
                fromcard=str(deck[0])
                tocard=str(stack[0])
            #check if you can move a card from the midstacks
            else:
                # Try to find a card stack to move
                for i in range(0,6):
                    #Find the first card revealed
                    firstrevealed = midarr[i][-1*revarr[i]]
                    #if it you arent checking the same stack, it is not empty, it wasnt the last move, and it is valid

                    if stack!=midarr[i] and (len(midarr[i])> 1) and firstrevealed != lastcard and checkplace(stack[-1],firstrevealed):
                        #Set each output to its respective value
                        tocard = str(stack[0])
                        fromcard = str(i+1)
                        numcards=revarr[i]
                    elif len(midarr[i]) > 1:
                        pass

        #You have an empty stack- Place a king
        else:
            if len(deck)>1 and deck[-1][0] == "K":
                fromcard = "0"
                tocard = str(stack[0])
                print("Found king to move: Deck")
            for i in midarr:
                if i != stack and len(i) > 1:
                    teststack = midarr[i[0]-1]
                    #make the first revealed card
                    firstrevealed = (teststack)[len(teststack)-revarr[i[0]-1]]
                    if firstrevealed[0] == "K" and teststack[1] is not firstrevealed:
                        print("Found a king in stack", i[0])
                        fromcard = str(i[0])
                        tocard = str(stack[0])
                        numcards = str(revarr[i[0]-1])

    if fromcard == "N":
        print("No moves found, Choosing Next card")
    if fromto=="F":
        print("output: "+fromcard)
        return fromcard
    elif fromto=="N":
        print("moving "+str(numcards)+" Cards")
        return str(numcards)
    else:
        print("output:"+tocard)
        return tocard
