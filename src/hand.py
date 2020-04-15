
# This class represents a single poker hand - the state of 1 round of the game
# This class will also be used to generate hand histories
from src.pot import Pot


class Hand:
    flop = []   # first 3 cards
    turn = []   # fourth card
    river = []  # fifth card
    community = []

    def __init__(self, table, deck, dealer_index):
        self.table = table
        self.deck = deck
        self.dealer_index = dealer_index
        self.pot = Pot(self.table, self.table)
        pass

    def end_hand(self):
        # award pot to winner, shift dealer, check if players stood up/sat down?
        pass

    def play_hand(self):
        self.collect_blinds(self.dealer_index)
        self.deck().shuffle()
        self.deal_cards(self.deck(), self.dealer_index)
        # preflop, flop and turn should return true if the hand has ended on that street due to folds
        if self.preflop():
            # award pot to winner, shift dealer, see if any players have stood up/sat down
            # allthis^stuff()
            self.end_hand()
        if self.flop():
            # award pot to winner, shift dealer, see if any players have stood up/sat down
            # allthis^stuff()
            self.end_hand()
        if self.turn():
            # award pot to winner, shift dealer, see if any players have stood up/sat down
            # allthis^stuff()
            self.end_hand()
        if self.river():
            # award pot to winner, shift dealer, see if any players have stood up/sat down
            # allthis^stuff()
            self.end_hand()
        self.showdown()


    def collect_blinds(self, dealer_index):
        if self.table.num_seated() < 2:
            # game cannot continue yet
            pass
        elif self.table.num_seated() == 2:
            # heads up case - dealer is small blind
            pass
        else:
            # player left of dealer is small blind, left of that is big blind
            pass


    def deal_cards(self, deck, dealer_index):
        # dealing starts to left of dealer
        pass


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