"""
Name: Jay Genao
Date: April 06, 2026

Program Description:
This program uses a Deck object to deal a five-card poker hand.
It allows the user to choose which card positions to replace during
the draw phase, then deals new cards in those positions and displays
the final hand.
"""

from deck import Deck


def deal_hand(deck):
    """
    Deals a five-card hand from the deck.

    Parameters:
        deck (Deck): The deck object used to deal cards.

    Variables:
        hand (list): Stores the five cards dealt to the player.

    Logic:
        1. Create an empty list for the hand.
        2. Loop five times.
        3. Deal one card each time and add it to the hand.
        4. Return the completed hand.

    Return:
        list: The list of five cards in the player's hand.
    """
    hand = []

    for _ in range(5):
        hand.append(deck.deal())

    return hand


def display_hand(hand, title):
    """
    Displays the cards in the player's hand with position numbers.

    Parameters:
        hand (list): The player's current hand of cards.
        title (str): A heading to display before the hand.

    Variables:
        position (int): The numbered position of each card.
        card (Card): A single card object from the hand.

    Logic:
        1. Print the title.
        2. Loop through the hand with numbered positions.
        3. Display each card with its position number.

    Return:
        None
    """
    print(f"\n{title}")
    for position, card in enumerate(hand, start=1):
        print(f"{position}. {card}")


def replace_cards(hand, deck):
    """
    Replaces selected cards in the hand based on user input.

    Parameters:
        hand (list): The player's current hand.
        deck (Deck): The deck object used to deal replacement cards.

    Variables:
        replace_input (str): The positions entered by the user.
        positions (list): The list of positions to replace.
        position (str): A single entered position from the list.
        index (int): The zero-based index of the card to replace.

    Logic:
        1. Ask the user which card positions to replace.
        2. If the user presses Enter, keep the hand as it is.
        3. Split the entered positions by commas.
        4. Convert each position to a zero-based index.
        5. Replace the selected cards with new cards from the deck.
        6. Ignore invalid positions outside the range 1 to 5.

    Return:
        list: The updated hand after replacements.
    """
    replace_input = input(
        "\nEnter card positions to replace (example: 1,3,5) "
        "or press Enter to keep all cards: "
    ).strip()

    if replace_input == "":
        return hand

    positions = replace_input.split(",")

    for position in positions:
        index = int(position.strip()) - 1

        if 0 <= index < 5:
            hand[index] = deck.deal()

    return hand


def main():
    """
    Controls the poker hand game.

    Parameters:
        None

    Variables:
        deck (Deck): The deck of cards used in the game.
        hand (list): The player's current hand of cards.

    Logic:
        1. Create a Deck object.
        2. Shuffle the deck.
        3. Deal the initial five-card hand.
        4. Display the initial hand.
        5. Ask the user which cards to replace.
        6. Replace the selected cards.
        7. Display the final hand.

    Return:
        None
    """
    print("=== Five-Card Poker Draw ===")

    # Create and shuffle the deck
    deck = Deck()
    deck.shuffle()

    # Deal the initial hand
    hand = deal_hand(deck)

    # Display the original hand
    display_hand(hand, "Original Hand")

    # Replace selected cards
    hand = replace_cards(hand, deck)

    # Display the final hand
    display_hand(hand, "Final Hand")


if __name__ == "__main__":
    main()