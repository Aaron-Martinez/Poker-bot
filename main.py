
from src.game import Game
from src.player import Player
from src.table import Table

max_seats = 6
small_blind = 1
big_blind = 2
antes = 0
table = Table(max_seats, small_blind, big_blind, antes)
player1 = Player("p1")
player2 = Player("p2")
player3 = Player("p3")
player4 = Player("p4")
player5 = Player("p5")
player6 = Player("p6")
players = [player1, player2, player3, player4, player5, player6]
i = 0
for seat in table.seats:
    print("trying to sit player " + players[i].name)
    seat.sit(players[i])
    i += 1

game = Game(table)
game.run()
print("done")