# This programs purpose is to simulate first-hand draws of a deck to gauge the decks consistency

import collections
import string
import numpy as np
import re
import random

# Deck list that will hold the exported info from EDO Pro
deckList = collections.deque([])

# Goes through given deck list and separates the card name from the card count
while True:
    addCard = input()
    # Looks for a return as the end of the deck list
    if addCard == '':
        break
    # Looks at given card name and removes the " x" in each line and separates the name and count by regular expression
    else:
        regexResults = re.search(r'(.*) x([0-9]*)', addCard)
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

print("Which of these single cards would you need one of in a opening hand to make a play")
print("Type the number of the corresponding card and hit enter after each one")
print("Enter an empty entry after you have finished")

# Printing list of cards with number in front so that the user can return what cards are needed in first hand
while True:
    if len(cardNames) > numList:
        print(f"{(numList + 1)}. {cardNames[numList]}")

        numList += 1

    else:
        print("________________________________________________________________________________")
        break

# Making list for the needed cards in first hand
neededCards = collections.deque([])

# collecting numbers from user of needed cards and referencing them back to corresponding number in list
while True:
    addCard = input()
    if addCard == "":
        break

    elif addCard.isnumeric() and int(addCard) <= len(cardNames):
        neededCards.append(cardNames[(int(addCard) - 1)])

    else:
        print("Please enter a number corresponding to one of the card numbers above")

random.shuffle(deck)

print(deck)
