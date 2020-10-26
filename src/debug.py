# This (maybe temporary) file is just to separate all methods which help me print out or debug different game states


class Debug:

    # mode = 'debug'
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
        action_prompt = '(' + player.position + ') player ' + player.name + '[' + str(player.stack_size) + ']'
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
        #print(hand.streets[hand.street] + ': ' + new_cards_str + '  | pot size: ' + str(hand.pot.total))
        print(Debug.log_str_community(hand))

    @staticmethod
    def log_str_community(hand):
        community_str = hand.streets[hand.street] + ': '
        for i in range(1, hand.street):
            for c in range(hand.community_cards_num[i]):
                community_str += str(hand.community[i][c]) + ' '
        new_cards = '['
        for c in range(hand.community_cards_num[hand.street]):
            new_cards += str(hand.community[hand.street][c]) + ' '
        new_cards = new_cards.strip() + ']'
        community_str += new_cards + '  | pot size: ' + str(hand.pot.total)
        return community_str


    @staticmethod
    def print_card_list(card_list):
        if Debug.mode == 'debug':
            cards_str = '(' + str(card_list[0])
            for card in card_list[1:]:
                cards_str += ', ' + str(card)
            cards_str += ')'
            print('Cards list: ' + cards_str)

    @staticmethod
    def print_card_keys(keys):
        if Debug.mode == 'debug':
            keys_str = ''
            for key in keys:
                keys_str += str(key) + ' '
            print('Card integer keys: ' + keys_str)


    @staticmethod
    def print_winners(winners):
        win_str = ''
        for p in winners:
            win_str += p.name + ' '
        print('Winners of the hand are: ' + win_str)


    @staticmethod
    def print_final_board(community):
        community_str = str(community[1][0]) + ', ' + str(community[1][1]) + ', ' + str(community[1][2])
        community_str += ', ' + str(community[2][0]) + ', ' + str(community[3][0])
        print('\n*** FINAL BOARD IS:  (' + community_str + ') ***')

    @staticmethod
    def log_str_check(player):
        check_str = player.name + ' (' + player.position + ') checks'
        return check_str

    @staticmethod
    def log_str_fold(player):
        fold_str = player.name + ' (' + player.position + ') folds'
        return fold_str

    @staticmethod
    def log_str_bet(player, amount):
        bet_str = player.name + ' (' + player.position + ') bets '
        if amount == player.stack_size:
            bet_str += 'all in for '
        bet_str += str(amount)
        return bet_str

    @staticmethod
    def log_str_call(player, total_bet):
        call_str = player.name + ' (' + player.position + ') calls '
        if player.stack_size <= total_bet - player.street_investment:
            call_str += 'all in '
        call_str += str(total_bet)
        return call_str

    @staticmethod
    def log_str_raise(player, amount):
        raise_str = player.name + ' (' + player.position + ') raises '
        if amount == player.stack_size + player.street_investment:
            raise_str += 'all in '
        raise_str += 'to ' + str(amount)
        return raise_str

    @staticmethod
    def log_str_post_sb(player, sb):
        sb_str = player.name + ' (' + player.position + ') posts small blind ' + str(sb)
        return sb_str

    @staticmethod
    def log_str_post_bb(player, bb):
        bb_str = player.name + ' (' + player.position + ') posts big blind ' + str(bb)
        return bb_str

    @staticmethod
    def log_str_blinds_allin(player):
        s = player.name + ' (' + player.position + ') is all in for ' + str(player.stack_size)
        return s

    @staticmethod
    def log_str_win_non_showdown(player, pot):
        s = player.name + ' (' + player.position + ') wins pot of ' + str(pot.total) + ' before showdown'
        return s

    @staticmethod
    def log_str_win_showdown(player, amt):
        s = player.name + ' (' + player.position + ') wins ' + str(amt) + ' at showdown'
        return s

    @staticmethod
    def log_str_win_leftover(player, amt):
        s = player.name + ' (' + player.position + ') chosen to win leftover amount from split pot: ' + str(amt)
        return s