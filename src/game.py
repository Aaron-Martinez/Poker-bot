
import src
from src.deck import Deck
from src.hand import Hand
from src.table import Table

max_seats = 6
small_blind = 5
big_blind = 10
antes = 0
table = Table(max_seats, small_blind, big_blind, antes)

class Game:

    def __init__(self, table):
        self._table = table
        self._deck = table.deck

    @property
    def table(self):
        return self._table

    @property
    def deck(self):
        return self._deck

    players = []
    deck = []


    def run(self):
        # todo: add conditions for game to continue (game not stopped by user)
        first_dealer_num = 1
        dealer_seat_num = first_dealer_num
        # todo: make deck a class attribute of game
        # while loop for individual hands
        game_continues = True
        while game_continues:
            # whos in thhis hand? pass players[] to hand
            # players ordered by position from small blind to dealer
            players = []
            i = dealer_seat_num + 1
            for counter in range(1, self.table.max_seats+1):
                if i >= self.table.max_seats:
                    print(i - self.table.max_seats)
                    players.append(self.table.get_seat(i - self.table.max_seats).get_player())
                    print("size = " + str(players.__len__()))
                    print("name = " + str(players[0].name))
                else:
                    print(i)
                    players.append(self.table.get_seat(i).get_player())
                    print("size = " + str(players.__len__()))
                    print("name = " + str(players[0].name))
                i += 1
            for p in players:
                from src.player import Player
                print(p.name)
            # hand = Hand(self.table(), self.deck())
            game_continues = False
