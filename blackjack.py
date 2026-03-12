from pcard import *
from hand import *
from player import *
from record import *


deck = Deck()
deck.shuffle()

player = Player("Player", 100)
dealer = Dealer("Dealer")

record = []

while True:
    if player.coin <= 0:
        print("Game over")
        break

    # 初期化
    player.hand.clear()
    dealer.hand.clear()

    # 賭け金入力
    while True:
        try:
            bet = int(input(f"bet? (coin: {player.coin}) > "))
            if bet <= 0:
                print("1以上の数字を入力してください")
            elif bet > player.coin:
                print("所持金以下の金額を入力してください")
            else:
                break
        except ValueError:
            print("数字を入力してください")

    # 最初の2枚を配る
    player.draw(deck)
    dealer.draw(deck)
    player.draw(deck)
    dealer.draw(deck)

    print(f"Dealer: {dealer.hand[0]}, ?")
    print(f"Player: {player.hand}  score={player.score()}")

    # プレイヤーのターン
    while player.score() < 21:
        yn = input("Hit or Stay? [h/s] > ")
        if yn not in "hHsS":
            print("h か s を入力してください")
            continue
        if yn in "sS":
            break

        player.draw(deck)
        print(f"Player: {player.hand}  score={player.score()}")

    # 勝敗判定
    if player.score() > 21:
        print("Player bust")
        player.coin -= bet
        result = -bet

    else:
        print(f"Dealer: {dealer.hand}  score={dealer.score()}")

        while dealer.score() < 17:
            dealer.draw(deck)
            print(f"Dealer: {dealer.hand}  score={dealer.score()}")

        if dealer.score() > 21:
            print("Dealer bust")
            player.coin += bet
            result = bet
        elif player.score() > dealer.score():
            print("Player win")
            player.coin += bet
            result = bet
        elif player.score() < dealer.score():
            print("Dealer win")
            player.coin -= bet
            result = -bet
        else:
            print("Draw")
            result = 0

    print(f"coin: {player.coin}")

    # 記録
    game_record = GameRecord(player.hand, dealer.hand, result)
    record.append(game_record)

    yn = input("Continue? [y/n] > ")
    if yn not in "yY":
        break

# ログ保存
with open("game.log", "w", encoding="utf-8") as f:
    for game in record:
        f.write(str(game) + "\n")
        
