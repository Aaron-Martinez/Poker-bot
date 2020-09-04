
import src
from src.deck import Deck
from src.hand import Hand
from src.table import Table
from src.player import Player

max_seats = 6
small_blind = 5
big_blind = 10
antes = 0
table = Table(max_seats, small_blind, big_blind, antes)

class Game:

    def __init__(self, table):
        self._table = table
        self._deck = Deck()
        self._dealer_seat_num = None

    @property
    def table(self):
        return self._table

    @property
    def deck(self):
        return self._deck

    @property
    def dealer_seat_num(self):
        return self._dealer_seat_num

    @dealer_seat_num.setter
    def dealer_seat_num(self, seat_num):
        self._dealer_seat_num = seat_num

    players = []

    def run(self):
        # todo: add conditions for game to continue (game not stopped by user) and set game_continues
        first_dealer_num = 1
        self.dealer_seat_num = first_dealer_num
        # while loop for individual hands
        game_continues = True
        handsPlayed = 0
        while game_continues:
            hand = self.initialize_hand(self.dealer_seat_num)
            hand.play_hand()

            handsPlayed += 1
            if handsPlayed >= 3:
                game_continues = False

            self.dealer_seat_num = self.move_dealer(self.dealer_seat_num)



    def initialize_hand(self, dealer_seat):
        print('\n----------- Initializing new hand -----------')
        #self.debug_print_players(dealer_seat)
        players = self.initialize_players(dealer_seat)
        hand = Hand(self.table, self.deck, dealer_seat, players)
        return hand


    def initialize_players(self, dealer_seat):
        players = []
        i = dealer_seat + 1
        for counter in range(self.table.max_seats):
            if i >= self.table.max_seats:
                if self.table.get_seat(i - self.table.max_seats).active_player():
                    players.append(self.table.get_seat(i - self.table.max_seats).get_player())
            else:
                if self.table.get_seat(i).active_player():
                    players.append(self.table.get_seat(i).get_player())
            i += 1
        positions = [' SB', ' BB', 'UTG', ' HJ', ' CO', ' BU']
        if len(players) < 6:
            positions.remove('UTG')
        if len(players) < 5:
            positions.remove('HJ')
        if len(players) < 4:
            positions.remove('CO')
        if len(players) < 3:
            positions.remove('BU')
        print("Players in next hand:")
        for p in range(len(players)):
            players[p].position = positions[p]
            print(players[p].name + '  ' + positions[p] + '  [' + str(players[p].stack_size) + ']')

        return players


    def move_dealer(self, dealer_seat):
        if dealer_seat == self.table.max_seats:
            return 1
        else:
            return dealer_seat + 1


    def debug_print_players(self, i):
        players = []
        for counter in range(1, self.table.max_seats + 1):
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
            print(p.name)
