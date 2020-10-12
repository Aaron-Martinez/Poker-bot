
# This (maybe temporary) file is just to separate all methods which help me print out or debug different game states

#from src.hand import Hand
#from src.player import Player
from src.pot import Pot


class Debug:

    #mode = 'debug'
    mode = 'play'

    @staticmethod
    def print_remaining_active_players(players):
        players_str = ''
        if len(players) > 0:
            players_str = 'Remaining players: (' + players[0].name
        for i in range(1, len(players)):
            players_str += ', ' + players[i].name
        players_str += ')'
        print(players_str)


    @staticmethod
    def create_action_prompt(player):
        action_prompt = '[' + str(player.stack_size) + '] Player ' + player.name + ' (' + player.position + ')'
        action_prompt += ' (' + player.hole_cards_str() + ')   ACTION: '
        return action_prompt


    @staticmethod
    def print_cards(players):
        if Debug.mode == 'play':
            for p in players:
                if p.is_human:
                    print(p.name + ', you were dealt  (' + p.hole_cards_str() + ')')
        elif Debug.mode == 'debug':
            for p in players:
                print(p.name + ':  (' + p.hole_cards_str() + ')')


    @staticmethod
    def print_community(hand, new_cards_str):
        print(hand.streets[hand.street] + ': ' + new_cards_str + ' | pot size: ' + str(hand.pot.total))
