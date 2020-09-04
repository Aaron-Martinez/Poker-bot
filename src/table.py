
from src.deck import Deck
from src.seat import Seat


class Table:

    def __init__(self, max_seats, small_blind, big_blind, antes):
        self._max_seats = max_seats
        #self._has_game = has_game
        self._small_blind = small_blind
        self._big_blind = big_blind
        self._antes = antes
        self._seats = []
        for i in range(1, max_seats+1):
            seat = Seat(i)
            self.seats.append(seat)

    @property
    def max_seats(self):
        return self._max_seats

    #@property
    #def has_game(self):
    #    return self._has_game

    @property
    def seats(self):
        return self._seats

    def get_seat(self, seat_num):
        #print("getting seat " + str(seat_num) + " at seats[" + str(seat_num-1) + "]")
        return self.seats[seat_num-1]

    @property
    def small_blind(self):
        return self._small_blind

    @property
    def big_blind(self):
        return self._big_blind

    @property
    def antes(self):
        return self._antes

    def num_seated(self):
        num = 0
        for seat in self.seats:
            if seat.has_player() and seat.player.is_seated():
                num += 1
        return num

    def get_seated_players(self):
        seated_players = []
        for seat in self.seats:
            if seat.has_player() and seat.player.is_seated():
                seated_players.append(seat.player)
        return seated_players
