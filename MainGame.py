from random import randint
def pickcard():
    fromstack=checkres()
    fcard=False
    # if the card exists, pick it
    # is the stack a number (Non 0)?
    if fromstack.__class__ is int:
        fromstack=int(fromstack)
        if fromstack>0  and fromstack<10 and len(movetostacks[fromstack-1])>1:
            fcard = ((movetostacks[fromstack-1])[-1])
            fromstack=movetostacks[int(fromstack)-1]

        elif fromstack == 0 and len(deck) > 1:
            fcard = deck[-1]
            fromstack = deck
        else :
            print("invalid Choice")
            pickcard()
    # Is it 0 (The deck) ?

    # is the stack one of the final?
    elif fromstack == "C" :
        fcard = club[-1]
        fromstack = club
    elif fromstack == "H":
        fcard = heart[-1]
        fromstack= heart
    # Did you pick spades?
    elif fromstack == "S" :
        fcard = spade[-1]
        fromstack = spade
    # Did you pick a diamond
    elif fromstack == "D":
        fcard = diamond[-1]
        fromstack = diamond
    # Do you want to pick the next card in the deck?
    elif fromstack == "N":
        fcard=deck[1]
        fromstack= deck
    else:
        print("Invalid Choice. Choose Again")
        pickcard()
    returnarr=[fcard, fromstack]
    return returnarr


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
    return card[1]


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
    print(color(topcard))
    print(color(newtop))
    if not topcard is int:
        if topval==newval and color(topcard) != color(newtop):
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

def reveal():
    for i in range(0, 6):
        print("Stack " + str(i + 1)+": ", end="")
        # choose the current stack
        currentstack = movetostacks[i]
        currentcount = revealedstacks[i]
        for i in range(0, (len(currentstack)-1) - currentcount):
            print("\'X\'  ", end="")
        # print the revealed cards
        if len(currentstack)>1:
            print(currentstack[-1 * currentcount:])
        # Print a new line if stack is empty
        else:
            print()
    # show the top card of the deck
    print("Deck: ", end="")
    print(deck[-1])
    # show the top cards of each final pile
    print("Clubs: "+str(club[-1]))
    print("Hearts: " + str(heart[-1]))
    print("Spades: " + str(spade[-1]))
    print("Diamonds: " + str(diamond[-1]))

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

# create the cards
suites=["♠", "♡", "♢", "♣"]
cards=[]
nums=[]
# ADD 1-10 to the numbers
for num in range(1, 10):
    nums.append(str(num))
nums.append("J")
nums.append("Q")
nums.append("K")
nums.append("T")
for suite in suites:
    for type in nums:
        cards.append(type+suite)

# create the piles
deck=[0]
stack1=[1]
stack2=[2]
stack3=[3]
stack4=[4]
stack5=[5]
stack6=[6]
movetostacks=[stack1, stack2,stack3, stack4, stack5, stack6]
club=["C"]
heart=["H"]
spade=["S"]
diamond=["D"]
finalstacks=[club,heart,spade,diamond]
#Show which cards are revealed
revealedstacks=[1,1,1,1,1,1]
for i in range(0,6):
    assign(cards, movetostacks[i],i+1)
assign(cards, deck, len(cards))
# Welcome "Screen"
print("")
print("")
print("Welcome to Text-Solitare")
print("Made by Chinmai Srinivas")
print("Intro To CS Final project")
print("Made in Python 3.6")
print("Started on 12/9/17")
print("Projects Never end. Still a work in progress")
print("Press enter to continue")
input()
print("\n\n\n\n\n\n\n")


# reveal instructions
print("Instructions:")
print("To move from a stack, choose 1-6")
print("To move from deck, 0")
print("To move to final stacks:")
print("C- Clubs")
print("H- Hearts")
print("S- Spades")
print("D- Diamonds")
print("N- Next card in Deck")
input("Press enter to Continue")
print("\n\n")
# Game loop
while not haswon(finalstacks):
    reveal()
    # reset the turn variables
    fromcard = 0
    tocard = 0
    fromstack = False
    tostack = False
    movevalid=False
    while not movevalid:
        fromcard = 0
        tocard = 0
        fromstack = False
        tostack = False
        while fromstack == False and fromstack.__class__ is bool:
            print("Where should the card come from?")
            fromarr = pickcard()
            fromcard = fromarr[0]
            fromstack = fromarr[1]
            print("You chose: "+ str(fromcard))
            isn=False
            if fromcard==deck[1] and len(deck)>1:
                #bypass the next stuff
                movevalid=True
                tostack= deck[-1]
                isn=True
            if len(fromstack)<2:
                fromstack=False

        while tostack == 0 and tostack == False:
            print("Where should the card go?")
            toarr=pickcard()
            tocard=toarr[0]
            tostack=toarr[1]
            print("You chose: "+ str(tocard))
            if tostack==0:
                print("invalid Choice")
        # Are you trying to move to the same stack?
        if tostack != fromstack and not isn:
            # Are you trying to move to one of the mid stacks?
            if tostack[0].__class__ is int and tostack[0]>0:
                # Is your move valid?
                if checkplace(tocard, fromcard):
                    movevalid=True
                    # convoluted way of adding 1 to the revealed for that stack
                    #print(fromstack)
                    # You cant see the cards. Whatevs
                    # print(int(tostack[0]))
                    addarray(revealedstacks,int(tostack[0])-1)
                else:
                    # Make them move again
                    print("invalid Choice Cant Wrong color/number")
            if tostack[0].__class__ is str:
                if (checkfinal(tostack,fromcard)):
                    movevalid=True
            else:
                print("Invalid Choice")
        else:
            print("Invalid Choice")
        #movevalid=True
    print("Move validated")
    # Allow shuffiling through Deck:
    # So if the choice is an "N", Switch the deck and run agian
    if fromcard==deck[1]:
        deck.append(deck[1])
        deck.pop(1)
    # Otherwise, move the card to the correct spot
    else:
        fromstack.pop(-1)
        tostack.append(fromcard)
    print("Success!")
