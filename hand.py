from pcard import *


class Hand(Deck):
    """definition of Hand"""

    def __init__(self):
        """constructor of Hand"""
        super().__init__()
        self.clear()

    def score(self):
        score = 0
        ace_count = 0

        for card in self:
            if card.number == 1:
                ace_count += 1
            elif card.number >= 10:
                score += 10
            else:
                score += card.number

        for _ in range(ace_count):
            if score + 11 <= 21:
                score += 11
            else:
                score += 1

        return score