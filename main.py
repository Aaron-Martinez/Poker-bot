
from src.game import Game
from src.player import *
from src.table import Table

max_seats = 6
small_blind = 1
big_blind = 2
antes = 0
table = Table(max_seats, small_blind, big_blind, antes)
player1 = HumanPlayer("Aa")
player2 = HumanPlayer("p2")
player3 = HumanPlayer("p3")
player4 = HumanPlayer("p4")
player5 = HumanPlayer("p5")
player6 = HumanPlayer("p6")

#player2 = RandomComputerPlayer("p2")
#player3 = RandomComputerPlayer("p3")
#player4 = RandomComputerPlayer("p4")
#player5 = RandomComputerPlayer("p5")
#player6 = RandomComputerPlayer("p6")
players = [player1, player2, player3, player4, player5, player6]
i = 0
for seat in table.seats:
    #print("trying to sit player " + players[i].name)
    seat.sit(players[i])
    i += 1

game = Game(table)
game.run()
print("\ndone")