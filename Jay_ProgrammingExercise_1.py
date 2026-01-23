"""
Name: JAY GENAO
Date: January 21, 2026
Program Description: This program pre-sells a limited number of cinema tickets.
Each buyer may purchase up to 4 tickets and no more than 20 tickets can be sold
total. The program prompts the user for ticket amounts, displays the remaining
tickets after each purchase, repeats until sold out, and then displays the total
number of buyers.
"""


def get_ticket_request(remaining_tickets):
    """
    Prompts the user for the number of tickets they want and validates the request.

    Parameters:
        remaining_tickets (int): The number of tickets still available.

    Variables:
        tickets_requested (int): The number of tickets the buyer requests.

    Logic:
        1. Ask the user how many tickets they want (1 to 4).
        2. If the request is not between 1 and 4, display an error and return 0.
        3. If the request is more than remaining_tickets, display an error and return 0.
        4. Return the valid number of tickets requested.

    Return:
        int: The valid ticket request amount (0 if invalid).
    """
    # Ask the buyer for the ticket quantity
    tickets_requested = int(input("How many tickets would you like to buy (1-4)? "))

    # Validate the buyer is purchasing between 1 and 4 tickets
    if tickets_requested < 1 or tickets_requested > 4:
        print("Invalid entry. You can only buy 1 to 4 tickets.")
        return 0

    # Validate the buyer is not purchasing more than what is left
    if tickets_requested > remaining_tickets:
        print("Not enough tickets remaining for that purchase.")
        return 0

    # Return valid request
    return tickets_requested


def sell_tickets():
    """
    Sells tickets until all tickets are sold and tracks the number of buyers.

    Parameters:
        None

    Variables:
        remaining_tickets (int): Tickets available to sell (starts at 20).
        buyer_count (int): Accumulator counting successful buyers.
        tickets_sold (int): Tickets sold to the current buyer.

    Logic:
        1. Set remaining_tickets to 20 and buyer_count to 0.
        2. Loop while remaining_tickets is greater than 0.
        3. Prompt the buyer for tickets using get_ticket_request.
        4. If valid, subtract tickets_sold from remaining_tickets.
        5. If valid, add 1 to buyer_count.
        6. Display remaining tickets after each successful purchase.
        7. When sold out, display total buyers.

    Return:
        int: The total number of buyers.
    """
    # Initialize tickets and buyer counter
    remaining_tickets = 20
    buyer_count = 0

    # Continue until tickets are sold out
    while remaining_tickets > 0:
        # Display how many tickets remain
        print(f"\nTickets remaining: {remaining_tickets}")

        # Get a validated request from the buyer
        tickets_sold = get_ticket_request(remaining_tickets)

        # Only complete a purchase if the request is valid
        if tickets_sold > 0:
            # Update remaining tickets and buyer count
            remaining_tickets -= tickets_sold
            buyer_count += 1

            # Display purchase success and updated remaining tickets
            print(f"Purchase successful. Tickets remaining: {remaining_tickets}")

    # Display final results
    print("\nAll tickets have been sold.")
    print(f"Total number of buyers: {buyer_count}")

    return buyer_count


def main():
    """
    Program entry point that starts the ticket pre-sale process.

    Parameters:
        None

    Variables:
        None

    Logic:
        1. Call sell_tickets to run the ticket sales loop.

    Return:
        None
    """
    # Start ticket sales
    sell_tickets()


if __name__ == "__main__":
    main()
