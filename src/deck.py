
from src.card import Card
import random


class Deck:

    def __init__(self):
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = ['hearts', 'diamonds', 'spades', 'clubs']
        self.suit_color = {'hearts': 'red', 'diamonds': 'red', 'spades': 'black', 'clubs': 'black'}
        self.deck = []
        self._create_deck()
        pass

    def _create_deck(self):
        for suit in self.suits:
            color = self.suit_color.get(suit)
            for rank in self.ranks:
                self.deck.append(Card(rank, suit, color))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def get_card(self):
        return self.deck.pop()

    @property
    def deck_size(self):
        return len(self.deck)

