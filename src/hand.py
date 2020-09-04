
# This class represents a single poker hand - the state of 1 round of the game
# This class will also be used to generate hand histories
from src.pot import Pot
from src.deck import Deck


class Hand:
    flop = []   # first 3 cards
    turn = []   # fourth card
    river = []  # fifth card
    community = []

    def __init__(self, table, deck, dealer_index, players):
        self.table = table
        self._deck = deck
        self.dealer_index = dealer_index
        self.players = players
        self.pot = Pot(self.table, self.players)

    @property
    def deck(self):
        return self._deck

    def end_hand(self):
        # award pot to winner, record hand
        pass

    def play_hand(self):
        self.collect_blinds(self.dealer_index)
        self.stack_sizes()
        self.deck.shuffle()
        self.deal_cards()

        self.return_cards()
        # preflop, flop and turn should return true if the hand has ended on that street due to folds
        #if self.preflop():
            # award pot to winner, shift dealer, see if any players have stood up/sat down
            # allthis^stuff()
        #    self.end_hand()
        #if self.flop():
            # award pot to winner, shift dealer, see if any players have stood up/sat down
            # allthis^stuff()
        #    self.end_hand()
        #if self.turn():
            # award pot to winner, shift dealer, see if any players have stood up/sat down
            # allthis^stuff()
        #    self.end_hand()
        #if self.river():
            # award pot to winner, shift dealer, see if any players have stood up/sat down
            # allthis^stuff()
        #    self.end_hand()
        #self.showdown()


    def stack_sizes(self):
        for p in self.players:
            print(p.name + ': ' + str(p.stack_size))

    def collect_blinds(self, dealer_index):
        self.pot.collect_blinds()
        #if self.table.num_seated() < 2:
            # game cannot continue yet
        #    pass
        #elif self.table.num_seated() == 2:
            # heads up case - dealer is small blind
        #    pass
        #else:
            # player left of dealer is small blind, left of that is big blind
        #    pass


    def deal_cards(self):
        for c in range(2):
            for p in self.players:
                p.get_card(self.deck.get_card())
        self.print_cards()

    def return_cards(self):
        for p in self.players:
            p.return_cards()

    def print_cards(self):
        for p in self.players:
            print(p.name + ':  (' + str(p.hole_cards[0]) + ', ' + str(p.hole_cards[1]) + ')')


    def preflop(self, deck, dealer_index):
        # preflop action starts from left of big blind
        # return true
        pass


    def flop(self):
        pass


    def turn(self):
        pass


    def river(self):
        pass


    def showdown(self):
        pass

    def get_next_to_act(self, current_index, num_players):
        # handle incorrect input params
        if current_index + 1 == num_players:
            return 0
        else:
            return current_index + 1