
class Pot:

    # pot should maybe store and update hand history for Hand to collect after

    def __init__(self, table, players):
        self._total = 0
        self.table = table
        self.players = players
        self.street = 0
        # the pot is good when a hand is ready to proceed to the next street
        self.pots_good = False

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, new_total):
        self._total = new_total

    def pot_size(self):
        print('Pot size is: ' + str(self.total))

    def stack_sizes(self):
        for p in self.players:
            print(p.name + ': ' + p.stack_size)

    def collect_blinds(self):
        self.pot_size()
        if self.players[0].stack_size <= self.table.small_blind:
            self.total = self.total + self.players[0].stack_size
            self.players[0].stack_size = 0
        else:
            self.players[0].stack_size = self.players[0].stack_size - self.table.small_blind
            self.total = self.total + self.table.small_blind
        if self.players[1].stack_size <= self.table.big_blind:
            self.total = self.total + self.players[1].stack_size
            self.players[1].stack_size = 0
        else:
            self.players[1].stack_size = self.players[1].stack_size - self.table.big_blind
            self.total = self.total + self.table.big_blind
        self.pot_size()


class SidePot(Pot):

    def __init__(self, parent, players):
        self.table = parent.table
        self.players = players