import random
import copy

def createCards():
    cards = []
    for i in range(70): # there are roughly 70 people but confirm the number later
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
    firstDiag = [0, 6, 12, 18, 24]
    secondDiag = [4, 8, 12, 16, 20]
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
    end = False
    calledUnsorted = []

    # add numbers and check if anyone has bingo
    while True:
        called.append(numbers.pop())
        for card in cards:
            if checkCard(called, card):
                calledUnsorted = copy.copy(called)
                called.sort()
                card.sort()
                # print "called ", called
                # print "a winn ", card # note: this stops execution as soon as any winner is found
                end = True
                # print "before: ", calledUnsorted
                return calledUnsorted
            
            

def driver():
    # game results is a list of booleans s.t. a boolean is true if the game had 6 B's in a row pulled
    # and false otherwise
    trues = 0
    falses = 0
    for i in range(10000):
        addTrue = False
        calledNumbers = playOneBingoGame()
        # print "called numbers: ", calledNumbers
        for ind in range(len(calledNumbers)):

            # this section needs work
            if 1 <= calledNumbers[ind] <= 15:
                try:
                    if 1 <= calledNumbers[ind + 1] <= 15:
                        if 1 <= calledNumbers[ind + 2] <= 15:
                            if 1 <= calledNumbers[ind + 3] <= 15:
                                if 1 <= calledNumbers[ind + 4] <= 15:
                                    if 1 <= calledNumbers[ind + 5] <= 15:
                                        addTrue = True
                                        print calledNumbers
                except:
                    continue


        if addTrue:
            trues += 1
        else:
            falses += 1
            
    print trues
    print trues + falses

driver()
        
                        


