import random
from deck import Deck
from poker_ranker import PokerRanker
import copy

class RenjiePoker:
    def __init__(self):
        self.deck = Deck()
        self.card_to_id = {}
        self.id_to_card = {}
        self.dealer_cards = []
        self.idx = 0
        self.player_cards = []
        self.hand_rank = PokerRanker()

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

        i = 0

        for suit in self.suits:
            for val in self.values:
                self.card_to_id[(suit, val)] = i
                self.id_to_card[i] = (suit, val)
                i += 1

    def take_turn(self, cards):
        card, dealer_cards, idx = self.deck.next_card_in_set(cards, self.idx)
        if card != ('EMPTY', 'EMPTY'):
            self.player_cards.append(card)

        self.dealer_cards = self.dealer_cards + dealer_cards
        self.idx = idx

        print(f"your cards: {card}")
        print("dealer cards:")
        for c in self.dealer_cards:
            print(c)
        print(f"cards left: {52 - self.idx}")

    def get_move(self):
        print("input move")
        temp = input()

        temp = temp.split(" ")

        cards = []

        for i in range(0, len(temp), 2):
            cards.append((temp[i], temp[i+1]))

        return cards
    
    def determine_winner(self):
        player_value = self.hand_rank.get_hand_rank(self.player_cards)

        player_spades, player_hearts, player_clubs, player_diamonds, player_aces, player_twos, \
            player_threes, player_fours, player_fives, player_sixes, player_sevens, player_eights, player_nines, \
                player_tens, player_jacks, player_queens, player_kings = self.hand_rank.sort_cards(self.player_cards)
        
        player_card_input = [player_aces, player_twos, player_threes, player_fours, player_fives,
                             player_sixes, player_sevens, player_eights, player_nines, player_tens, player_jacks,
                             player_queens, player_kings]
        
        dealer_spades, dealer_hearts, dealer_clubs, dealer_diamonds, dealer_aces, dealer_twos, \
            dealer_threes, dealer_fours, dealer_fives, dealer_sixes, dealer_sevens, dealer_eights, dealer_nines, \
                dealer_tens, dealer_jacks, dealer_queens, dealer_kings = self.hand_rank.sort_cards(self.dealer_cards)
        
        dealer_card_input = [dealer_aces, dealer_twos, dealer_threes, dealer_fours, dealer_fives,
                             dealer_sixes, dealer_sevens, dealer_eights, dealer_nines, dealer_tens, dealer_jacks,
                             dealer_queens, dealer_kings]

        if player_value == 1:
            player_straight_flush = self.hand_rank.get_straight_flushes(player_spades, player_hearts, player_clubs, player_diamonds)
            dealer_straight_flush = self.hand_rank.get_straight_flushes(dealer_spades, dealer_hearts, dealer_clubs, dealer_diamonds)

            if len(dealer_straight_flush) == 0:
                return 1
        
            if dealer_straight_flush[0] >= player_straight_flush[0]:
                return 0
            return 1
        
        if player_value == 2:
            dealer_straight_flush = self.hand_rank.get_straight_flushes(dealer_spades, dealer_hearts, dealer_clubs, dealer_diamonds)
            if len(dealer_straight_flush) > 0:
                return 0
            player_quads = self.hand_rank.get_four_of_a_kind(player_card_input)
            dealer_quads = self.hand_rank.get_four_of_a_kind(dealer_card_input)

            if len(dealer_quads) == 0:
                return 1
            if dealer_quads[0] >= player_quads[0]:
                return 0
            return 1
        
        if player_value == 3:
            dealer_straight_flush = self.hand_rank.get_straight_flushes(dealer_spades, dealer_hearts, dealer_clubs, dealer_diamonds)
            if len(dealer_straight_flush) > 0:
                return 0
            dealer_quads = self.hand_rank.get_four_of_a_kind(dealer_card_input)

            if len(dealer_quads) > 0:
                return 0
            
            player_full_house = self.hand_rank.get_full_house(player_card_input)
            dealer_full_house = self.hand_rank.get_full_house(dealer_card_input)

            if len(dealer_full_house) == 0:
                return 1
            if dealer_full_house[0] >= player_full_house[0]:
                return 0
            return 1
        
        if player_value == 4:
            dealer_straight_flush = self.hand_rank.get_straight_flushes(dealer_spades, dealer_hearts, dealer_clubs, dealer_diamonds)
            if len(dealer_straight_flush) > 0:
                return 0
            dealer_quads = self.hand_rank.get_four_of_a_kind(dealer_card_input)

            if len(dealer_quads) > 0:
                return 0
            dealer_full_house = self.hand_rank.get_full_house(dealer_card_input)

            if len(dealer_full_house) > 0:
                return 0
            
            player_flush = self.hand_rank.get_flush(player_spades, player_hearts, player_clubs, player_diamonds)
            dealer_flush = self.hand_rank.get_flush(dealer_spades, dealer_hearts, dealer_clubs, dealer_diamonds)

            if len(dealer_flush) == 0:
                return 1
            
            if dealer_flush[0] >= player_flush[0]:
                return 0
            return 1
        
        if player_value >= 5:
            dealer_straight_flush = self.hand_rank.get_straight_flushes(dealer_spades, dealer_hearts, dealer_clubs, dealer_diamonds)
            if len(dealer_straight_flush) > 0:
                return 0
            dealer_quads = self.hand_rank.get_four_of_a_kind(dealer_card_input)

            if len(dealer_quads) > 0:
                return 0
            dealer_full_house = self.hand_rank.get_full_house(dealer_card_input)

            if len(dealer_full_house) > 0:
                return 0
            dealer_flush = self.hand_rank.get_flush(dealer_spades, dealer_hearts, dealer_clubs, dealer_diamonds)
            if len(dealer_flush) > 0:
                return 0
            
            return self.hand_rank.get_compare_hands(self.player_cards, self.dealer_cards)




    def play_game(self):
        while len(self.player_cards) < 5 and self.idx < len(self.deck.deck):
            cards = self.get_move()
            self.take_turn(cards)

        n = len(self.dealer_cards)
        print("player hand: ")

        print(self.player_cards)
        print("dealer cards: ")
        for i in range(n):
            print(self.dealer_cards[i])

        winner = self.determine_winner()

        if winner == 1:              
            print("player wins")
            return 1
        
        else:
            print("dealer wins")
            return 0
        
    def simple_simulation_setup(self, moves, setup=False):
        if setup:
            self.player_cards = []
            self.dealer_cards = []
            self.deck.shuffle()

            self.idx = 5 - moves

            self.player_cards = self.deck.deck[0:self.idx]

            r = random.randint(self.idx, 51)

            self.dealer_cards = self.deck.deck[self.idx:r]

            self.idx = r

        player_cards = [0]*52
        dealer_cards = [0]*52

        player_spades = [0]*13
        player_hearts = [0]*13
        player_clubs = [0]*13
        player_diamonds = [0]*13

        player_ranks = [0]*13
        player_straight = [0]*13

        dealer_spades = [0]*13
        dealer_hearts = [0]*13
        dealer_clubs = [0]*13
        dealer_diamonds = [0]*13

        dealer_ranks = [0]*13
        dealer_straight = [0]*13

        for card in self.player_cards:
            player_cards[self.card_to_id[card]] = 1
            if card[0] == "Spades":
                player_spades[self.deck.card_rank[card[1]] - 1] = 1
            elif card[0] == "Hearts":
                player_hearts[self.deck.card_rank[card[1]] - 1] = 1
            elif card[0] == "Clubs":
                player_clubs[self.deck.card_rank[card[1]] - 1] = 1
            elif card[0] == "Diamonds":
                player_diamonds[self.deck.card_rank[card[1]] - 1] = 1
            
            player_ranks[self.deck.card_rank[card[1]] - 1] += 1
            player_straight[self.deck.card_rank[card[1]] - 1] = 1

        
        
        for card in self.dealer_cards:
            dealer_cards[self.card_to_id[card]] = 1
            if card[0] == "Spades":
                dealer_spades[self.deck.card_rank[card[1]] - 1] = 1
            elif card[0] == "Hearts":
                dealer_hearts[self.deck.card_rank[card[1]] - 1] = 1
            elif card[0] == "Clubs":
                dealer_clubs[self.deck.card_rank[card[1]] - 1] = 1
            elif card[0] == "Diamonds":
                dealer_diamonds[self.deck.card_rank[card[1]] - 1] = 1
            
            dealer_ranks[self.deck.card_rank[card[1]] - 1] += 1
            dealer_straight[self.deck.card_rank[card[1]] - 1] = 1

        # print(f"player cards: {self.player_cards}")
        # print(f"coded player cards: {player_cards}")
        # print(f"dealer cards: {self.dealer_cards}")
        # print(f"coded dealer cards: {dealer_cards}")

        # print(f"player spades: {player_spades}")
        # print(f"player hearts: {player_hearts}")
        # print(f"player clubs: {player_clubs}")
        # print(f"player diamonds: {player_diamonds}")

        # print(f"player ranks: {player_ranks}")
        # print(f"player straight: {player_straight}")

        # print(f"dealer spades: {dealer_spades}")
        # print(f"dealer hearts: {dealer_hearts}")
        # print(f"dealer clubs: {dealer_clubs}")
        # print(f"dealer diamonds: {dealer_diamonds}")

        # print(f"dealer ranks: {dealer_ranks}")
        # print(f"dealer straight: {dealer_straight}")

        return [player_cards, player_spades, player_hearts, player_clubs, player_diamonds, player_ranks, player_straight, dealer_cards, dealer_spades, dealer_hearts, dealer_clubs, dealer_diamonds, dealer_ranks, dealer_straight]

        

    def simulation_move(self, cards):
        temp_deck = copy.deepcopy(self.deck)
        temp_idx = copy.deepcopy(self.idx)
        temp_player_cards = copy.deepcopy(self.player_cards)
        temp_dealer_cards = copy.deepcopy(self.dealer_cards)

        while self.idx < 52 and cards[self.card_to_id[self.deck.deck[self.idx]]] == 0:
            self.dealer_cards.append(self.deck.deck[self.idx])
            self.idx += 1

        if self.idx < 52:
            self.player_cards.append(self.deck.deck[self.idx])
            self.idx += 1

        while len(self.dealer_cards) < 8:
            self.dealer_cards.append(self.deck.deck[self.idx])
            self.idx += 1
        # try:
        #     winner = self.determine_winner()
        # except:
        #     print(self.player_cards)
        #     print(self.dealer_cards)
        #     assert False

        winner = self.determine_winner()

        self.deck = temp_deck
        self.idx = temp_idx
        self.player_cards = temp_player_cards
        self.dealer_cards = temp_dealer_cards

        if winner == 1:
            return 1
        return 0
    
    def create_game_state(self, player_cards, idx=-1):
        self.player_cards = player_cards
        self.deck.shuffle()
        self.dealer_cards = []

        p = 0

        for i in range(52):
            if self.deck.deck[p] in self.player_cards:
                self.deck.deck[i], self.deck.deck[p] = self.deck.deck[p], self.deck.deck[i]
                p += 1

        if idx == -1:
            self.idx = random.randint(len(player_cards, 51))
        self.dealer_cards = self.deck.deck[len(player_cards): self.idx]

    # def create_straight_flush




        

        



        