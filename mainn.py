import random


#### Classes
# - Stack Of Cards
class StackOfCards(object):
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    values = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]
    drawn_cards = []
    number_of_cards_drawn = 0

    def draw_card_sub(self):
        card = {'suit': StackOfCards.suits[random.randint(0, 3)], 'value': StackOfCards.values[random.randint(0, 12)]}
        return card

    def draw_card(self):
        card = StackOfCards().draw_card_sub()
        if StackOfCards.number_of_cards_drawn == 0:
            StackOfCards.drawn_cards.append(card)
            StackOfCards.number_of_cards_drawn += 1
            return card
        while StackOfCards.number_of_cards_drawn > 0 and StackOfCards.number_of_cards_drawn < 52:
            while card in StackOfCards.drawn_cards:
                card = StackOfCards().draw_card_sub()
            else:
                StackOfCards.drawn_cards.append(card)
                StackOfCards.number_of_cards_drawn += 1
                return card
        else:
            print('No cards left')

    def print_drawn(self):
        print(StackOfCards.drawn_cards)

    def clear(self):
        StackOfCards.drawn_cards = []


# - Player
class Player(object):
    def __init__(self, name='blank'):
        self.name = name
        self.cards = []
        self.cards1 = []
        self.bets = 0
        self.bets1 = 0
        self.insurance = 0
        self.win_amount = 0
        self.win_amount1 = 0
        self.loss_amount1 = 0
        self.loss_amount = 0

    def split(self):
        values = []
        for el in self.cards:
            values.append(el['value'])
        unique = set(values)
        for el in unique:
            values.remove(el)
        if len(values) != 0:
            self.cards1.append(self.cards[0])
            self.cards.remove(self.cards[0])
            self.bets1 += self.bets
            return 1
        else:
            print('Nothing to split!')
            return 0

    def set_name(self):
        self.name = str(input('Please enter your name here: '))

    def draw_card(self):
        self.cards.append(StackOfCards().draw_card())
        try:
            self.cards.remove(None)  # depricate later
        except:
            pass

    def draw_cards(self, int):
        if int == 1:
            self.cards.append(StackOfCards().draw_card())
        elif int == 2:
            self.cards1.append(StackOfCards().draw_card())

    def check_cards(self):
        if len(self.cards1) != 0:
            return self.cards, self.cards1
        else:
            return self.cards

    def get_name(self):
        return (self.name)

    def make_bet(self):
        print(self.name, ', please make your bet:')
        self.bets += int(input())

    def get_card(self, int):
        return (self.cards[int])

    def get_cards(self):
        if len(self.cards1) != 0:
            for el in self.cards:
                print('--<', el['suit'], el['value'], '>--')
            print('- - - - - - - - - - - - - - - - - - - - - - -')
            for el in self.cards1:
                print('--<', el['suit'], el['value'], '>--')
        else:
            for el in self.cards:
                print('--<', el['suit'], el['value'], '>--')

    def make_insurance(self):
        self.insurance += int(input())

    def add_winn_amount(self, hand, int):
        if hand == 1:
            self.win_amount += int
        elif hand == 2:
            self.win_amount1 += int

    def add_lost_amount(self, hand, int):
        if hand == 1:
            self.loss_amount += int
        elif hand == 2:
            self.loss_amount1 += int

    def get_balance(self):
        return ((self.win_amount + self.insurance) - self.loss_amount) + (self.win_amount1 - self.loss_amount1)

    def score_calc(self, hands):
        hands = int(hands)
        score = 0
        blackjack = 0
        if hands == 2:
            for el in self.cards1:
                if (el['value'] == 'K' or el['value'] == 'Q' or el['value'] == 'J') and 'A' in el.values():
                    blackjack += 1
                elif el['value'] == 'K' or el['value'] == 'Q' or el['value'] == 'J':
                    score += 10
                elif el['value'] == 'A':
                    score += 11
                elif type(el['value']) is int:
                    score += el['value']
            for el in self.cards1:
                if el['value'] == 'A' and score > 21:
                    score -= 10
            if blackjack == 1:
                return 777
            else:
                return score
        elif hands == 1:
            for el in self.cards:
                if (el['value'] == 'K' or el['value'] == 'Q' or el['value'] == 'J') and 'A' in el.values():
                    blackjack += 1
                elif el['value'] == 'K' or el['value'] == 'Q' or el['value'] == 'J':
                    score += 10
                elif el['value'] == 'A':
                    score += 11
                elif type(el['value']) is int:
                    score += el['value']
            for el in self.cards:
                if el['value'] == 'A' and score > 21:
                    score -= 10
            if blackjack == 1:
                return 777
            else:
                return score


# - Dealer
class Dealer(Player):
    def __init__(self):
        Player.__init__(self, name='Dealer')

# - Game
def game_start():
    # -variables setup
    dealer = Dealer()
    player1 = Player()
    player2 = Player()
    player3 = Player()
    player4 = Player()
    player5 = Player()
    player6 = Player()
    player7 = Player()
    removed = []
    players = [player1, player2, player3, player4, player5, player6, player7]
    number_of_players = int(input('How many people will play? :'))
    ## -- Functions --

    ## blackjack
    def blackjack_occured(n,hand):
        if hand == 1:
            print(players[n].name, 'got blackjack')
            print(players[n].name, '+',((players[n].bets * 3) / 2))
        elif hand == 2:
            print(players[n].name, 'got blackjack')
            print(players[n].name, '+',((players[n].bets1 * 3) / 2))
        if hand == 1 and hand == 2:
            removed.append(players[n])

    ## first hand looses
    def hand_lost(n, hand):
        if hand == 1:
            print(players[n].name, '1st hand have lost')
            print(players[n].name, (players[n].insurance + players[n].win_amount) - players[n].bets)
            players[n].cards = []
        elif hand == 2:
            print(players[n].name, '2nd hand have lost')
            print(players[n].name, (players[n].insurance + players[n].win_amount1) - players[n].bets1)
            players[n].cards1 = []

    ## player looses
    def player_loose(n,hand):
        if hand == 1:
            print(players[n].name, 'have lost')
            print(players[n].name, (players[n].insurance + players[n].win_amount) - players[n].bets)
        elif hand == 2:
            print(players[n].name, 'have lost')
            print(players[n].name, (players[n].insurance + players[n].win_amount) - players[n].bets1)
        if hand == 1 or hand == 2:
            removed.append(players[n])

    ## dealer gets A
    def dealer_gets_a():
        print('Ladies and gentlemen, House got Ace, are you willing to make an insurance bet?:')
        for n in range(0, number_of_players):
            print(players[n].get_name(), '( yes / no ) :')
            if str(input()) == 'yes':
                print('please enter your insurance bet :')
                players[n].make_insurance()
            else:
                continue
        dealer.draw_cards(1)
        if dealer.get_card(2) == 'A' or dealer.get_card(2) == 'K' or dealer.get_card(2) == 'Q' or dealer.get_card(
                2) == 'J' or dealer.get_card(2) == 10:
            for n in range(0, number_of_players):
                if players[n].insurance > 0:
                    players[n].add_winn_amount(players[n].insurance * 2)
                    print(players[n].name,'Gets insurance',players[n].win_amount)
        elif dealer.score_calc(1) == 777:
            print('Dealer got blackjack')
            for n in range(0, number_of_players):
                if players[n].score_calc(1) == 777:
                    print(players[n].name, 'got blackjack')
                    players[n].win_amount += ((players[n].bets * 3) / 2)
                    print(players[n].name, (players[n].insurance + players[n].win_amount) - players[n].loss_amount)
                else:
                    players[n].loss_amount += players[n].bets
            print('Game over')
            for n in range(0, number_of_players):
                print(players[n].name, (players[n].insurance + players[n].win_amount) - players[n].loss_amount)
            return 'gamover'

    ## moves circle
    def moves_circle():
        print(
            'Please make your moves. You can:  - Stand (do nothing)  - Hit (draw as many cards as you wish)  - Double(double your bet and get one more card)  - Split (if you have any 10points pair, you can split it to 2 separate hands)  - Surrender (pay half your bet and give up) ')

        for n in range(0, number_of_players):
            print(players[n].name, ', your move :')
            move = input()
            if move == 'Stand' or move == 'stand':
                continue
            elif move == 'Hit' or move == 'hit':
                while True:
                    players[n].draw_cards(1)
                    print(players[n].get_cards())
                    if players[n].score_calc(1) > 21 and players[n].score_calc(1) != 777:
                        player_loose(n,1)
                        break
                    elif players[n].score_calc(1) == 777:
                        blackjack_occured(n,1)
                        break
                    else:
                        question = str(input('one more? (yes/no)'))
                        if question == 'yes' or question == 'Yes':
                            continue
                        elif question == 'no' or question == 'No':
                            break

            elif move == 'Double' or move == 'double':
                players[n].bets *= 2
                players[n].draw_cards(1)
                print(players[n].get_cards())
                if players[n].score_calc(1) > 21:
                    player_loose(n,1)
                elif players[n].score_calc(1) == 777:
                    print(players[n].name, 'got blackjack')
                    players[n].win_amount += ((players[n].bets * 3) / 2)
                    print(players[n].name, (players[n].insurance + players[n].win_amount) - players[n].loss_amount)

             # Split start - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

            elif move == 'Split' or move == 'split':
                if players[n].split() == 1:
                    players[n].get_cards()
                    print('You can now stay, hit, double or surrender for each hand, which hand we will be working with? (1 / 2):')
                    hand = input()
                    if hand == '1':
                        print('What would you like to do?')
                        action = input(':')
                        if action == 'Stay' or action == 'stay':
                            continue
                        elif action == 'hit' or action == 'Hit':
                            while True:
                                players[n].draw_cards(1)
                                print(players[n].get_cards())
                                if players[n].score_calc(1) > 21 and players[n].score_calc(1) != 777:
                                    hand_lost(n,1)
                                    break
                                elif players[n].score_calc(1) == 777:
                                    blackjack_occured(n,1)
                                    break
                                else:
                                    question = str(input('one more? (yes / no)'))
                                    if question == 'yes' or question == 'Yes':
                                        continue
                                    elif question == 'no' or question == 'No':
                                        break

                        elif action == 'double' or action == 'Double':
                            players[n].bets *= 2
                            players[n].draw_cards(1)
                            print(players[n].get_cards())
                            players[n].score_calc(1)
                            if players[n].score_calc(1) > 21 and players[n].score_calc(1) != 777:
                                hand_lost(n,1)
                            elif players[n].score_calc(1) == 777:
                                blackjack_occured(n,1)

                        elif action == 'surrender' or action == 'Surrender':
                            print(players[n].name,'1st hand surrendered')
                            print(players[n].name, '-', players[n].bets/2, '$')
                            players[n].win_amount += players[n].bets/2
                            hand_lost(n,1)

                    elif hand == '2':
                        if action == 'Stay' or action == 'stay':
                            continue
                        elif action == 'hit' or action == 'Hit':
                            while True:
                                players[n].draw_cards(2)
                                print(players[n].get_cards())
                                if players[n].score_calc(2) > 21 and players[n].score_calc(2) != 777:
                                    hand_lost(n,2)
                                    break
                                elif players[n].score_calc(2) == 777:
                                    blackjack_occured(n,2)
                                    break
                                else:
                                    question = str(input('one more? (yes / no)'))
                                    if question == 'yes' or question == 'Yes':
                                        continue
                                    elif question == 'no' or question == 'No':
                                        break

                        elif action == 'double' or action == 'Double':
                            players[n].bets *= 2
                            players[n].draw_cards(2)
                            print(players[n].get_cards())
                            players[n].score_calc(2)
                            if players[n].score_calc(2) > 21 and players[n].score_calc(2) != 777:
                                hand_lost(n,2)
                            elif players[n].score_calc(2) == 777:
                                blackjack_occured(n,2)

                        elif action == 'surrender' or action == 'Surrender':
                            print(players[n].name,'2nd hand surrendered')
                            print(players[n].name, '-', players[n].bets1/2, '$')
                            players[n].win_amount += players[n].bets1/2
                            hand_lost(n,2)

                    print('Would you like to perform an action on other hand ? ( yes / no )')
                    qqq = input()
                    if qqq == 'Yes' or qqq == 'yes':
                        if hand == '2':
                            print('What would you like to do?')
                            action1 = input(':')
                            if action1 == 'Stay' or action == 'stay':
                                continue
                            elif action1 == 'hit' or action == 'Hit':
                                while True:
                                    players[n].draw_cards(1)
                                    print(players[n].get_cards())
                                    if players[n].score_calc(1) > 21 and players[n].score_calc(1) != 777:
                                        hand_lost(n,1)
                                        break
                                    elif players[n].score_calc(1) == 777:
                                        blackjack_occured(n,1)
                                        break
                                    else:
                                        question = str(input('one more? (yes / no)'))
                                        if question == 'yes' or question == 'Yes':
                                            continue
                                        elif question == 'no' or question == 'No':
                                            break

                            elif action1 == 'double' or action == 'Double':
                                players[n].bets *= 2
                                players[n].draw_cards(1)
                                print(players[n].get_cards())
                                players[n].score_calc(1)
                                if players[n].score_calc(1) > 21 and players[n].score_calc(1) != 777:
                                    hand_lost(n,1)
                                elif players[n].score_calc(1) == 777:
                                    blackjack_occured(n,1)

                            elif action1 == 'surrender' or action == 'Surrender':
                                print(players[n].name,'1st hand surrendered')
                                print(players[n].name, '-', players[n].bets/2, '$')
                                players[n].win_amount += players[n].bets/2
                                hand_lost(n,1)

                        elif hand == '1':
                            print('What would you like to do?')
                            action2 = input(':')
                            if action2 == 'Stay' or action == 'stay':
                                continue
                            elif action2 == 'hit' or action == 'Hit':
                                while True:
                                    players[n].draw_cards(2)
                                    print(players[n].get_cards())
                                    if players[n].score_calc(2) > 21 and players[n].score_calc(2) != 777:
                                        hand_lost(n,2)
                                        break
                                    elif players[n].score_calc(2) == 777:
                                        blackjack_occured(n,2)
                                        break
                                    else:
                                        question = str(input('one more? (yes / no)'))
                                        if question == 'yes' or question == 'Yes':
                                            continue
                                        elif question == 'no' or question == 'No':
                                            break

                            elif action2 == 'double' or action == 'Double':
                                players[n].bets *= 2
                                players[n].draw_cards(2)
                                print(players[n].get_cards())
                                players[n].score_calc(2)
                                if players[n].score_calc(2) > 21 and players[n].score_calc(2) != 777:
                                    hand_lost(n,2)
                                elif players[n].score_calc(2) == 777:
                                    blackjack_occured(n,2)

                            elif action2 == 'surrender' or action == 'Surrender':
                                print(players[n].name,'2nd hand surrendered')
                                print(players[n].name, '-', players[n].bets1/2, '$')
                                players[n].win_amount += players[n].bets1/2
                                hand_lost(n,2)


                else:
                    print('Looks like there is nothing to split, please make another move')
                    local_move = input('hit, stand, double :')
                    if local_move == 'Stand' or local_move == 'stand':
                        continue
                    elif local_move == 'Hit' or local_move == 'hit':
                        while True:
                            players[n].draw_cards(1)
                            print(players[n].get_cards())
                            if players[n].score_calc(1) > 21 and players[n].score_calc(1) != 777:
                                player_loose(n,1)
                                break
                            elif players[n].score_calc(1) == 777:
                                blackjack_occured(n,1)
                                break
                            else:
                                question = str(input('one more? (yes/no)'))
                                if question == 'yes' or question == 'Yes':
                                    continue
                                elif question == 'no' or question == 'No':
                                    break

                    elif local_move == 'Double' or local_move == 'double':
                        players[n].bets *= 2
                        players[n].draw_cards(1)
                        print(players[n].get_cards())
                        if players[n].score_calc(1) > 21:
                            player_loose(n,1)
                        elif players[n].score_calc(1) == 777:
                            print(players[n].name, 'got blackjack')
                            players[n].win_amount += ((players[n].bets * 3) / 2)
                            print(players[n].name, (players[n].insurance + players[n].win_amount) - players[n].loss_amount)

                # Split end - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

            elif move == 'surrender' or move =='Surrender':
                print(players[n].name,'surrendered')
                print(players[n].name, '-', (players[n].bets + players[n].bets1)/2, '$')
        dscore = dealer.score_calc(1)
        print('Dealers hand')
        dealer.get_cards()
        while dscore < 17:
            print('Dealers hand:')
            dealer.draw_card()
            dealer.get_cards()
            dscore = dealer.score_calc(1)
        for n in range(0, number_of_players):
            playscore = players[n].score_calc(1)
            playscore2 = players[n].score_calc(2)
            if dscore > 21 and dscore != 777:
                print('House have lost')
                print(players[n].name, ', wins :', (players[n].bets * 2) + (players[n].bets1 * 2))
            elif players[n].score_calc(1) == 777 and players[n] not in removed:
                blackjack_occured(n)
                if players[n].score_calc(2) == 777 and players[n] not in removed:
                    blackjack_occured(n)
            elif playscore2 != 0 and players[n] not in removed:
                if playscore < dscore and playscore2 < dscore or (playscore2 > 21 and playscore > 21):
                    player_loose(n,1)
                    player_loose(n,2)
                elif playscore > dscore and playscore2 < dscore:
                    print(players[n].name, ',hand 2 wins :', players[n].bets * 2)
                elif playscore < dscore and playscore2 > dscore:
                    print(players[n].name, ',hand 1 wins :', players[n].bets1 * 2)
                elif playscore > dscore and playscore2 > dscore:
                    print(players[n].name, ', both hands wins :', (players[n].bets * 2) + (players[n].bets1 * 2))
            elif players[n] not in removed:
                if playscore < dscore:
                    player_loose(n,1)
                elif playscore > dscore and playscore <= 21:
                    print(players[n].name, 'wins :', players[n].bets * 2)

        print('Game over')
        start = input('Play another game? (yes / no) :')
        if start == 'yes' or start == 'Yes':
            game_start()
        elif start == 'no' or start == 'No':
            print('Bye bye ;)')

    # ------GAME BODY-----
    for n in range(0, number_of_players):
        players[n].set_name()
    for n in range(0, number_of_players):
        players[n].make_bet()
    for n in range(0, number_of_players):
        players[n].draw_cards(1)
        players[n].draw_cards(1)
        print('2 Cards were given to', players[n].get_name())

    dealer.draw_cards(1)
    dealer.draw_cards(1)
    print('Houses also got 2 cards, first card is: --<', dealer.get_card(0)['suit'], dealer.get_card(0)['value'], '>--')

    for n in range(0, number_of_players):
        print(players[n].get_name())
        players[n].get_cards()

    if dealer.get_card(0)['value'] == 'A':
        if dealer_gets_a() == 'gamover':
            print('restarting game')
            game_start()
        else:
            moves_circle()

    else:
        moves_circle()


game_start()
