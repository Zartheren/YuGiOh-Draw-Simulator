# This programs purpose is to simulate first-hand draws of a deck to gauge the decks consistency

import collections
import string
import numpy as np
import re
import random
import pyinputplus
import os


# Deck list that will hold the exported info from EDO Pro
deckList = collections.deque([])

print("Please paste the deck list copied from EDO Pro")

# Goes through given deck list and separates the card name from the card count
while True:
    desiredCard = input()
    # Looks for a return as the end of the deck list
    if desiredCard == '':
        break
    # Looks at given card name and removes the " x" in each line and separates the name and count by regular expression
    else:
        regexResults = re.search(r'(.*) x([0-9]*)', desiredCard)
        deckList.append(regexResults.groups())

# Making list of only card names
cardNames = [x[0] for x in deckList]
# Value for incrementing the number in the following list output
numList = 0
# Making value for indexing what cards have been added to the deck to be drawn
filling = 0
# Making list of what is going to be complete deck list that will be used for drawing from
deck = collections.deque([])

# Filling deck with cards by their number count
for card in deckList:
    while filling < int(card[1]):
        deck.append(card[0])
        filling += 1
    filling = 0

# Clearing terminal window before displaying list back to user
os.system('cls')

# Printing list of cards with number in front so that the user can return what cards are needed in first hand
while True:
    if len(cardNames) > numList:
        print(f"{(numList + 1)}. {cardNames[numList]}")

        numList += 1

    else:
        print("________________________________________________________________________________")
        break


print("\nWhich of these single cards would you need one of in a opening hand to make a play")
print("Type the number of the corresponding card and hit enter after each one")
print("Enter an empty entry after you have finished")

# Making list for the needed cards in first hand
neededCards = collections.deque([])

# collecting numbers from user of needed cards and referencing them back to corresponding number in list
desiredCard = pyinputplus.inputNum("Card number: ", blank=True, min=1, max=(len(cardNames)))

while desiredCard != "":
    desiredCard = pyinputplus.inputNum("Card number: ", blank=True, min=1, max=(len(cardNames)))

    if desiredCard != "":
        neededCards.append(cardNames[(int(desiredCard) - 1)])

    else:
        print("Please input how many times you would like the program to run")

# Getting number of times to run test
requestedDraws = pyinputplus.inputNum(min=1)

firstDraws = 0
secondDraws = 0
totalDraws = 0
hand = []
firstTurnResults = []
secondTurnResults = []

# Simulate shuffling deck and drawing
for runs in deck:
    while totalDraws < int(requestedDraws):
        # Shuffle deck
        random.shuffle(deck)
        # Getting random boolean to see if first hand is on first turn or second
        firstTurn = bool(random.getrandbits(1))
        if firstTurn:
            # Drawing the first 5 cards of the deck for first turn move
            for index in range(0, 5):
                hand.append(deck[index])
            # Storing resulting draws that match the needed cards
            firstTurnResults.append(len(np.intersect1d(neededCards, hand)))
            # Adding to first turn draw counter
            firstDraws += 1

        else:
            # Drawing the first 6 cards of the deck for second turn move
            for index in range(0, 6):
                hand.append(deck[index])
            # Storing resulting draws that match the needed cards
            secondTurnResults.append(len(np.intersect1d(neededCards, hand)))
            # Adding to second turn draw counter
            secondDraws += 1

        # Reset and adding to total draw counter
        hand = []
        totalDraws += 1

# Counting first turn results
firstZero = firstTurnResults.count(0)
firstOne = firstTurnResults.count(1)
firstTwo = firstTurnResults.count(2)
firstThree = firstTurnResults.count(3)
firstFour = firstTurnResults.count(4)
firstFive = firstTurnResults.count(5)

# Counting second turn results
secondZero = secondTurnResults.count(0)
secondOne = secondTurnResults.count(1)
secondTwo = secondTurnResults.count(2)
secondThree = secondTurnResults.count(3)
secondFour = secondTurnResults.count(4)
secondFive = secondTurnResults.count(5)
secondSix = secondTurnResults.count(6)

print(
    f"""    The following is for first turn draws
    You Drew first {firstDraws} times
    You had {firstZero} hands with none of the needed cards or {(100 * firstZero / firstDraws):.2f}%
    {firstOne} with 1 or {(100 * firstOne / firstDraws):.2f}%
    {firstTwo} with 2 or {(100 * firstTwo / firstDraws):.2f}%
    {firstThree} with 3 or {(100 * firstThree / firstDraws):.2f}%
    {firstFour} with 4 or {(100 * firstFour / firstDraws):.2f}%
    {firstFive} with 5 or {(100 * firstFive / firstDraws):.2f}%
    
    The following is for second turn draws
    You Drew second {secondDraws} times
    You had {secondZero} hands with none of the needed cards or {(100 * secondZero / secondDraws):.2f}%
    {secondOne} with 1 or {(100 * secondOne / secondDraws):.2f}%
    {secondTwo} with 2 or {(100 * secondTwo / secondDraws):.2f}%
    {secondThree} with 3 or {(100 * secondThree / secondDraws):.2f}%
    {secondFour} with 4 or {(100 * secondFour / secondDraws):.2f}%
    {secondFive} with 5 or {(100 * secondFive / secondDraws):.2f}%
    {secondSix} with 6 or {(100 * secondSix / secondDraws):.2f}%

    In total out of {totalDraws}, these are the combined results:
    {firstZero + secondZero} with 0 or {(100 * (firstZero + secondZero) / totalDraws):.2f}%
    {firstOne + secondOne} with 1 or {(100 * (firstOne + secondOne) / totalDraws):.2f}%
    {firstTwo + secondTwo} with 2 or {(100 * (firstTwo + secondTwo) / totalDraws):.2f}%
    {firstThree + secondThree} with 3 or {(100 * (firstThree + secondThree) / totalDraws):.2f}%
    {firstFour + secondFour} with 4 or {(100 * (firstFour + secondFour) / totalDraws):.2f}%
    {firstFive + secondFive} with 5 or {(100 * (firstFive + secondFive) / totalDraws):.2f}%
    {secondSix} with 6 or {(100 * secondSix / totalDraws):.2f}%
    """
)
