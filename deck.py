from random import sample

class Deck:
    def __init__(self):
        self.suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
        self.values = [
            'A',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            'J',
            'Q',
            'K'
        ]

        self.suit_rank = {
            'Spades': 1,
            'Hearts': 2,
            'Clubs': 3,
            'Diamonds': 4
        }

        self.card_rank = {
            'A': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 11,
            'Q': 12,
            'K': 13
        }

        self.deck = [(i, j) for i in self.suits for j in self.values]

        self.deck = sample(self.deck, 52)

    def shuffle(self):
        self.deck = sample(self.deck, 52)
    
    def next_card_in_set(self, cards, idx):
        dealer_cards = []
        while idx < len(self.deck) and self.deck[idx] not in cards:
            dealer_cards.append(self.deck[idx])
            idx += 1
        
        if idx < len(self.deck):
            card = self.deck[idx]
        else: 
            card = ('EMPTY', 'EMPTY')
        
        return card, dealer_cards, idx+1
