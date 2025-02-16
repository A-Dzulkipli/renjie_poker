class PokerRanker:
    def __init__(self):
        self.ranking = {
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
        self.ranks = [
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

        self.number_to_rank = {
            1: 'A',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10',
            11: 'J',
            12: 'Q',
            13: 'K'
        }

    def rank_cards(self, hand):
        ranks = sorted([self.ranking[card[1]] for card in hand])

        return ranks
    
    def check_straight(self, hand):
        if len(hand) != 5:
            return False
        ranks = self.rank_cards(hand)

        if ((ranks[4] - ranks[0] == 4) or ((ranks[4] - ranks[1] == 3) and (ranks[4] == 13) and (ranks[0] == 1))):
            return True
        return False
    
    def check_flush(self, hand):
        if len(hand) != 5:
            return False
        suits = {card[0] for card in hand}

        if len(suits) == 1:
            return True
        return False
    
    def check_four_of_a_kind(self, hand):
        ranks = [card[1] for card in hand]

        count = {}

        for r in ranks:
            if r in count:
                count[r] += 1
            else:
                count[r] = 1
        
        for (key, value) in count.items():
            if value == 4:
                return True
        return False
    
    def check_full_house(self, hand):
        ranks = [card[1] for card in hand]

        count = {}

        for r in ranks:
            if r in count:
                count[r] += 1
            else:
                count[r] = 1

        two = False
        three = False

        for (key, value) in count.items():
            if value == 2:
                two = True
            if value == 3:
                three = True
            if (value != 2) and (value != 3):
                return False
        
        if len(count.items()) != 2:
            return False
        if two and three:
            return True
        return False
    
    def check_three_of_a_kind(self, hand):
        ranks = [card[1] for card in hand]

        count = {}

        for r in ranks:
            if r in count:
                count[r] += 1
            else:
                count[r] = 1

        mx = 0
        is_two = False

        for (key, val) in count.items():
            mx = max(mx, val)
            if val == 2:
                is_two = True

        if mx == 3 and  not is_two:
            return True
        return False
    
    def check_two_pair(self, hand):
        ranks = [card[1] for card in hand]

        count = {}

        for r in ranks:
            if r in count:
                count[r] += 1
            else:
                count[r] = 1

        mx = 0

        twos = 0

        for (key, val) in count.items():
            mx = max(mx, val)
            if val == 2:
                twos += 1

        if twos == 2 and mx == 2:
            return True
        
        return False

    
    def check_pair(self, hand):
        ranks = [card[1] for card in hand]

        count = {}

        for r in ranks:
            if r in count:
                count[r] += 1
            else:
                count[r] = 1

        mx = 0
        twos = 0

        for (key, val) in count.items():
            mx = max(mx, val)
            if val == 2:
                twos += 1

        if mx == 2 and twos == 1:
            return True
        return False
    
    def get_hand_rank(self, hand):
        if self.check_flush(hand) and self.check_straight(hand):
            return 1
        
        if self.check_four_of_a_kind(hand):
            return 2
        
        if self.check_full_house(hand):
            return 3
        
        if self.check_flush(hand):
            return 4
        
        if self.check_straight(hand):
            return 5
        
        if self.check_three_of_a_kind(hand):
            return 6
        
        if self.check_two_pair(hand):
            return 7

        if self.check_pair(hand):
            return 8
        
        return 9
    
    def compare_straight(self, hand_1, hand_2):
        ranks_1 = self.rank_cards(hand_1)
        ranks_2 = self.rank_cards(hand_2)

        if (ranks_1[4] - ranks_1[0] == 4):
            val1 = ranks_1[4]
        else:
            val1 = 14


        if (ranks_2[4] - ranks_2[0] == 4):
            val2 = ranks_2[4]
        else:
            val2 = 14


        if val1 > val2:
            return 1
        elif val2 > val1:
            return 2
        else:
            return 0
        
    
    def compare_flush(self, hand_1, hand_2):
        ranks_1 = self.rank_cards(hand_1)
        ranks_2 = self.rank_cards(hand_2)

        s1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        s2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for r in ranks_1:
            if r != 1:
                s1[12-(r-2)] = 1
            else:
                s1[0] = 1
        
        for r in ranks_2:
            if r != 1:
                s2[12-(r-2)] = 1
            else:
                s2[0] = 1


        if s1 > s2:
            return 1
        elif s2 > s1:
            return 2
        else:
            return 0
        
    def compare_four_of_a_kind(self, hand_1, hand_2):
        ranks_1 = self.rank_cards(hand_1)
        ranks_2 = self.rank_cards(hand_2)

        count_1 = {}

        for r in ranks_1:
            if r in count_1:
                count_1[r] += 1
            else:
                count_1[r] = 1

        count_2 = {}

        for r in ranks_2:
            if r in count_2:
                count_2[r] += 1
            else:
                count_2[r] = 1


        four_1 = []
        four_2 = []

        one_1 = []
        one_2 = []
        
        for (key, value) in count_1.items():
            if value == 4:
                four_1.append(key)

            if value == 1:
                one_1.append(key)

        for (key, value) in count_2.items():
            if value == 4:
                four_2.append(key)
            
            if value == 1:
                one_2.append(key)

        for i in range(len(four_1)):
            if four_1[i] == 1:
                four_1[i] = 14
        
        for i in range(len(four_2)):
            if four_2[i] == 1:
                four_2[i] = 14

        for i in range(len(one_1)):
            if one_1[i] == 1:
                one_1[i] = 14
        
        for i in range(len(one_2)):
            if one_2[i] == 1:
                one_2[i] = 14

        four_1 = four_1 + one_1
        four_2 = four_2 + one_2
        
        if four_1 > four_2:
            return 1
        elif four_2 > four_1:
            return 2
        else:
            return 0
        
    def compare_full_house(self, hand_1, hand_2):
        ranks_1 = self.rank_cards(hand_1)
        ranks_2 = self.rank_cards(hand_2)

        count_1 = {}

        for r in ranks_1:
            if r in count_1:
                count_1[r] += 1
            else:
                count_1[r] = 1

        count_2 = {}

        for r in ranks_2:
            if r in count_2:
                count_2[r] += 1
            else:
                count_2[r] = 1


        three_1 = []
        three_2 = []

        two_1 = []
        two_2 = []
        
        for (key, value) in count_1.items():
            if value == 3:
                three_1.append(key)

            if value == 2:
                two_1.append(key)

        for (key, value) in count_2.items():
            if value == 3:
                three_2.append(key)
            
            if value == 2:
                two_2.append(key)

        for i in range(len(three_1)):
            if three_1[i] == 1:
                three_1[i] = 14
        
        for i in range(len(three_2)):
            if three_2[i] == 1:
                three_2[i] = 14

        for i in range(len(two_1)):
            if two_1[i] == 1:
                two_1[i] = 14
        
        for i in range(len(two_2)):
            if two_2[i] == 1:
                two_2[i] = 14

        three_1 = three_1 + two_1
        three_2 = three_2 + two_2
        
        if three_1 > three_2:
            return 1
        elif three_2 > three_1:
            return 2
        else:
            return 0
        
    
    def compare_three_of_a_kind(self, hand_1, hand_2):
        ranks_1 = self.rank_cards(hand_1)
        ranks_2 = self.rank_cards(hand_2)

        count_1 = {}

        for r in ranks_1:
            if r in count_1:
                count_1[r] += 1
            else:
                count_1[r] = 1

        count_2 = {}

        for r in ranks_2:
            if r in count_2:
                count_2[r] += 1
            else:
                count_2[r] = 1


        three_1 = []
        three_2 = []

        one_list_1 = []
        one_list_2 = []
        
        for (key, value) in count_1.items():
            if value == 3:
                three_1.append(key)

            if value == 1:
                one_list_1.append(key)

        for (key, value) in count_2.items():
            if value == 3:
                three_2.append(key)
            
            if value == 1:
                one_list_2.append(key)

        for i in range(len(three_1)):
            if three_1[i] == 1:
                three_1[i] = 14
        
        for i in range(len(three_2)):
            if three_2[i] == 1:
                three_2[i] = 14

        for i in range(len(one_list_1)):
            if one_list_1[i] == 1:
                one_list_1[i] = 14
        
        for i in range(len(one_list_2)):
            if one_list_2[i] == 1:
                one_list_2[i] = 14

        one_list_1.sort(reverse=True)
        one_list_2.sort(reverse=True)

        three_1 = three_1 + one_list_1
        three_2 = three_2 + one_list_2
        
        if three_1 > three_2:
            return 1
        elif three_2 > three_1:
            return 2
        else:
            return 0
        
    def compare_two_pair(self, hand_1, hand_2):
        ranks_1 = self.rank_cards(hand_1)
        ranks_2 = self.rank_cards(hand_2)

        count_1 = {}

        for r in ranks_1:
            if r in count_1:
                count_1[r] += 1
            else:
                count_1[r] = 1
            
        count_2 = {}

        for r in ranks_2:
            if r in count_2:
                count_2[r] += 1
            else:
                count_2[r] = 1

        twos_1 = []
        twos_2 = []

        one_1 = []
        one_2 = []

        for (key, val) in count_1.items():
            if val == 2:
                twos_1.append(key)
            
            if val == 1:
                one_1.append(key)

        for (key, val) in count_2.items():
            if val == 2:
                twos_2.append(key)
            
            if val == 1:
                one_2.append(key)

        for i in range(len(twos_1)):
            if twos_1[i] == 1:
                twos_1[i] = 14
        
        for i in range(len(twos_2)):
            if twos_2[i] == 1:
                twos_2[i] = 14

        twos_1.sort(reverse=True)
        twos_2.sort(reverse=True)

        for i in range(len(one_1)):
            if one_1[i] == 1:
                one_1[i] = 14

        for i in range(len(one_2)):
            if one_2[i] == 1:
                one_2[i] = 14

        twos_1 = twos_1 + one_1
        twos_2 = twos_2 + one_2

        if twos_1 > twos_2:
            return 1
        elif twos_2 > twos_1:
            return 2
        else:
            return 0
        
    
    def compare_pair(self, hand_1, hand_2):
        ranks_1 = self.rank_cards(hand_1)
        ranks_2 = self.rank_cards(hand_2)

        count_1 = {}

        for r in ranks_1:
            if r in count_1:
                count_1[r] += 1
            else:
                count_1[r] = 1
            
        count_2 = {}

        for r in ranks_2:
            if r in count_2:
                count_2[r] += 1
            else:
                count_2[r] = 1

        two_1 = []
        two_2 = []

        ones_1 = []
        ones_2 = []

        for (key, val) in count_1.items():
            if val == 2:
                two_1.append(key)
            
            if val == 1:
                ones_1.append(key)

        for (key, val) in count_2.items():
            if val == 2:
                two_2.append(key)
            
            if val == 1:
                ones_2.append(key)

        for i in range(len(two_1)):
            if two_1[i] == 1:
                two_1[i] = 14
        
        for i in range(len(two_2)):
            if two_2[i] == 1:
                two_2[i] = 14

        for i in range(len(ones_1)):
            if ones_1[i] == 1:
                ones_1[i] = 14
        
        for i in range(len(ones_2)):
            if ones_2[i] == 1:
                ones_2[i] = 14

        ones_1.sort(reverse=True)
        ones_2.sort(reverse=True)

        twos_1 = two_1 + ones_1
        twos_2 = two_2 + ones_2

        if twos_1 > twos_2:
            return 1
        elif twos_2 > twos_1:
            return 2
        else:
            return 0
        
    def compare_high_card(self, hand_1, hand_2):
        ranks_1 = self.rank_cards(hand_1)
        ranks_2 = self.rank_cards(hand_2)

        for i in range(len(ranks_1)):
            if ranks_1[i] == 1:
                ranks_1[i] = 14
        
        for i in range(len(ranks_2)):
            if ranks_2[i] == 1:
                ranks_2[i] = 14

        ranks_1.sort(reverse=True)
        ranks_2.sort(reverse=True)

        if ranks_1 > ranks_2:
            return 1
        elif ranks_2 > ranks_1:
            return 2
        else:
            return 0

    def compare_hands(self, hand_1, hand_2):

        rank_1 = self.get_hand_rank(hand_1)
        rank_2 = self.get_hand_rank(hand_2)

        if rank_1 < rank_2:
            return 1
        elif rank_2 < rank_1:
            return 2
        else:
            if rank_1 == 1:
                return self.compare_flush(hand_1, hand_2)
            if rank_1 == 2:
                return self.compare_four_of_a_kind(hand_1, hand_2)
            if rank_1 == 3:
                return self.compare_full_house(hand_1, hand_2)
            if rank_1 == 4:
                return self.compare_flush(hand_1, hand_2)
            if rank_1 == 5:
                return self.compare_straight(hand_1, hand_2)
            if rank_1 == 6:
                return self.compare_three_of_a_kind(hand_1, hand_2)
            if rank_1 == 7:
                return self.compare_two_pair(hand_1, hand_2)
            if rank_2 == 8:
                return self.compare_pair(hand_1, hand_2)
            
            return self.compare_high_card(hand_1, hand_2)
        
    def sort_cards(self, cards):
        spades = [card[1] for card in cards if card[0] == 'Spades']
        hearts = [card[1] for card in cards if card[0] == 'Hearts']
        clubs = [card[1] for card in cards if card[0] == 'Clubs']
        diamonds = [card[1] for card in cards if card[0] == 'Diamonds']

        aces = [card for card in cards if card[1] == 'A']
        twos = [card for card in cards if card[1] == '2']
        threes = [card for card in cards if card[1] == '3']
        fours = [card for card in cards if card[1] == '4']
        fives = [card for card in cards if card[1] == '5']
        sixes = [card for card in cards if card[1] == '6']
        sevens = [card for card in cards if card[1] == '7']
        eights = [card for card in cards if card[1] == '8']
        nines = [card for card in cards if card[1] == '9']
        tens = [card for card in cards if card[1] == '10']
        jacks = [card for card in cards if card[1] == 'J']
        queens = [card for card in cards if card[1] == 'Q']
        kings = [card for card in cards if card[1] == 'K']

        return spades, hearts, clubs, diamonds, aces, twos, threes, fours, fives, sixes, sevens, eights, nines, tens, jacks, queens, kings
    
    def get_straight_flush_helper(self, suit):
        suit_count = 0
        suit_last = -1

        straight_flushes = []
        res = []

        for i in range(len(self.ranks)):
            if self.ranks[i] in suit:
                if suit_last == -1:
                    suit_count = 1
                elif suit_last == i-1:
                    suit_count += 1
                suit_last = i
            else:
                suit_last = -1
                suit_count = 0
            
            if suit_count >= 5:
                straight_flushes.append(i+1)

        if suit_count >= 4 and 'A' in suit:
            straight_flushes.append(1)

        # for val in straight_flushes:
        #     if val != 0:
        #         top = val + 1
        #         hand = []

        #         for i in range(top - 4, top + 1):
        #             hand.append(self.number_to_rank[i])
                
        #         res.append(hand)
        #     else:
        #         res.append(['10', 'J', 'Q', 'K', 'A'])
        
        # return res

        return straight_flushes
    
    def get_straight_flushes(self, spades, hearts, clubs, diamonds):
        spade_flush = self.get_straight_flush_helper(spades)
        heart_flush = self.get_straight_flush_helper(hearts)
        club_flush = self.get_straight_flush_helper(clubs)
        diamond_flush = self.get_straight_flush_helper(diamonds)

        # for hand in spade_flush:
        #     for i in range(len(hand)):
        #         hand[i] = ('Spades', hand[i])

        # for hand in heart_flush:
        #     for i in range(len(hand)):
        #         hand[i] = ('Hearts', hand[i])

        # for hand in club_flush:
        #     for i in range(len(hand)):
        #         hand[i] = ('Clubs', hand[i])

        # for hand in diamond_flush:
        #     for i in range(len(hand)):
        #         hand[i] = ('Diamonds', hand[i])

        # return spade_flush + heart_flush + club_flush + diamond_flush

        straight_flushes = {
            val for val in spade_flush + heart_flush + club_flush + diamond_flush
        }

        straight_flushes = list(straight_flushes)

        for i in range(len(straight_flushes)):
            if straight_flushes[i] == 1:
                straight_flushes[i] = 14
        if len(straight_flushes) == 0:
            return []
        return [max(straight_flushes)]
    
    def get_four_of_a_kind(self, cards):
        res = []
        suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

        for i in range(13):
            if len(cards[i]) >= 4:
                # res.append([(self.number_to_rank[i+1], suit) for suit in suits])
                res.append(i+1)

        for i in range(len(res)):
            if res[i] == 1:
                res[i] = 14

        if len(res) == 0:
            return []
        
        return [max(res)]
    
    def get_full_house(self, cards):

        trips = []
        pairs = []

        for i in range(13):
            if len(cards[i]) >= 2:
                if i+1 != 1:
                    pairs.append(i+1)
                else:
                    pairs.append(14)
            if len(cards[i]) >= 3:
                if i+1 != 1:
                    trips.append(i+1)
                else:
                    trips.append(14)
        
        res = [(i, j) for i in trips for j in pairs if i != j]

        if len(res) == 0:
            return []

        top = max(val[0] for val in res)

        res = [val for val in res if val[0] == top]

        top = max([val[1] for val in res])

        res = [val for val in res if val[1] == top]

        return res
    
    def get_flush(self, spades, hearts, clubs, diamonds):
        spades = [self.ranking[card] for card in spades]
        hearts = [self.ranking[card] for card in hearts]
        clubs = [self.ranking[card] for card in clubs]
        diamonds = [self.ranking[card] for card in diamonds]

        for i in range(len(spades)):
            if spades[i] == 1:
                spades[i] = 14
        
        for i in range(len(hearts)):
            if hearts[i] == 1:
                hearts[i] = 14

        for i in range(len(clubs)):
            if clubs[i] == 1:
                clubs[i] = 14

        for i in range(len(diamonds)):
            if diamonds[i] == 1:
                diamonds[i] = 14


        spades.sort(reverse=True)
        hearts.sort(reverse=True)
        clubs.sort(reverse=True)
        diamonds.sort(reverse=True)

        if len(spades) >= 5:
            spades = spades[0:5]
        else:
            spades = []

        if len(hearts) >= 5:
            hearts = hearts[0:5]
        else:
            hearts = []

        if len(clubs) >= 5:
            clubs = clubs[0:5]
        else:
            clubs = []

        if len(diamonds) >= 5:
            diamonds = diamonds[0:5]
        else:
            diamonds = []

        if max(len(spades), len(clubs), len(hearts), len(diamonds)) == 5:
            return max(spades, clubs, hearts, diamonds)
        else:
            return []
    
    def get_compare_hands(self, player_cards, dealer_cards):
        n = len(dealer_cards)
        for i in range(n-4):
            for j in range(i, n-3):
                for k in range(j, n-2):
                    for l in range(k, n-1):
                        for m in range(l, n):
                            dealer_hand = [dealer_cards[i], dealer_cards[j], dealer_cards[k], dealer_cards[l], dealer_cards[m]]
                            if self.compare_hands(player_cards, dealer_hand) != 1:
                                return 0
        return 1
        
        



