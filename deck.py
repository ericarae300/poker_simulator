
import random
from typing import List, Tuple
from evaluator import best, suits, ranks

class Card:
# Represents a single playing card (rank and suit)

    def __init__(self, rank: str, suit: str) -> None:
        # Initializes card with rank and suit. 
        #   rank: 2-10, Jack, Queen, King, Ace
        #   suit: Hearts, Diamonds, Clubs, Spades

        self.rank = rank
        self.suit = suit
        self.value = ranks.index(rank)  
        
    def __repr__(self) -> str:
        # returns string representation of the card
        return f"{self.rank} of {self.suit}"

class Deck:
# shuffles and deals a standard 52 card deck. 
    
    def __init__(self) -> None:
        # initialize 52 card deck
        self.cards: List[Card] = [Card(r, s) for s in suits for r in ranks]
        
    def shuffle(self) -> None:
        random.shuffle(self.cards)
    
    def deal(self, num: int = 1) -> List[Card]:
        # Deals and removes cards from main deck. Returns list of dealt cards.
        # num: number of cards to deal (default = 1)
        if num <= len(self.cards):
            return [self.cards.pop() for _ in range(num)] 
        else:
            raise ValueError("Not enough cards in the deck to deal.")
    
class Player:
# represents a player   

    def __init__(self, name: str, chips: int = 1000) -> None:
    # initialize player names and number of chips (default = 1000)
        self.name = name
        self.chips = chips
        self.hand: List[Card] = []
        self.folded = False
        
    def bet(self, amount: int) -> int:
    # remove chips from player's stack as their bet (amount). Returns bet value
    
        if amount > self.chips:
            raise ValueError(f"{self.name} has {self.chips} chips but tried to bet {amount}.")
        self.chips -= amount
        return amount
    
    def __repr__(self) -> str:
        return f"Player {self.name}, Chips: {self.chips}, Hand: {self.hand}, Folded: {self.folded}"

    
class TexasHoldem:
# class to manage game  

    def __init__(self, players: List[Player]) -> None:
    # initialize game and list of players
        self.deck = Deck()
        self.deck.shuffle()
        self.players = players
        self.community_cards: List[Card] = []
        self.pot = 0
        
    def deal_hole_cards(self) -> None:
    # deal two starting cards to each player
        self.deck.shuffle()
        for player in self.players:
            player.hand = self.deck.deal(2)
    
    def deal_flop(self) -> None:
        # discard one card and deal 3 community cards
        self.deck.deal(1)  
        self.community_cards += self.deck.deal(3)
        
    def deal_turn(self) -> None:
        # discard one card and deal one community card, round begins
        self.deck.deal(1)  
        self.community_cards += self.deck.deal(1)
        
    def deal_river(self) -> None:
        # discard one card and deal one community card
        self.deck.deal(1)  
        self.community_cards += self.deck.deal(1)
    
    def showdown(self) -> Player:
        # evaluate all remaining players' hands and determine winner
        # returns winning player object. 
        print("Showdown! Reveal your hands!")
        results = []
        # iterate through players. If player hasn't folded determine each players best hand & rank
        for p in self.players:
            if not p.folded:
                rank, hand = best(p.hand + self.community_cards)
                results.append((p, rank, hand))        
                print(f"{p.name}'s Best Hand: {hand}, Best Hand Rank: {rank}")
        
        if not results:
            print("No players remaining!")
            return None
            
        winner = max(results, key=lambda x: x[1])
        print(f"\nThe winner is {winner[0].name} with hand rank {winner[1]}!")
        return winner[0]               
    
    def reset_round(self) -> None:
        # reset game state for new round
        self.community_cards = []
        self.pot = 0
        for player in self.players:
            player.hand = []
            player.folded = False
        self.deck = Deck()
        self.deck.shuffle()