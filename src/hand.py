
# This class represents a single poker hand - the state of 1 round of the game
# This class will also be used to generate hand histories
from src.pot import *
from src.deck import Deck
from src.debug import Debug
import copy
import random


class Hand:
    #flop = []   # first 3 cards
    #turn = []   # fourth card
    #river = []  # fifth card
    community = []
    community_cards_num = [0, 3, 1, 1]
    streets = ['preflop', 'flop', 'turn', 'river']

    def __init__(self, table, deck, dealer_index, players):
        self.table = table
        self._deck = deck
        self.dealer_index = dealer_index
        self.players = players
        self.active_players = copy.copy(self.players)
        self.pot = Pot(self.table, self.players)
        self._street = 0
        self._flop = []
        self._turn = []
        self._river = []
        self._community = [[], self._flop, self._turn, self._river]
        self._hand_log = None

    @property
    def deck(self):
        return self._deck

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, st):
        self._street = st

    @property
    def community(self):
        return self._community

    @property
    def hand_log(self):
        return self._hand_log

    # pot should be awarded to winner(s) before this method
    def end_hand(self):
        self.community.clear()
        self.reset_current_street_investment()
        self.reset_current_hand_investment()
        for p in self.players:
            p.is_folded = False

    def play_hand(self):
        self.collect_blinds(self.dealer_index)
        #self.stack_sizes()
        self.deck.shuffle()
        self.deal_cards()
        is_hand_finished = self.preflop()
        if not is_hand_finished:
            self.postflop()
        self.return_cards()



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
        Debug.print_cards(self.players)

    def deal_community_cards(self):
        new_cards_str = ''
        for c in range(self.community_cards_num[self.street]):
            self.community[self.street].append(self.deck.get_card())
            if c > 0:
                new_cards_str += ', '
            new_cards_str += str(self.community[self.street][c])
        #print(self.streets[self.street] + ': ' + new_cards_str)
        Debug.print_community(self, new_cards_str)



    def return_cards(self):
        for p in self.players:
            p.return_cards(self.deck)
        for st in range(len(self.community)):
            for c in range(len(self.community[st])):
                self.deck.return_card(self.community[st][c])

    def print_cards(self):
        for p in self.players:
            print(p.name + ':  (' + str(p.hole_cards[0]) + ', ' + str(p.hole_cards[1]) + ')')


    def preflop(self):
        print('\n*** beginning preflop action ***')
        # preflop action starts from left of big blind
        is_hand_finished = self.betting_round(2, self.table.big_blind)
        if is_hand_finished:
            self.end_hand()
        else:
            self.reset_current_street_investment()
        return is_hand_finished

    def postflop(self):
        print('\n*** beginning postflop action ***')
        self.street += 1
        #for loop for postflop
        while self.street <= 3:
            self.deal_community_cards()
            #print('*** beginning ' + self.streets[self.street] + ' action ***')
            Debug.print_remaining_active_players(self.active_players)
            is_hand_finished = self.betting_round(0, 0)
            if is_hand_finished:
                self.end_hand()
                return
            else:
                self.reset_current_street_investment()
                #print('*** end of ' + self.streets[self.street] + ' action ***')
                self.street += 1
        self.showdown()
        return is_hand_finished

    def betting_round(self, first_to_act_idx, total_bet):
        is_hand_finished = False
        more_action = True
        turn_player_idx = first_to_act_idx
        raise_amount = total_bet
        last_to_act = self.active_players[first_to_act_idx-1]
        any_allins = False
        allins = []
        #print('last to act is ' + last_to_act.name)
        while more_action:
            active_player = self.active_players[turn_player_idx]
            closing_action = False
            if active_player is last_to_act:
                closing_action = True
            action = active_player.action(total_bet, raise_amount, self.table.big_blind, closing_action)
            action_arr = action.split()
            if action_arr[0].casefold() == 'x' or action_arr[0].casefold() == 'k' or action_arr[0].casefold() == 'check':
                if total_bet > active_player.street_investment:
                    print('Cannot check if facing a bet/raise. Try again')
                    continue
                self.check(active_player)
                if active_player is last_to_act:
                    more_action = False
            elif action_arr[0] == 'b' or action_arr[0].casefold() == 'bet':
                amt = int(action_arr[1])
                if total_bet > 0:
                    print('Raise instead of bet if facing a bet. Try again')
                    continue
                elif amt > active_player.stack_size:
                    print('Cannot bet more than current stack. Try again')
                    continue
                elif amt < self.table.big_blind <= active_player.stack_size:
                    print('Minimum bet is 1 big blind: ' + str(self.table.big_blind) + '. Try again')
                    continue
                total_bet = amt
                raise_amount = amt
                self.bet(active_player, amt)
                last_to_act = self.active_players[turn_player_idx-1]
            elif action_arr[0].casefold() == 'f' or action_arr[0].casefold() == 'fold':
                self.fold(active_player)
                if active_player is last_to_act:
                    more_action = False
            elif action_arr[0] == 'c' or action_arr[0].casefold() == 'call':
                if total_bet == active_player.street_investment:
                    print('Not facing a bet or raise. Valid actions are check(x), bet(b) or fold(f)')
                    continue
                self.call(active_player, total_bet)
                if active_player is last_to_act:
                    more_action = False
            elif action_arr[0] == 'r' or action_arr[0].casefold() == 'raise':
                amt = int(action_arr[1])
                full_raise = True
                if total_bet == 0:
                    print('Cannot reraise if there is no bet. Try again')
                    continue
                if amt - total_bet < raise_amount:
                    if active_player.stack_size + active_player.street_investment > amt:
                        print('Must raise current bet by at least ' + str(raise_amount) + '. Try again')
                        continue
                    else:
                        if amt == active_player.stack_size + active_player.street_investment:
                            full_raise = False
                if full_raise:
                    raise_amount = amt - total_bet
                total_bet = amt
                self.reraise(active_player, amt)
                if full_raise:
                    last_to_act = self.active_players[turn_player_idx - 1]
            if len(self.active_players) == 0 or len(self.active_players) == 1 and active_player is last_to_act:
                if len(self.pot.allin_players) > 0:
                    self.showdown()
                else:
                    self.non_showdown()
                is_hand_finished = True
                more_action = False
                break
            #elif len(self.active_players) == 1 and len(self.pot.allin_players) == 0:
            #    self.non_showdown()
            #    is_hand_finished = True
            #    more_action = False
            #    break
            if active_player not in self.active_players:
                turn_player_idx -= 1
            if turn_player_idx + 1 == len(self.active_players):
                turn_player_idx = 0
            else:
                turn_player_idx += 1
        # create sidepots if necessary
        if any_allins and not is_hand_finished:
            p_sorted = [allins[0]]
            for p in self.active_players:
                inserted = False
                for i in range(len(p_sorted)):
                    if p.street_investment < p_sorted[i].street_investment:
                        p_sorted.insert(i, p)
                if not inserted:
                    p_sorted.append(p)
            for p in allins:
                inserted = False
                for i in range(len(p_sorted)):
                    if p.street_investment < p_sorted[i].street_investment:
                        p_sorted.insert(i, p)
                if not inserted:
                    p_sorted.append(p)
            num_sidepots = 0
            for i in range(0, len(p_sorted) - 1):
                if p_sorted[i].street_investment < p_sorted[i+1].street_investment:
                    difference = p_sorted[i+1].street_investment - p_sorted[i].street_investment
                    sidepot = SidePot(self.pot, p_sorted[i+1:])
                    for p in p_sorted[i+1:]:
                        Pot.transfer_chips(self.pot, sidepot)
                    self.pot.add_side_pot(sidepot)
                    num_sidepots += 1
            # if no chip transfers are necessary then there is only one new sidepot with remaining active players
            if num_sidepots == 0:
                sidepot = SidePot(self.pot, self.active_players)
                self.pot.add_side_pot(sidepot)
        return is_hand_finished


    def check(self, player):
        print('player ' + player.name + ' (' + player.position + ') checks')

    def bet(self, player, amount):
        if amount == player.stack_size:
            print('player ' + player.name + ' (' + player.position + ') bets all in for ' + str(amount))
            self.pot.move_all_in(player)
            self.active_players.remove(player)
        else:
            print('player ' + player.name + ' (' + player.position + ') bets ' + str(amount))
            self.pot.invest_chips(player, amount)

    def fold(self, player):
        print('player ' + player.name + ' (' + player.position + ') folds')
        #print('Removing ' + player.name + ' from active players')
        self.active_players.remove(player)
        player.is_folded = True

    def call(self, player, total_bet):
        if player.stack_size <= total_bet - player.street_investment:
            print('player ' + player.name + ' (' + player.position + ') calls all in')
            self.pot.move_all_in(player)
            self.active_players.remove(player)
        else:
            print('player ' + player.name + ' (' + player.position + ') calls remaining ' + str(total_bet - player.street_investment))
            self.pot.invest_chips(player, total_bet - player.street_investment)

    def reraise(self, player, amount):
        if amount == player.stack_size + player.street_investment:
            print('player ' + player.name + ' (' + player.position + ') raises all in to ' + str(amount))
            self.pot.move_all_in(player)
            self.active_players.remove(player)
        else:
            print('player ' + player.name + ' (' + player.position + ') raises to ' + str(amount))
            self.pot.invest_chips(player, amount - player.street_investment)

    def flop(self):
        self.deal_community_cards(3)
        print('FLOP: ' + str(self.community[0]) + ', ' + str(self.community[1]) + ', ' + str(self.community[2]))
        print('*** beginning flop action ***')


    def turn(self):
        self.deal_community_cards(1)
        print('TURN: ' + str(self.community[3]))
        print('*** beginning turn action ***')


    def river(self):
        self.deal_community_cards(1)
        print('RIVER: ' + str(self.community[4]))
        print('*** beginning river action ***')

    # reset the amt invested on current street by each player when moving to the next street
    def reset_current_street_investment(self):
        for p in self.players:
            p.street_investment = 0


    # reset the amt invested on current hand by each player when moving to the next hand
    def reset_current_hand_investment(self):
        for p in self.players:
            p.hand_investment = 0


    def non_showdown(self):
        if len(self.active_players) != 1:
            print('Error in non_showdown, ' + str(len(self.active_players)) + ' active players left')
        else:
            active_bet = self.active_players[0].street_investment
            previous_bet = 0
            for p in self.players:
                if p is not self.active_players[0]:
                    if p.street_investment > previous_bet:
                        previous_bet = p.street_investment
            self.pot.return_chips(self.active_players[0], active_bet - previous_bet)
            print('Player ' + self.active_players[0].name + ' wins pot of ' + str(self.pot.total) + ' before showdown')


    def showdown(self):
        print('Got to showdown. Number of sidepots = ' + str(len(self.pot.side_pots)))
        # handle side pots first
        while len(self.pot.side_pots) > 0:
            side_pot = self.pot.side_pots.pop()
            winners = self.determine_winners(side_pot)
            self.award_pot(side_pot, winners)
        # award main pot
        self.award_pot(self.pot, self.determine_winners(self.pot))


    def determine_winners(self, pot):
        winners = []
        hand_ranks = {}
        for p in pot.players:
            hand_ranks[p] = self.rank_hand(p)
        for k in hand_ranks.keys():
            if not winners or hand_ranks[k] > hand_ranks[winners[0]]:
                winners = [k]
            elif hand_ranks[k] == hand_ranks[winners[0]]:
                winners.append(k)
        return winners

    def rank_hand(self, player):
        # dummy method for now
        print('Player ' + player.name + ' hand: ' + player.hole_cards_str())
        rank = random.randint(0, 100)
        return rank


    def award_pot(self, pot, winners):
        if len(winners) > 1:
            amount_won = int(pot.total / len(winners))
            leftover = pot.total - (amount_won * len(winners))
            for p in winners:
                pot.return_chips(p, amount_won)
            pot.return_chips(random.choice(winners), leftover)
        else:
            pot.return_chips(winners[0], pot.total)

