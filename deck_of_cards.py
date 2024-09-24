import random


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["spades", "hearts", "diamonds", "hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    # fisher-yates shuffle
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        c = self.cards.pop()
        return c

# class Player(object):
#     def __init__(self):


# deck = Deck()
# deck.shuffle()
# deck.show()
#
# print('pause\n')
#
# card = deck.draw()
# card.show()
#
# print('\npause\n')
#
# deck.show()


