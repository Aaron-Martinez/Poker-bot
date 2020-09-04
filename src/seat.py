
class Seat:

    def __init__(self, table, num):
        self._table = table
        self._num = num
        self._has_player = False
        self.player = None
        self._is_sitting = False
        self._new_player = True


    def __init__(self, num):
        self._num = num
        self._has_player = False
        self.player = None

    @property
    def table(self):
        return self._table

    @property
    def num(self):
        return self._num

    @property
    def has_player(self):
        return self._has_player

    @has_player.setter
    def has_player(self, value):
        self._has_player = value

    @property
    def is_sitting(self):
        return self._is_sitting

    @is_sitting.setter
    def is_sitting(self, sitting):
        self._is_sitting = sitting

    def active_player(self):
        if self.has_player and self.is_sitting:
            return True
        else:
            return False

    def get_player(self):
        if self.has_player:
            return self.player
        else:
            print("no player in this seat")

    def new_player(self):
        return self._new_player


    #@property
    #def player(self):
    #    return self._player

    def sit(self, player):
        self.player = player
        self.has_player = True
        self.is_sitting = True
        print("sitting player " + player.name)