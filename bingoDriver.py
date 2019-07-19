import random
import copy

def createCards():
    cards = []
    for i in range(88): # there are 88 people according to dan diener
        card = []
        a = 1
        b = 15
        for j in range(5):
            for i in range(5):
                randNumToAdd = random.randint(a, b)
                while randNumToAdd in card:
                    randNumToAdd = random.randint(a, b)    
                card.append(randNumToAdd)
            a += 15
            b += 15
        card[12] = 0 # free spot, this should always be in called
        cards.append(card)
    
    return cards

def checkCard(called, card):
    # print "called ", called
    # print "card ", card
    # check columns
    if set(card[:5]) <= set(called) or set(card[5:10]) <= set(called) or set(card[10:15]) <= set(called) or set(card[15:20]) <= set(called) or set(card[20:]) <= set(called):
        # print "win column"
        return True

    # check rows
    multiplesOf5 = [0, 5, 10, 15, 20]
    for i in range(5):
        if set([card[multipleOf5 + i] for multipleOf5 in multiplesOf5]) <= set(called):
            # print "win in row ", i
            return True

    # check diagonals
    firstDiag = [0, 6, 12, 18, 24] # indices for winning a game by doing diagonal from top left to bottom right
    secondDiag = [4, 8, 12, 16, 20] # indices for winning by doing diagonal from bottom left to top right
    if set([card[f] for f in firstDiag]) <= called or set([card[s] for s in secondDiag]) <= set(called):
        # print "win by diag"
        return True
    
    return False


def playOneBingoGame():

    # setup
    called = [0]
    cards = createCards()
    numbers = [i for i in range(1, 76)]
    random.shuffle(numbers)

    # add numbers and check if anyone has bingo
    while True:
        called.append(numbers.pop())
        if any(checkCard(called, card) for card in cards):
            return called
            
            

def driver():
    trues = 0
    total = 10000
    for i in range(total):
        addTrue = False
        calledNumbers = playOneBingoGame()
        # print "called numbers: ", calledNumbers
        for ind in range(len(calledNumbers)):

            # this section needs work
            try:
                if all([1 < calledNumbers[ind + j] <= 15 for j in range(0, 6)]):
                    addTrue = True
                    print calledNumbers
                    break # to prevent repeats in the case of games where 7 or more B's are called in a row
            except:
                continue


        if addTrue:
            trues += 1
        if i % (total / 100)  == 0:
            print float(i) / (float(total) / 100), "percent finished"

    print trues, " games where 6 B's in a row were called out of ",
    print total, " games."

driver()
        
                        


