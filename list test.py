
deck = []

while True:
    addCard = input()
    if addCard == '':
        break
    else:
        deck.append(addCard)

deck = ' x'.join(deck).split(' x')

print("Your deck list is:")

# for addCard in deck:
#    print(addCard)

print(deck)
