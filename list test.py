# This programs purpose is to simulate first-hand draws of a deck to gauge the decks consistency

import collections
import string
import numpy as np
import re
import random

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

# # Output what you entered, in the stored format
# print("Your deck list is:")
# print(deckList)
#
# print('Number of card names:')
# print(len(deckList))

# Making list of only card names
cardNames = [x[0] for x in deckList]
numList = 0

print("Which of these single cards would you need one of in a opening hand to make a play")
print("Type the number of the corresponding card and hit enter after each one")
print("Enter an empty entry after you have finished")

while True:
    if len(cardNames) > numList:
        print(f"{(numList + 1)}. {cardNames[numList]}")

        numList = numList + 1

    else:
        print("________________________________________________________________________________")
        break

neededCards = collections.deque([])

while True:
    addCard = input()
    if addCard == "":
        break

    elif addCard.isnumeric() and int(addCard) <= len(cardNames):
        neededCards.append(cardNames[(int(addCard) - 1)])

    else:
        print("Please enter a number corresponding to one of the card numbers above")

# # Print out list of cards that user marked as needed
# print(neededCards)

# Filling deck with cards by their number count
filling = 0
deck = collections.deque([])

while filling <= len(cardNames):
    deck.append()

random.shuffle(deckList)

