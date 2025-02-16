from deck import Deck
from poker_ranker import PokerRanker
from renjie_poker import RenjiePoker

def test_deck_length():
    test_deck = Deck()
    try:
        assert len(test_deck.deck) == 52
        print("test_deck_length passed")
    except:
        print("test deck_length failed")

    

def test_shuffle():
    test_deck = Deck()

    for card in test_deck.deck:
        print(card)

def test_straight_ordering():
    test_checker = PokerRanker()
    hand_1 = [('Spades', 'A'), ('Hearts', '2'), ('Spades', '3'), ('Clubs', '5'), ('Diamonds', '4')]
    hand_2 = [('Spades', 'A'), ('Spades', '2'), ('Spades', '3'), ('Spades', '5'), ('Spades', '4')]
    hand_3 = [('Spades', 'A'), ('Hearts', '2'), ('Spades', '3'), ('Clubs', '5'), ('Diamonds', '7')]
    hand_4 = [('Spades', 'A'), ('Hearts', 'Q'), ('Spades', 'J'), ('Clubs', 'K'), ('Diamonds', '10')]
    
    rank_1 = test_checker.rank_cards(hand_1)
    rank_2 = test_checker.rank_cards(hand_2)
    rank_3 = test_checker.rank_cards(hand_3)
    rank_4 = test_checker.rank_cards(hand_4)

    try:
        assert rank_1 == [1,2,3,4,5]
        print("hand_1 passed rank")
    except:
        print("hand_1 failed")
        print(f"rank_1: {rank_1}")

    try:
        assert rank_2 == [1,2,3,4,5]
        print("hand_2 passed rank")
    except:
        print("hand_1 failed")
        print(f"rank_2: {rank_2}")

    try:
        assert rank_3 == [1,2,3,5,7]
        print("hand_3 passed rank")
    except:
        print("hand_3 failed")
        print(f"rank_3: {rank_3}")

    try:
        assert rank_4 == [1,10,11,12,13]
        print("hand_4 passed rank")
    except:
        print("hand_4 failed")
        print(f"rank_4: {rank_4}")

def test_straight():
    test_checker = PokerRanker()

    hand_1 = [('Spades', 'A'), ('Hearts', '2'), ('Spades', '3'), ('Clubs', '5'), ('Diamonds', '4')]
    hand_2 = [('Spades', 'A'), ('Spades', '2'), ('Spades', '3'), ('Spades', '5'), ('Spades', '4')]
    hand_3 = [('Spades', 'A'), ('Hearts', '2'), ('Spades', '3'), ('Clubs', '5'), ('Diamonds', '7')]
    hand_4 = [('Spades', 'A'), ('Hearts', 'Q'), ('Spades', 'J'), ('Clubs', 'K'), ('Diamonds', '10')]

    try:
        assert test_checker.check_straight(hand_1) == True
        print("hand 1 is a straight")
    except:
        print("hand 1 is not a straight")
    try:
        assert test_checker.check_straight(hand_2) == True
        print("hand 2 is a straight")
    except:
        print("hand 2 is not a straight")
    try:
        assert test_checker.check_straight(hand_3) != True
        print("hand 3 is not a straight")
    except:
        print("hand 3 is a straight")
    try:
        assert test_checker.check_straight(hand_4) == True
        print("hand 4 is a straight")
    except:
        print("hand 4 is not a straight")

def test_flush():
    test_checker = PokerRanker()

    hand_1 = [('Spades', 'A'), ('Hearts', '2'), ('Spades', '3'), ('Clubs', '5'), ('Diamonds', '4')]
    hand_2 = [('Spades', 'A'), ('Spades', '2'), ('Spades', '3'), ('Spades', '5'), ('Spades', '4')]
    hand_3 = [('Spades', 'A'), ('Hearts', '2'), ('Spades', '3'), ('Clubs', '5'), ('Diamonds', '7')]
    hand_4 = [('Spades', 'A'), ('Hearts', 'Q'), ('Spades', 'J'), ('Clubs', 'K'), ('Diamonds', '10')]

    try:
        assert test_checker.check_flush(hand_1) == False
        print("hand_1 is not a flush")
    except:
        print("hand_1 is a flush")

    try:
        assert test_checker.check_flush(hand_2) == True
        print("hand_2 is a flush")
    except:
        print("hand_2 is not a flush")

    try:
        assert test_checker.check_flush(hand_3) == False
        print("hand_3 is not a flush")
    except:
        print("hand_3 is a flush")

    try:
        assert test_checker.check_flush(hand_4) == False
        print("hand_4 is not a flush")
    except:
        print("hand_4 is a flush")

def test_four_of_a_kind():
    test_checker = PokerRanker()

    hand_1 = [('Spades', 'A'), ('Hearts', '2'), ('Spades', '3'), ('Clubs', '5'), ('Diamonds', '4')]
    hand_2 = [('Spades', 'A'), ('Spades', '2'), ('Spades', '3'), ('Spades', '5'), ('Spades', '4')]
    hand_3 = [('Spades', 'A'), ('Hearts', '2'), ('Spades', '3'), ('Clubs', '5'), ('Diamonds', '7')]
    hand_4 = [('Spades', 'A'), ('Hearts', 'Q'), ('Spades', 'J'), ('Clubs', 'K'), ('Diamonds', '10')]
    hand_5 = [('Spades', 'A'), ('Hearts', 'A'), ('Diamonds', 'A'), ('Clubs', 'A'), ('Diamonds', '10')]

    try:
        assert test_checker.check_four_of_a_kind(hand_1) == False
        print("hand 1 is not four of a kind")
    except:
        print("hand 1 is four of a kind")

    try:
        assert test_checker.check_four_of_a_kind(hand_2) == False
        print("hand 2 is not four of a kind")
    except:
        print("hand 2 is four of a kind")

    try:
        assert test_checker.check_four_of_a_kind(hand_3) == False
        print("hand 3 is not four of a kind")
    except:
        print("hand 3 is four of a kind")

    try:
        assert test_checker.check_four_of_a_kind(hand_4) == False
        print("hand 4 is not four of a kind")
    except:
        print("hand 4 is four of a kind")

    try:
        assert test_checker.check_four_of_a_kind(hand_5)
        print("hand 5 is four of a kind")
    except:
        print("hand 5 is notfour of a kind")

def test_full_house(test_checker, hands, expected):
    for pair in zip(hands, expected):
        print(pair[0])
        try:
            assert test_checker.check_full_house(pair[0]) == pair[1]

        except:
            print("full house test failed")
            return
    
    print("full house test passed")

def test_three_of_a_kind(test_checker, hands, expected):
    for pair in zip(hands, expected):
        print(pair[0])
        try:
            assert test_checker.check_three_of_a_kind(pair[0]) == pair[1]

        except:
            print("three of a kind test failed")
            return
    
    print("three of a kind test passed")

def test_pair(test_checker, hands, expected):
    for pair in zip(hands, expected):
        print(pair[0])
        try:
            assert test_checker.check_pair(pair[0]) == pair[1]

        except:
            print("pair test failed")
            return
    
    print("pair test passed")

def test_two_pair(test_checker, hands, expected):
    for pair in zip(hands, expected):
        print(pair[0])
        try:
            assert test_checker.check_two_pair(pair[0]) == pair[1]

        except:
            print("two pair test failed")
            return
    
    print("two pair test passed")

def test_ranker(test_checker, hands, expected):
    for pair in zip(hands, expected):
        print(pair[0])
        try:
            assert test_checker.get_hand_rank(pair[0]) == pair[1]

        except:
            print("hand rank test failed")
            return
    
    print("hand rank test passed")

def test_straight_comp(test_checker, hands, expected):
    for pair in zip(hands, expected):
        print(pair[0])
        try:
            assert test_checker.compare_straight(pair[0][0], pair[0][1]) == pair[1]

        except:
            print("straight comp test failed")
            return
    
    print("straight_comp test passed")

def test_flush_comp(test_checker, hands, expected):
    for pair in zip(hands, expected):
        print(pair[0])
        try:
            assert test_checker.compare_flush(pair[0][0], pair[0][1]) == pair[1]

        except:
            print("flush comp test failed")
            return
    
    print("flush_comp test passed")

def test_four_of_a_kind_comp(test_checker, hands, expected):
    for pair in zip(hands, expected):
        print(pair[0])
        try:
            assert test_checker.compare_four_of_a_kind(pair[0][0], pair[0][1]) == pair[1]

        except:
            print("four_of_a_kind comp test failed")
            return
    
    print("four of a kind test passed")

def test_full_house_comp(test_checker, hands, expected):
    for pair in zip(hands, expected):
        print(pair[0])
        try:
            assert test_checker.compare_full_house(pair[0][0], pair[0][1]) == pair[1]

        except:
            print("full house comp test failed")
            return
    
    print("full house comp test passed")

def test_three_comp(test_checker, hands, expected):
    for pair in zip(hands, expected):
        print(pair[0])
        try:
            assert test_checker.compare_three_of_a_kind(pair[0][0], pair[0][1]) == pair[1]

        except:
            print("threes comp test failed")
            return
    
    print("threes  comp test passed")

def test_twos_comp(test_checker, hands, expected):
    for pair in zip(hands, expected):
        print(pair[0])
        try:
            assert test_checker.compare_two_pair(pair[0][0], pair[0][1]) == pair[1]

        except:
            print("twos comp test failed")
            return
    
    print("twos  comp test passed")

def test_pair_comp(test_checker, hands, expected):
    for pair in zip(hands, expected):
        print(pair[0])
        try:
            assert test_checker.compare_pair(pair[0][0], pair[0][1]) == pair[1]

        except:
            print("pair comp test failed")
            return
    
    print("pair comp test passed")

def test_high_comp(test_checker, hands, expected):
    for pair in zip(hands, expected):
        print(pair[0])
        try:
            assert test_checker.compare_high_card(pair[0][0], pair[0][1]) == pair[1]

        except:
            print("high card comp test failed")
            return
    
    print("high comp test passed")

def test_hand_comp(test_checker, hands, expected):
    for pair in zip(hands, expected):
        print(pair[0])
        try:
            assert test_checker.compare_hands(pair[0][0], pair[0][1]) == pair[1]

        except:
            print("hand comp test failed")
            return
    
    print("hand comp test passed")

def test_get_straight_flush_main(test_checker, cards):
    print(test_checker.get_straight_flushes(cards[0], cards[1], cards[2], cards[3]))


def test_fours(test_checker, cards):
    print(test_checker.get_four_of_a_kind(cards))

def test_get_full_house(test_checker, cards):
    print(test_checker.get_full_house(cards))

def test_get_flush(test_checker, cards):
    print(test_checker.get_flush(cards[0], cards[1], cards[2], cards[3]))

def test_poker_ranker():

    test_checker = PokerRanker()

    hands = [
        [('Spades', 'A'), ('Hearts', '2'), ('Spades', '3'), ('Clubs', '5'), ('Diamonds', '4')],
        [('Spades', 'A'), ('Spades', '2'), ('Spades', '3'), ('Spades', '5'), ('Spades', '4')],
        [('Spades', 'A'), ('Hearts', '2'), ('Spades', '3'), ('Clubs', '5'), ('Diamonds', '7')],
        [('Spades', 'A'), ('Hearts', 'Q'), ('Spades', 'J'), ('Clubs', 'K'), ('Diamonds', '10')],
        [('Spades', 'A'), ('Hearts', 'A'), ('Diamonds', 'A'), ('Clubs', 'A'), ('Diamonds', '10')],
        [('Spades', 'A'), ('Hearts', 'A'), ('Diamonds', 'A'), ('Clubs', '10'), ('Diamonds', '10')],
        [('Spades', 'A'), ('Hearts', 'A'), ('Diamonds', 'A'), ('Clubs', '10'), ('Diamonds', '9')],
        [('Spades', 'A'), ('Hearts', 'A'), ('Diamonds', 'K'), ('Clubs', '10'), ('Diamonds', '9')],
        [('Spades', 'A'), ('Hearts', 'A'), ('Diamonds', 'K'), ('Clubs', 'K'), ('Diamonds', '9')]
    ]

    straights = [
        [('Spades', 'A'), ('Hearts', '2'), ('Spades', '3'), ('Clubs', '5'), ('Diamonds', '4')],
        [('Spades', 'A'), ('Spades', '2'), ('Spades', '3'), ('Spades', '5'), ('Spades', '4')],
        [('Spades', 'A'), ('Hearts', 'Q'), ('Spades', 'J'), ('Clubs', 'K'), ('Diamonds', '10')],
        [('Spades', '3'), ('Hearts', '4'), ('Spades', '5'), ('Clubs', '6'), ('Diamonds', '7')]
    ]

    fours = [
        [('Spades', 'A'), ('Hearts', 'A'), ('Spades', 'A'), ('Clubs', 'A'), ('Diamonds', '2')],
        [('Spades', 'A'), ('Spades', 'A'), ('Spades', 'A'), ('Spades', 'A'), ('Spades', '2')],
        [('Spades', 'A'), ('Hearts', 'A'), ('Spades', 'A'), ('Clubs', 'A'), ('Diamonds', '3')],
        [('Spades', 'K'), ('Hearts', 'K'), ('Spades', 'K'), ('Clubs', 'K'), ('Diamonds', '7')],
        [('Spades', 'Q'), ('Hearts', 'Q'), ('Spades', 'Q'), ('Clubs', 'Q'), ('Diamonds', 'Q')]
    ]

    full_houses = [
        [('Spades', 'A'), ('Hearts', 'A'), ('Spades', 'A'), ('Clubs', '2'), ('Diamonds', '2')],
        [('Spades', 'A'), ('Spades', 'A'), ('Spades', 'A'), ('Spades', '2'), ('Spades', '2')],
        [('Spades', 'A'), ('Hearts', 'A'), ('Spades', 'A'), ('Clubs', '3'), ('Diamonds', '3')],
        [('Spades', 'K'), ('Hearts', 'K'), ('Spades', 'K'), ('Clubs', '7'), ('Diamonds', '7')],
        [('Spades', 'Q'), ('Hearts', 'Q'), ('Spades', 'Q'), ('Clubs', 'K'), ('Diamonds', 'K')]
    ]

    threes = [
        [('Spades', 'A'), ('Hearts', 'A'), ('Spades', 'A'), ('Clubs', '3'), ('Diamonds', '2')],
        [('Spades', 'A'), ('Spades', 'A'), ('Spades', 'A'), ('Spades', '2'), ('Spades', '3')],
        [('Spades', 'A'), ('Hearts', 'A'), ('Spades', 'A'), ('Clubs', '4'), ('Diamonds', '3')],
        [('Spades', 'K'), ('Hearts', 'K'), ('Spades', 'K'), ('Clubs', '8'), ('Diamonds', '7')],
        [('Spades', 'Q'), ('Hearts', 'Q'), ('Spades', 'Q'), ('Clubs', 'J'), ('Diamonds', 'K')]
    ]

    twos = [
        [('Spades', 'A'), ('Hearts', 'A'), ('Spades', '3'), ('Clubs', '3'), ('Diamonds', '2')],
        [('Spades', 'A'), ('Spades', 'A'), ('Spades', '3'), ('Spades', '4'), ('Spades', '3')],
        [('Spades', 'A'), ('Hearts', 'A'), ('Spades', '4'), ('Clubs', '4'), ('Diamonds', '3')],
        [('Spades', 'K'), ('Hearts', 'K'), ('Spades', '8'), ('Clubs', '8'), ('Diamonds', '7')],
        [('Spades', 'Q'), ('Hearts', 'Q'), ('Spades', 'J'), ('Clubs', 'J'), ('Diamonds', 'K')]
    ]

    pairs = [
        [('Spades', 'A'), ('Hearts', 'A'), ('Spades', '3'), ('Clubs', '4'), ('Diamonds', '2')],
        [('Spades', 'A'), ('Spades', 'A'), ('Spades', '3'), ('Spades', '5'), ('Spades', '4')],
        [('Spades', 'A'), ('Hearts', 'A'), ('Spades', '4'), ('Clubs', '2'), ('Diamonds', '3')],
        [('Spades', 'K'), ('Hearts', 'K'), ('Spades', '8'), ('Clubs', '6'), ('Diamonds', '7')],
        [('Spades', 'Q'), ('Hearts', 'Q'), ('Spades', 'J'), ('Clubs', '10'), ('Diamonds', 'K')]
    ]

    highs = [
        [('Spades', 'A'), ('Hearts', 'K'), ('Spades', '3'), ('Clubs', '4'), ('Diamonds', '2')],
        [('Spades', 'A'), ('Spades', 'K'), ('Spades', '3'), ('Spades', '2'), ('Spades', '4')],
        [('Spades', 'A'), ('Hearts', 'K'), ('Spades', '4'), ('Clubs', '2'), ('Diamonds', '6')],
        [('Spades', 'K'), ('Hearts', 'J'), ('Spades', '8'), ('Clubs', '6'), ('Diamonds', '7')],
        [('Spades', 'Q'), ('Hearts', '2'), ('Spades', 'J'), ('Clubs', '10'), ('Diamonds', 'K')]
    ]

    straight_comps = [[straights[0], straights[1]], [straights[0], straights[2]], [straights[0], straights[3]]]

    four_comps = [[fours[0], fours[1]], [fours[0], fours[2]], [fours[0], fours[3]], [fours[3], fours[4]]]

    full_house_comps = [[full_houses[0], full_houses[1]], [full_houses[0], full_houses[2]], [full_houses[0], full_houses[3]], [full_houses[3], full_houses[4]]]

    three_comps = [[threes[0], threes[1]], [threes[0], threes[2]], [threes[0], threes[3]], [threes[3], threes[4]]]

    twos_comps = [[twos[0], twos[1]], [twos[0], twos[2]], [twos[0], twos[3]], [twos[3], twos[4]]]

    pair_comps = [[pairs[0], pairs[1]], [pairs[0], pairs[2]], [pairs[0], pairs[3]], [pairs[3], pairs[4]]]

    high_comps = [[highs[0], highs[1]], [highs[0], highs[2]], [highs[0], highs[3]], [highs[3], highs[4]]]

    full_house_expected = [0, 0, 0, 0 ,0, 1, 0, 0, 0]
    three_of_a_kind_expected = [0, 0, 0, 0 ,0, 0, 1, 0, 0]
    pair_expected = [0, 0, 0, 0 ,0, 0, 0, 1, 0]
    two_pair_expected = [0, 0, 0, 0 ,0, 0, 0, 0, 1]
    rank_expected = [5, 1, 9, 5, 2, 3, 6, 8, 7]
    straight_comps_expected = [0, 2, 2]
    flush_comps_expected = [0, 2, 1]
    four_comps_expected = [0, 2, 1, 1]
    full_house_comps_expected = [0, 2, 1, 1]
    three_comps_expected = [0, 2, 1, 1]
    twos_comps_expected = [2, 2, 1, 1]
    pair_comps_expected = [2, 0, 1, 1]
    high_comps_expected = [2, 2, 1, 2]
    

    # test_straight_ordering()
    # test_straight()
    # test_flush()
    # test_four_of_a_kind()

    # test_full_house(test_checker, hands, full_house_expected)
    # test_three_of_a_kind(test_checker, hands, three_of_a_kind_expected)
    # test_pair(test_checker, hands, pair_expected)
    # test_two_pair(test_checker, hands, two_pair_expected)
    # test_ranker(test_checker, hands, rank_expected)
    # test_straight_comp(test_checker, straight_comps, straight_comps_expected)
    # test_flush_comp(test_checker, straight_comps, flush_comps_expected)
    # test_four_of_a_kind_comp(test_checker, four_comps, four_comps_expected)
    # test_full_house_comp(test_checker, full_house_comps, full_house_comps_expected)
    # test_three_comp(test_checker, three_comps, three_comps_expected)
    # test_twos_comp(test_checker, twos_comps, twos_comps_expected)
    # test_pair_comp(test_checker, pair_comps, pair_comps_expected)
    # test_high_comp(test_checker, high_comps, high_comps_expected)
    test_hand_comp(test_checker, pair_comps, pair_comps_expected)

    test_get_straight_flush(test_checker, ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
    spades = ['A', 'K', 'Q', 'J', '10', '2', '3', '4', '5']
    print("test straight flush main")
    test_get_straight_flush_main(test_checker,[spades, [], [], spades])

    cards = [['Spades', 'Hearts', 'Diamonds', 'Clubs'], ['a', 'b', 'c'], ['a', 'b']] + [[]]*10

    print("test fours")

    test_fours(test_checker, cards)

    test_get_full_house(test_checker, cards)

    flush_cards = [['A', 'K', 'Q', 'J', '9'], ['A', 'K', 'Q', '10', '9'], ['A', 'Q', 'J', '9', '10'], ['A', 'K', 'J', '10', '9']]

    test_get_flush(test_checker, flush_cards)

    # print(test_checker.compare_two_pair(twos[0], twos[3]))

    # print(test_checker.check_full_house(hands[5]) == full_house_expected[5])


def test_get_card(deck, cards):
    card, dealer_cards, idx = deck.next_card_in_set(50, cards)

    print(f"card: {card}")
    print("dealer cards:")
    print(dealer_cards)
    print(f"idx: {idx}")

def test_get_straight_flush(test_checker, cards):
    flushes = test_checker.get_straight_flush_helper(cards)
    print(flushes)

def test_deck():
    test_deck_length()
    test_shuffle()
    test_deck = Deck()
    for card in test_deck.deck:
        print(card)
    test_get_card(test_deck, [('Spades', 'A'), ('Hearts', 'A'), ('Diamonds', 'A'), ('Clubs', 'A')])

def test_input(renjie):
    print(renjie.get_move())

def test_renjie():
    test_renjie = RenjiePoker()
    test_renjie.simple_simulation_setup(1)
    move = test_renjie.get_move()
    cards = [0]*52

    for m in move:
        cards[test_renjie.card_to_id[m]] = 1

    print(test_renjie.simulation_move(cards))
    # test_renjie.play_game()

    # test_input(test_renjie)

def main():
    # test_deck()
    # test_poker_ranker()
    test_renjie()

main()