from collections import Counter
from itertools import combinations
from typing import List, Tuple, Dict

# Define suits and ranks of a standard deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Define hand rankings
hand_rankings: Dict[str, int] = {
    "High Card": 1, 
    "One Pair": 2,
    "Two Pair": 3,
    "Three of a Kind": 4,
    "Straight": 5,
    "Flush": 6,
    "Full House": 7,
    "Four of a Kind": 8,
    "Straight Flush": 9,
    "Royal Flush": 10
}


def is_flush(cards: List) -> bool:
    # checks if a hand is a flush, returns True if all cards are the same suit
    # cards is a list of card objects
    hand_suits = [card.suit for card in cards]
    return len(set(hand_suits)) == 1


def is_straight(values: List[int]) -> bool:
    # checks if hand is a straight. values is a list of card rank values (0-12)
    # returns true if hand contains a straight
    values = sorted(set(values))
    if len(values) < 5:
        return False
    for i in range(len(values) - 4):
        if values[i + 4] - values[i] == 4:
            return True
    if set([12, 0, 1, 2, 3]).issubset(set(values)):
        return True
    return False

def evaluate_hand(cards: List) -> Tuple[Tuple[int, Tuple], str]:
    # evaluates a five card poker hand, cards is a list of exactly 5 card objects
    # returns tuple (hand_ranking_tuple, hand_name), where hand_ranking_tuple is (ranking_value, tiebreaker_values)
    rank_values = [ranks.index(card.rank) for card in cards]
    rank_counts = Counter(rank_values)  # count occurrences of each rank
    most_common = rank_counts.most_common()  # list of (rank, count) tuples sorted by frequency
    flush = is_flush(cards)
    straight = is_straight(rank_values)
    
    # Return (hand ranking, tuple of tiebreaker values in descending order of importance)
    if flush and straight:
        high_card = max(rank_values)
        if high_card == ranks.index('Ace'):
            return (hand_rankings["Royal Flush"], (high_card,))
        return (hand_rankings["Straight Flush"], (high_card,))
    elif most_common[0][1] == 4:
        extra = [v for v, c in most_common if c != 4][0]
        return (hand_rankings['Four of a Kind'], (most_common[0][0], extra))  # quad value, extra card
    elif most_common[0][1] == 3 and most_common[1][1] == 2:
        return (hand_rankings['Full House'], (most_common[0][0], most_common[1][0]))  # three, pair
    elif flush:
        return (hand_rankings["Flush"], tuple(sorted(rank_values, reverse=True)))
    elif straight:
        return (hand_rankings['Straight'], (max(rank_values),))
    elif most_common[0][1] == 3:
        extras = tuple(sorted([v for v, c in most_common if c != 3], reverse=True))
        return (hand_rankings['Three of a Kind'], (most_common[0][0],) + extras)  # set, extras
    elif most_common[0][1] == 2 and most_common[1][1] == 2:
        pairs = sorted([most_common[0][0], most_common[1][0]], reverse=True)
        extra = [v for v, c in most_common if c == 1][0]
        return (hand_rankings['Two Pair'], (pairs[0], pairs[1], extra))  # high pair, low pair, extra
    elif most_common[0][1] == 2:
        extras = tuple(sorted([v for v, c in most_common if c != 2], reverse=True))
        return (hand_rankings['One Pair'], (most_common[0][0],) + extras)  # pair, extras
    else:
        # High card - all cards in descending order
        return (hand_rankings['High Card'], tuple(sorted(rank_values, reverse=True)))



def best(seven_cards: List) -> Tuple[Tuple[int, Tuple], Tuple]:
    # finds the best 5 card hand from a 7 card combo (hole cards + community cards)
    # returns tuple (best_rank_tuple, best_hand), best_rank_tuple is (ranking_value, tiebreaker_values)
    # best_hand is a tuple of the best 5 card objects

    best_rank = (-1, ())  # hand ranking, tiebreak cards
    best_hand = None

    # Calculate all combinations of 5 cards from the 7
    total_combinations = combinations(seven_cards, 5)

    # Iterate through each combination and evaluate its rank
    for combo in total_combinations:
        rank = evaluate_hand(combo)
        # If current rank is better than the best found, update best rank and hand
        if rank > best_rank:
            best_rank = rank
            best_hand = combo
    return best_rank, best_hand