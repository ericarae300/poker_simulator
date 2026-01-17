# main script to run game

from deck import Card, Deck, Player, TexasHoldem

def demo_game():
    # runs demo game with 3 players 
    print("TEXAS HOLD'EM POKER SIMULATOR")
    print()

    # Create players
    players = [
        Player("John", chips=1000),
        Player("Ella", chips=1000),
        Player("Ava", chips=1000)
    ]

    # Initialize game
    game = TexasHoldem(players)

    print("Players:")
    for p in players:
        print(f"  - {p.name}: {p.chips} chips")
    print()

    # Deal hole cards
    print("DEALING HOLE CARDS...")
    game.deal_hole_cards()
    for p in players:
        print(f"{p.name}'s hole cards: {p.hand}")
    print()

    # Deal flop
    print("THE FLOP")
    game.deal_flop()
    print(f"Community cards: {game.community_cards}")
    print()

    # Deal turn
    print("THE TURN")
    game.deal_turn()
    print(f"Community cards: {game.community_cards}")
    print()

    # Deal river
    print("THE RIVER")
    game.deal_river()
    print(f"Community cards: {game.community_cards}")
    print()

    # Showdown
    print("SHOWDOWN!!!")
    game.showdown()
    print()

def demo_hand_evaluation():
    # demos hand evaluation cababilities 
    print("HAND EVALUATION DEMO")
    print()

    from evaluator import best

    # Create sample hand
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
    demo_game()
    
    demo_hand_evaluation()
