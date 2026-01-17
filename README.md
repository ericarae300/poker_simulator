# Poker Simulator

This project is a Python-based Texas Hold'em poker simulator. It implements traditional a traditional Texas Hold'em poker game and evaluates player hands. I created this project to learn more about the game of poker amd its connection to probability theory.

## Features

- **Card & Deck Management**: Standard 52-card deck with shuffle and deal operations
- **Player System**: Tracks player chips, hands, and overall game state
- **Hand Evaluation**: Hand ranking from High Card to Royal Flush
- **Texas Hold'em Logic**: Incorporates hole cards, flop, turn, river, and showdown
- **Hand Comparison**: Automatically determines winner using hand strength (also takes tiebreakers into account).

## Try my simulator:

Clone the repo and install dependencies:

```bash
git clone https://github.com/yourusername/poker_simulator.git
cd poker_simulator
pip install -r requirements.txt
```

### Quick Start

- Modify this example however you would like by changing player names and number of chips.

```python
from deck import Player, TexasHoldem

# Create players
players = [
    Player("Alice", chips=1000),
    Player("Bob", chips=1000),
    Player("Charlie", chips=1000)
]

# Initialize game
game = TexasHoldem(players)

# Deal hole cards
game.deal_hole_cards()

# Play through community cards
game.deal_flop()
game.deal_turn()
game.deal_river()

# Determine winner
game.showdown()
```

### Evaluator

```python
from deck import Card
from evaluator import best, evaluate_hand

# Create cards
cards = [
    Card("Ace", "Hearts"),
    Card("King", "Hearts"),
    Card("Queen", "Diamonds"),
    Card("Jack", "Clubs"),
    Card("10", "Spades"),
    Card("9", "Hearts"),
    Card("8", "Diamonds")
]

# Find best 5 card hand
rank, best_hand = best(cards)
print(f"Best hand rank: {rank[0]}")
print(f"Best hand: {best_hand}")
```

## Folder Structure

```
poker_simulator/
├── deck.py           # Card, Deck, Player, and TexasHoldem classes
├── evaluator.py      # Hand evaluation and ranking logic
├── poker.ipynb       # Jupyter notebook with examples
├── requirements.txt  # Python dependencies
├── .gitignore
└── README.md
```

## Hand Rankings

1. Royal Flush: Ace, King, Queen, Jack, ten (all of the same suit)
2. Straight Flush: Five consecutive cards (all of the same suit)
3. Four of a Kind: Four cards of the same rank (suits can differ)
4. Full House: Three of a kind plus a pair (suits can differ)
5. Flush: Five cards of the same suit (rank can differ)
6. Straight: Five consecutive cards by rank (suit can differ)
7. Three of a Kind: Three cards of the same rank (suit can differ)
8. Two Pair: Two different pairs (suits can differ, highest two pair at showdown wins).
9. One Pair: Two cards of the same rank (suits can differ, 3 other side cards, highest one pair at showdown wins).
10. High Card: No combinations, lowest ranking hand, the highest card in the hand determines the hand strength.

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## License

MIT License - see LICENSE file for details
