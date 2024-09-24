import deck_of_cards

# make the piles first for the game, seven piles
# and create the deck

pile_1 = []
pile_2 = []
pile_3 = []
pile_4 = []
pile_5 = []
pile_6 = []
pile_7 = []
pile_help = []

piles = [pile_1, pile_2, pile_3, pile_4, pile_5, pile_6, pile_7]

deck = deck_of_cards.Deck()
deck.shuffle()


# simulating dealing out the deck with 3 cards leftover
# dealing out 7 to each pile allows for 3 leftover in "help" pile
# doing one large for loop create duplicates

for i in range(7):
    pile_1.append(deck.draw())
for i in range(7):
    pile_2.append(deck.draw())
for i in range(7):
    pile_3.append(deck.draw())
for i in range(7):
    pile_4.append(deck.draw())
for i in range(7):
    pile_5.append(deck.draw())
for i in range(7):
    pile_6.append(deck.draw())
for i in range(7):
    pile_7.append(deck.draw())
for i in range(3):
    pile_help.append(deck.draw())

print("1")
for card in pile_1:
    card.show()

print("2")
for card in pile_2:
    card.show()

print("3")
for card in pile_3:
    card.show()

print("4")
for card in pile_4:
    card.show()

print("5")
for card in pile_5:
    card.show()

print("6")
for card in pile_6:
    card.show()

print("7")
for card in pile_7:
    card.show()

print("help")
for card in pile_help:
    card.show()
