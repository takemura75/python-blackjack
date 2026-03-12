from hand import Hand
from pcard import Deck


class Person:
    """definition of Person"""

    def __init__(self, name=""):
        self.name = name
        self.hand = Hand()

    def draw(self, deck):
        try:
            self.hand.append(deck.draw())
        except IndexError:
            deck.extend(Deck())
            deck.shuffle()
            self.hand.append(deck.draw())

    def score(self):
        return self.hand.score()


class Player(Person):
    """definition of Player"""

    def __init__(self, name="", coin=0):
        super().__init__(name)
        self.coin = coin


class Dealer(Person):
    """definition of Dealer"""

    def __init__(self, name="Dealer"):
        super().__init__(name)


if __name__ == "__main__":
    p = Player("Alice", 100)
    print(p.coin)
    d = Dealer()
    print(d.hand)
