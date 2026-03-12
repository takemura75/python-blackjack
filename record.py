from pcard import *


class GameRecord():
    """definition of Deck"""
    def __init__(self, player_hand, dealer_hand, gain):
        self.player_hand = str(player_hand)
        self.dealer_hand = str(dealer_hand)
        self.gain = gain

    def __str__(self):
        return ",".join([self.player_hand,
                         self.dealer_hand, str(self.gain)])
