class Card:

    def __init__(self, rank, suit, color):
        self._rank = rank
        self._suit = suit
        self._color = color

    def __str__(self):
        return self.get_rank_str() + self.suit

    def get_rank_str(self):
        if self.rank == 14:
            return 'A'
        elif self.rank == 13:
            return 'K'
        elif self.rank == 12:
            return 'Q'
        elif self.rank == 11:
            return 'J'
        elif self.rank == 10:
            return 'T'
        else:
            return str(self.rank)

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @property
    def color(self):
        return self._color

    @property
    def info(self):
        return self.rank, self.suit, self.color

