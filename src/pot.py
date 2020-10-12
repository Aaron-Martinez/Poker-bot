
class Pot:

    # pot should maybe store and update hand history for Hand to collect after

    def __init__(self, table, players):
        self._total = 0
        self.table = table
        self.players = players
        self._allin_players = []
        self.street = 0
        # the pot is good when a hand is ready to proceed to the next street
        self.pots_good = False
        self._side_pots = []

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, new_total):
        self._total = new_total

    @property
    def allin_players(self):
        return self._allin_players

    @property
    def side_pots(self):
        return self._side_pots

    def pot_size(self):
        print('Pot size is: ' + str(self.total))

    def stack_sizes(self):
        for p in self.players:
            print(p.name + ': ' + p.stack_size)

    def collect_blinds(self):
        #self.pot_size()
        print('*** collecting blinds ***')
        if self.players[0].stack_size <= self.table.small_blind:
            self.total = self.total + self.players[0].stack_size
            self.players[0].move_all_in()
        else:
            self.players[0].invest_chips(self.table.small_blind)
            self.total = self.total + self.table.small_blind
        if self.players[1].stack_size <= self.table.big_blind:
            self.total = self.total + self.players[1].stack_size
            self.players[1].move_all_in
        else:
            self.players[1].invest_chips(self.table.big_blind)
            self.total = self.total + self.table.big_blind
        #self.pot_size()

    # amt is assumed not to be greater than player stack size before this method called
    def invest_chips(self,  player, amt):
        player.invest_chips(amt)
        print('Pot size:  ' + str(self.total) + ' -> ' + str(self.total + amt))
        if not self.side_pots:
            self.total += amt
        else:
            # chips are added to currently active sidepot if there is one started
            self.side_pots[-1].total += amt

    def move_all_in(self, player):
        #print('Pot size:  ' + str(self.total) + ' -> ' + str(self.total + player.stack_size))
        #self.total += player.stack_size
        self.invest_chips(player, player.stack_size)
        player.move_all_in()
        self.allin_players.append(player)

    def create_side_pot(self, players):
        side_pot = SidePot(self, players)
        self.add_side_pot(side_pot)

    def add_side_pot(self, side_pot):
        self.side_pots.append(side_pot)

    def return_chips(self, player, amt):
        player.return_chips(amt)
        self.total -= amt

    @staticmethod
    def transfer_chips(from_pot, to_pot, amt):
        from_pot.total -= amt
        to_pot += amt


class SidePot(Pot):

    def __init__(self, parent, players):
        self.table = parent.table
        self.players = players
