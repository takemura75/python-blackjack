import random


class PlayingCard:
    """definition of Playing Card"""
    SUIT_LIST = ('♣', '♢', '♡', '♠')
    NUMBER_LIST = ('', 'A', '2', '3', '4', '5', '6',
                   '7', '8', '9', '10', 'J', 'Q', 'K')

    def __init__(self, suit, number):
        """constructor of Playing Card"""
        self.suit = suit
        self.number = number

    def output(self):
        return self.suit + self.NUMBER_LIST[self.number]

    def __str__(self):
        return self.suit + self.NUMBER_LIST[self.number]

    def __eq__(self, other):
        return (self.suit == other.suit
                and self.number == other.number)

    def __hash__(self):
        return hash((self.suit, self.number))


class Deck(list):
    """definition of Deck"""
    def __init__(self):
        """constructor of Deck"""
        super().__init__()
        self.extend([PlayingCard(x, y+1)
                     for x in PlayingCard.SUIT_LIST
                     for y in range(13)])
        self.shuffle()

    def pop(self):
        return super().pop()

    draw = pop

    def shuffle(self):
        """shuffle the deck"""
        random.shuffle(self)

    def __str__(self):
        return " ".join([str(c) for c in self])

    def insert(self, card):
        """insert the card at the random point"""
        i = random.randint(0, len(self))
        super().insert(i, card)


if __name__ == "__main__":
    card1 = PlayingCard(PlayingCard.SUIT_LIST[3], 1)
    card2 = PlayingCard(PlayingCard.SUIT_LIST[0], 11)
    card3 = PlayingCard(PlayingCard.SUIT_LIST[2], 12)
    card4 = PlayingCard(PlayingCard.SUIT_LIST[1], 13)
    print(card1, card2, card3, card4)

    deck = Deck()
    print(deck)
