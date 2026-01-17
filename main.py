"""
Main poker simulator game runner.

This module demonstrates a complete Texas Hold'em game with multiple players.
"""

from deck import Card, Deck, Player, TexasHoldem


def demo_game():
    """Run a demonstration Texas Hold'em game with 3 players."""
    print("=" * 60)
    print("TEXAS HOLD'EM POKER SIMULATOR")
    print("=" * 60)
    print()

    # Create players
    players = [
        Player("Alice", chips=1000),
        Player("Bob", chips=1000),
        Player("Charlie", chips=1000)
    ]

    # Initialize game
    game = TexasHoldem(players)

    print("Players:")
    for p in players:
        print(f"  - {p.name}: {p.chips} chips")
    print()

    # Deal hole cards
    print("-" * 60)
    print("DEALING HOLE CARDS...")
    print("-" * 60)
    game.deal_hole_cards()
    for p in players:
        print(f"{p.name}'s hole cards: {p.hand}")
    print()

    # Deal flop
    print("-" * 60)
    print("THE FLOP")
    print("-" * 60)
    game.deal_flop()
    print(f"Community cards: {game.community_cards}")
    print()

    # Deal turn
    print("-" * 60)
    print("THE TURN")
    print("-" * 60)
    game.deal_turn()
    print(f"Community cards: {game.community_cards}")
    print()

    # Deal river
    print("-" * 60)
    print("THE RIVER")
    print("-" * 60)
    game.deal_river()
    print(f"Community cards: {game.community_cards}")
    print()

    # Showdown
    print("=" * 60)
    game.showdown()
    print("=" * 60)


def demo_hand_evaluation():
    """Demonstrate hand evaluation capabilities."""
    print("\n" + "=" * 60)
    print("HAND EVALUATION DEMO")
    print("=" * 60)
    print()

    from evaluator import best

    # Create a sample hand
    cards = [
        Card("Ace", "Hearts"),
        Card("King", "Hearts"),
        Card("Queen", "Diamonds"),
        Card("Jack", "Clubs"),
        Card("10", "Spades"),
        Card("9", "Hearts"),
        Card("8", "Diamonds")
    ]

    print("7 Cards:")
    for i, card in enumerate(cards, 1):
        print(f"  {i}. {card}")
    print()

    rank, best_hand = best(cards)
    print(f"Best 5-card hand:")
    for card in best_hand:
        print(f"  - {card}")
    print()
    print(f"Hand ranking value: {rank[0]}")
    print(f"Tiebreaker values: {rank[1]}")
    print()


if __name__ == "__main__":
    # Run demo game
    demo_game()

    # Run hand evaluation demo
    demo_hand_evaluation()
