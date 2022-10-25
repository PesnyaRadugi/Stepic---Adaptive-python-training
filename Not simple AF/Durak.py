cards = input().split()
trump = str(input())

class Card:
    Ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    def __init__(self, rank, suit, order):
        self.rank = rank
        self.suit = suit
        self.order = order
        
    @property
    def value(self):
        val = Card.Ranks.index(self.rank)
        return val

first_card = Card(cards[0][:-1], cards[0][-1], 'First')
second_card = Card(cards[1][:-1], cards[1][-1], 'Second')

if first_card.suit == second_card.suit:
    if first_card.value > second_card.value:
        print(first_card.order)
    else:
        print(second_card.order)

else:
    if first_card.suit == trump:
        print(first_card.order)
    elif second_card.suit == trump:
        print(second_card.order)
    else:
        print('Error')