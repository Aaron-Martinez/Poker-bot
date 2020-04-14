
class Seat:

    def __init__(self, table, num):
        self._table = table
        self._num = num
        #self._has_player = False
        self.has_player = False
        self.player = None

    def __init__(self, num):
        self._num = num
        #self._has_player = False
        self.has_player = False
        self.player = None

    @property
    def table(self):
        return self._table

    @property
    def num(self):
        return self._num

    #@property
    #def has_player(self):
    #    return self._has_player

    #@has_player.setter
    #def has_player(self, value):
    #    'setting'
    #    self.has_player = value

    def get_player(self):
        if self.has_player:
            return self.player
        else:
            print("no player in this seat")

    #@property
    #def player(self):
    #    return self._player

    def sit(self, player):
        self.player = player
        self.has_player = True
        print("sitting player " + player.name)