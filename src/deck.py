
from src.card import Card
import random


class Deck:

    def __init__(self):
        #self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.suits = ['h', 'd', 's', 'c']
        self.suit_color = {'hearts': 'red', 'diamonds': 'red', 'spades': 'black', 'clubs': 'black'}
        self._suit_key = {'s': 0, 'h': 1, 'd': 2, 'c': 3}
        self.deck = []
        self._create_deck()

    def _create_deck(self):
        print('creating the deck')
        for suit in self.suits:
            color = self.suit_color.get(suit)
            for rank in self.ranks:
                self.deck.append(Card(rank, suit, color))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def get_card(self):
        return self.deck.pop()

    def return_card(self, card):
        self.deck.append(card)

    @property
    def deck_size(self):
        return len(self.deck)

    @property
    def suit_key(self):
        return self._suit_key
