# This programs purpose is to simulate first-hand draws of a deck to gauge the decks consistency

import collections
import string
import numpy as np
import re
import random

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
desiredCard = input()

while desiredCard != "":
    desiredCard = input()

    if desiredCard.isnumeric() and int(desiredCard) <= len(cardNames):
        neededCards.append(cardNames[(int(desiredCard) - 1)])

    else:
        print("Please input how many times you would like the program to run")

# Getting number of times to run test
requestedDraws = input()

draws = 0
hand = []
results = []

# Simulate shuffling deck and drawing
for runs in deck:
    while draws < int(requestedDraws):
        # Shuffle deck
        random.shuffle(deck)
        # Drawing the first 5 cards of the deck
        for index in range(0, 5):
            hand.append(deck[index])
        # Storing resulting draws that match the needed cards
        results.append(len(np.intersect1d(neededCards, hand)))
        # Reset and adding to draw counter
        hand = []
        draws += 1

zero = results.count(0)
one = results.count(1)
two = results.count(2)
three = results.count(3)
four = results.count(4)
five = results.count(5)

print(
    f"""You had {zero} hands with none of the needed cards
    {one} with 1 or {(100 * one/draws):.2f}%
    {two} with 2 or {(100 * two/draws):.2f}%
    {three} with 3 or {(100 * three/draws):.2f}%
    {four} with 4 or {(100 * four/draws):.2f}%
    {five} with 5 or {(100 * five/draws):.2f}%
    """
    )
