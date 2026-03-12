#!/usr/bin/env python3

import sys
from pcard import *
from hand import Hand
from player import *
from record import *


def output(player, score=False):
    hand = player.hand
    if not player.open:
        hand = " ".join(["XX"] + [str(card) for card in hand[1:]])
    if score:
        print("{0}:\t{1} = {2}".format(
            player.name, hand, player.score()))
    else:
        print("{0}:\t{1}".format(player.name, hand))


def game(deck, player, dealer):
    dealer.open = False
    dealer.hand.clear()
    player.hand.clear()
    while True:
        try:
            bet = int(input("How much do you bet? "))
            break
        except ValueError:
            continue
    print("You bet {0} coin(s)".format(bet))
    player.draw(deck)
    dealer.draw(deck)
    player.draw(deck)
    dealer.draw(deck)
    output(dealer)
    output(player, True)

    lose = False
    win = False
    tie = False
    yn = input("Hit or Stay? (h or s)")
    while yn in "hHyY":
        player.draw(deck)
        output(player, True)
        if player.score() > 21:
            lose = True
            break
        yn = input("Hit or Stay? (h or s)")

    if not lose:
        print("Turn of the Dealer")
        print("Open the card")
        dealer.open = True
        output(dealer)
        while dealer.score() < 17:
            dealer.draw(deck)
            output(dealer)
            if dealer.score() > 21:
                win = True

        print("No more hit")
        output(dealer, True)
        output(player, True)

        if player.score() > dealer.score():
            win = True
        elif player.score() == dealer.score():
            tie = True
        else:
            lose = True

    if win:
        print("You Win")
        player.coin += bet
        gain = bet
    elif tie:
        print("Tie")
        gain = 0
    elif lose:
        print("You Lose")
        player.coin -= bet
        gain = -bet
    else:
        print("You Win or Lose?")
    print("You have {0} coins".format(player.coin))
    record.append(GameRecord(player.hand, dealer.hand, gain))

deck = Deck()
deck.shuffle()

player = Player("You", 100)
dealer = Dealer()
record = []
yn = input("Do you play the game?(y/n)")
while yn != "n" and yn != "N":
    game(deck, player, dealer)
    yn = input("Next Game? (y/n)")

print("Game End")
with open("game.log", "w") as fp:
    for line in record:
        fp.write(str(line)+"\n")
