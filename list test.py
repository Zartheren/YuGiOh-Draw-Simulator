import collections
import numpy as np
import re

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

print("Your deck list is:")

print(deckList)
