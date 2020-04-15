
class Pot:

    # pot should maybe store and update hand history for Hand to collect after

    def __init__(self, table, players):
        self.total = 0
        self.table = table
        self.players = players
        self.street = 0
        # the pot is good when a hand is ready to proceed to the next street
        self.pots_good = False


class SidePot(Pot):

    def __init__(self, parent, players):
        self.table = parent.table
        self.players = players