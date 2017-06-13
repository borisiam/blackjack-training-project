import random

class StackOfCards(object):
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    values = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]
    drawn_cards = []
    number_of_cards_drawn = 0

    def draw_card_sub(self):
        card = {'suit': StackOfCards.suits[random.randint(0, 3)], 'value': StackOfCards.values[random.randint(0, 12)]}
        return card

    def draw_card(self):
        cards = []
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
                print(card)
                return card
        else:
            print('No cards left')

x = StackOfCards()
x.draw_card()
m = []
for n in range(0,100):
    m.append(x.draw_card())

print(m)