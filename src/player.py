from src.debug import Debug
import random

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
        self._street_investment = 0
        self._hand_investment = 0
        self._is_folded = False
        self._can_raise = True

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

    def hole_cards_str(self):
        return str(self.hole_cards[0]) + ', ' + str(self.hole_cards[1])

    @property
    def is_folded(self):
        return self._is_folded

    @is_folded.setter
    def is_folded(self, folded):
        self._is_folded = folded

    @property
    def can_raise(self):
        return self._can_raise

    @can_raise.setter
    def can_raise(self, r):
        self._can_raise = r

    # the amount of chips invested by this player on the current street
    @property
    def street_investment(self):
        return self._street_investment

    @street_investment.setter
    def street_investment(self, cards):
        self._street_investment = cards

    # the total amount of chips invested by this player in the current hand
    @property
    def hand_investment(self):
        return self._street_investment

    @hand_investment.setter
    def hand_investment(self, cards):
        self._hand_investment = cards

    def invest_chips(self, amt):
        self.street_investment += amt
        self.hand_investment += amt
        self.stack_size -= amt

    def move_all_in(self):
        self.invest_chips(self.stack_size)

    def return_chips(self, amt):
        self.stack_size += amt

    # antes do not contribute to current street/hand investment
    def ante(self, amt):
        self.stack_size -= amt

    def get_card(self, card):
        self.hole_cards.append(card)

    def return_cards(self, deck):
        deck.return_card(self.hole_cards[0])
        deck.return_card(self.hole_cards[1])
        self.hole_cards = []


    def action(self, total_bet, raise_amount, big_blind, closing_action):
        # get legal actions first
        action_str = input('Player ' + self.name + ' action: ')
        return action_str

    def get_legal_actions(self, total_bet, prev_raise_amount, closing_action):
        legal_actions = ['x', 'b', 'f', 'c', 'r']
        if total_bet > 0:
            legal_actions.remove('b')
        if total_bet > self.street_investment:
            legal_actions.remove('x')
        if total_bet == self.street_investment:
            legal_actions.remove('f')
            legal_actions.remove('c')
        if total_bet == 0 or total_bet >= self.street_investment + self.stack_size:
            legal_actions.remove('r')
        return legal_actions

    def generate_random_legal_action(self, total_bet, prev_raise_amount, big_blind, closing_action):
        action_str = ''
        legal_actions = self.get_legal_actions(total_bet, prev_raise_amount, closing_action)
        action_str1 = random.choice(legal_actions)
        if action_str1 == 'x':
            action_str = 'x'
        elif action_str1 == 'b':
            bet_size = 0
            if self.stack_size <= big_blind:
                bet_size = self.stack_size
            elif self.stack_size > big_blind:
                bet_size = random.randint(big_blind, self.stack_size)
            action_str2 = str(bet_size)
            action_str = action_str1 + ' ' + action_str2
        elif action_str1 == 'f':
            action_str = 'f'
        elif action_str1 == 'c':
            action_str = 'c'
        elif action_str1 == 'r':
            raise_size = 0
            if self.stack_size + self.street_investment <= total_bet + prev_raise_amount:
                raise_size = self.stack_size + self.street_investment
            elif self.stack_size + self.street_investment > total_bet + prev_raise_amount:
                raise_size = random.randint(total_bet + prev_raise_amount, self.stack_size + self.street_investment)
            action_str2 = str(raise_size)
            action_str = action_str1 + ' ' + action_str2
        return action_str


class HumanPlayer(Player):

    def __init__(self, name):
        self._name = name
        self._positions = ['BU', 'SB', 'BB', 'UTG', 'HJ', 'CO']
        self._position = ''
        self._stack_size = 200
        self._hole_cards = []
        self._street_investment = 0
        self._hand_investment = 0
        self._is_human = True
        self._can_raise = True

    def action(self, total_bet, raise_amount, big_blind, closing_action):
        action_prompt = Debug.create_action_prompt(self)
        action_str = input(action_prompt)
        return action_str

    @property
    def is_human(self):
        return self._is_human


# AI that will simply take random actions on every turn
class RandomComputerPlayer(Player):

    def __init__(self, name):
        self._name = name
        self._positions = ['BU', 'SB', 'BB', 'UTG', 'HJ', 'CO']
        self._position = ''
        self._stack_size = 200
        self._hole_cards = []
        self._street_investment = 0
        self._hand_investment = 0
        self._is_human = False
        self._can_raise = True

    def action(self, total_bet, raise_amount, big_blind, closing_action):
        # take a random action from legal options
        action_str = self.generate_random_legal_action(total_bet, raise_amount, big_blind, closing_action)
        #print('Player ' + self.name + ' action: ' + action_str)
        return action_str

    @property
    def is_human(self):
        return self._is_human