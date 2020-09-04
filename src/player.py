
class Player:
    is_small_blind = False
    is_big_blind = False
    is_seated = True

    def __init__(self, name):
        self._name = name
        self._positions = ['BU', 'SB', 'BB', 'UTG', 'HJ', 'CO']
        self._position = ''
        self._stack_size = 200
        self._hole_cards = []

    @property
    def stack_size(self):
        return self._stack_size

    @stack_size.setter
    def stack_size(self, new_size):
        self._stack_size = new_size

    @property
    def is_seated(self):
        return self.is_seated

    @property
    def name(self):
        return self._name

    @property
    def positions(self):
        return self._positions

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, pos):
        self._position = self.positions[pos]

    @position.setter
    def position(self, pos):
        self._position = pos

    @property
    def hole_cards(self):
        return self._hole_cards

    @hole_cards.setter
    def hole_cards(self, cards):
        self._hole_cards = cards

    def get_card(self, card):
        self.hole_cards.append(card)

    def return_cards(self):
        self.hole_cards = []


    # todo: this function will differ between human and AI players - move it later
    def action(self):
        pass

    def fold(self):
        pass
        # remember to clear hole_cards[]

    def bet(self, amount):
        pass

    def check(self):
        pass

    def reraise(self, amount):
        pass



class HumanPlayer(Player):
    name = "Aaron"



class ComputerPlayer(Player):
    name = "AI"