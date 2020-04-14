
class Player:
    stack_size = 10000
    is_small_blind = False
    is_big_blind = False
    is_seated = True
    hole_cards = []

    def __init__(self):
        pass

    def __init__(self, name):
        self._name = name

    @property
    def is_seated(self):
        return self.is_seated

    @property
    def name(self):
        return self._name

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