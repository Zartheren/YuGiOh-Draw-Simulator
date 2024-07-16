# This programs purpose is to simulate first-hand draws of a deck to gauge the decks consistency

import collections
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

# Output what you entered, in the stored format
print("Your deck list is:")
print(deckList)

print('Number of card names:')
print(len(deckList))

# Making list of only card names
cardNames = [x[0] for x in deckList]
numList = 0

while True:
    if len(cardNames) <= numList:
        print(f"{numList}. {list.index(cardNames[numList])}")

        numList = numList + 1

    else:
        break

print("Done")

random.shuffle(deckList)

