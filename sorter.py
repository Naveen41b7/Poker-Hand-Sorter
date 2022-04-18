# importing sys for reading a file
import sys 

# Suit Types -> D - Diamonds, H - Hearts, S - Spades, C - Clubs
 
# Store the list of values of card from lowest value to highest value
pokerCards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# Initialize global variables of both players winning game count
# Increment values of below variables determining which player won
player1won = 0
player2won = 0

# If both the players get tie, use this variable to determine which player is winner
playersTiedValue = 0


def getCardsValueIndex(fiveCards):
    cardsList = getCardsList(fiveCards)
    cardValueIndex = []
    for cardValue in cardsList:
        cardValueIndex.append(pokerCards.index(cardValue[0]))
    
    return sorted(cardValueIndex, reverse=True)


# Gets the cards of single player as sorted/unsorted list based on isSort param
def getCardsList(fiveCards, isSort = False):
    if isSort:
        return sorted(fiveCards.split( ))
    else:
        return fiveCards.split( )


# Gets only the value(number) of cards of single player
def getCardsValues(fiveCards):
    values = []
    for card in fiveCards.split( ):
        values.append(card[0:1])
        
    return values




# Test case pass(player2) - AH 9S 4D TD 8S KS QS JS TS AS
# Test case fail(player2) - AH 9S 4D TD 8S KS QD JC TD AC
def isRoyalFlush(fiveCards):
    # T - Ten,  J - Jack, Q - Queen, K - King, A - Ace
    rfList = ['T', 'J', 'Q', 'K', 'A']
    firstSuit = fiveCards[1:2]
    isRf = 10
    for rf in rfList:
        if fiveCards.count(firstSuit) != 5 or fiveCards.find(rf) == -1:
            isRf = -1
            break
            
    return isRf

 

# Test case pass(player2) - AH 9S 4D TD 8S AH 4H AH AH AH
# Test case fail(player2) - AH 9S 4D TD 8S 4H 3H 6H 7H 5H
def isFourKind(fiveCards):
    fourKind = -1
    noDuplicateList = list(dict.fromkeys(getCardsValues(fiveCards)))
    # print(noDuplicateList)
    if (len(noDuplicateList) == 2 and isThreeKind(fiveCards) != 4):
        fourKind = 8
    
    return fourKind



# Test case pass(player2) - AH 9S 4D TD 8S AH 4H AH AH AH
# Test case fail(player2) - AH 9S 4D TD 8S 4H 3H 6H 7H 5H
def isFlush(fiveCards):
    firstSuit = fiveCards[1:2]
    isFlush = -1

    if fiveCards.count(firstSuit) == 5:
        isFlush = 6
            
    return isFlush

 

# Test case pass(player2) - AH 9S 4D TD 8S 4H 3H 6H 7H 5H
# Test case fail(player2) - AH 9S 4D TD 8S AH 4H AH AH AH  
def isStraight(fiveCards):
    counter = pokerCards.index(fiveCards[0][0:1])
    isStraight = 5

    for card in fiveCards:
        # print(card[0] + '====' + pokerCards[counter])
        if counter > 12 or card[0] != pokerCards[counter]:
            isStraight = -1
            break
            
        counter += 1
    return isStraight



# Test case pass(player2) - AH 9S 4D TD 8S 4H 3H 6H 7H 5H
# Test case fail(player2) - AH 9S 4D TD 8S KH JS QC TC 8D
def isStraightFlush(fiveCards):
    isStraightFlush = -1
    fiveCardsList = getCardsList(fiveCards)

    if isFlush(fiveCards) == 6 and isStraight(fiveCardsList) == 5:
        isStraightFlush = 9
    
    return isStraightFlush



# Test case pass(player2) - AH 9S 4D TD 8S 2S 2H 3H 3C AD
# Test case fail(player2) - AH 9S 4D TD 8S 4D 3H 6S 7C 5S
def isTwoPairs(fiveCards):
    global playersTiedValue
    cardsList = getCardsValues(fiveCards)
    twoPairs = -1
    duplicateList = list([card for card in cardsList if cardsList.count(card) in range(2, 3)])
    duplicateList = list(dict.fromkeys(duplicateList))

    # print(duplicateList)
    if (len(duplicateList) == 2):
        playersTiedValue = max(pokerCards.index(duplicateList[0]), pokerCards.index(duplicateList[1]))
        twoPairs = 3
        
    return twoPairs



# Test case pass(player2) - AH 9S 4D TD 8S 3S 4H 3H AD 8C
# Test case fail(player2) - AH 9S 4D TD 8S 4D 3H 4S 7C 4S  
def isPair(fiveCards):
    global playersTiedValue
    cardsList = getCardsValues(fiveCards)
    pair = -1
    duplicateList = list([card for card in cardsList if cardsList.count(card) in range(2, 3)])
    duplicateList = list(dict.fromkeys(duplicateList))
    
    # print(duplicateList)
    if (len(duplicateList) == 1):
        playersTiedValue = pokerCards.index(duplicateList[0])
        pair = 2
    
    return pair



# Test case pass(player2) - AH 9S 4D TD 8S 3S 4H 3H AD 3C
# Test case fail(player2) - AH 9S 4D TD 8S 4D 3H 6S 7C 5S    
def isThreeKind(fiveCards):
    threeKind = -1
    noDuplicateList = list(dict.fromkeys(getCardsValues(fiveCards)))
    
    if (len(noDuplicateList) in range(2, 4) and isTwoPairs(fiveCards) != 3):
        threeKind = 4
    
    return threeKind



# Test case pass(player2) - AH 9S 4D TD 8S 3S 3H 3H AD AC
# Test case fail(player2) - AH 9S 4D TD 8S 3D 3H 4S 6C 4S 
def isFullHouse(fiveCards):
    global playersTiedValue
    fullHouse = -1
    cardsList = getCardsValues(fiveCards)
    
    if (isThreeKind(fiveCards) == 4 and isPair(fiveCards) == 2):
        fullHouse = 7
    
    for card in cardsList:
        if cardsList.count(card) == 3:
            playersTiedValue = pokerCards.index(card)
            break
    
    return fullHouse



# Test case pass1(player2) - AH 9S 4D TD 8S 4H 4C 6S 7S KD
# Test case pass2(player2) - AH 9S 4D TD 8S 2C 3S 9S 9D TD
def getHighCard(fiveCards):
    global playersTiedValue
    valueIndexList = getCardsValueIndex(fiveCards)

    return max(valueIndexList)




def highCardTieBreaker(p1list, p2list):
    global player1won, player2won
    for c1, c2 in zip(p1list, p2list):
        if (c1 == c2):
            continue
        elif (c1 > c2):
            player1won += 1
            break
        else:
            player2won += 1
            break




# function to decide winner from 2 players
def getRankofPlayer(fiveCards):
    playerRank = -1
    if (isRoyalFlush(fiveCards) == 10):
        playerRank = 100
    elif (isStraightFlush(fiveCards) == 9):
        playerRank = 90
    elif (isFourKind(fiveCards) == 8):
        playerRank = 80
    elif (isFullHouse(fiveCards) == 7):
        playerRank = 70
    elif (isFlush(fiveCards) == 6):
        playerRank = 60
    elif (isStraight(getCardsList(fiveCards, True)) == 5):
        playerRank = 50
    elif (isThreeKind(fiveCards) == 4):
        playerRank = 40
    elif (isTwoPairs(fiveCards) == 3):
        playerRank = 30
    elif (isPair(fiveCards) == 2):
        playerRank = 20
    else:
        playerRank = getHighCard(fiveCards)
        
    return playerRank




# method which determines which player is won
def determinePlayerWon(playerCards):
    p1Cards = playerCards[0:14] # get only player1 cards
    p2Cards = playerCards[15:len(playerCards)] # get only player2 cards
    
    p1rank = getRankofPlayer(p1Cards) # get rank of player1
    p1tied = playersTiedValue # if ranks tied, use this to determine winner
    p2rank = getRankofPlayer(p2Cards) # get rank of player2
    p2tied = playersTiedValue # if ranks tied, use this to determine winner
    
    # global variables that are initialized in line 11 and 12 
    # whichever player wins increment their winning count
    global player1won, player2won

    if (p1rank > p2rank):
        player1won += 1
    elif (p1rank < p2rank):
        player2won += 1
    elif (p1rank == p2rank and p2rank % 10 == 0):
            if (p1tied > p2tied):
                player1won += 1
            elif (p1tied < p2tied):
                player2won += 1
            else:
                highCardTieBreaker(getCardsValueIndex(p1Cards), getCardsValueIndex(p2Cards))
    else:
        highCardTieBreaker(getCardsValueIndex(p1Cards), getCardsValueIndex(p2Cards))



# How to run?
# For windows, in the root folder of this project, open cmd
# Run the command -> 'python PokerHandSorter_Sharan.py poker-hands.txt'
# For testing -> 'python PokerHandSorter_Sharan.py poker-hands-test.txt'

# reads the string passed as first argument
inFile = sys.argv[1]


# open the file whose name matches first argument
with open(inFile, 'r') as cards:
    playerCardsList = cards.read().splitlines() # convert all lines to list


# Iterate through each item in the list and pass it 
for playerCards in playerCardsList:
    determinePlayerWon(playerCards) # pass each item to this function to know which player won


# Print the number of hands of each player won in game
print("Player 1: " + str(player1won))
print("Player 2: " + str(player2won))