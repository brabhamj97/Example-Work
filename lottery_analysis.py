from random import choice


def get_winning_ticket(num_letters):
    """Create a winning ticket"""
    winning_ticket = []
    print(f"Time to find out the winning ticket....: \n")

    # If length under 4 code will run choice method on possibilities
    while len(winning_ticket) < 4:
        chosen_item = choice(num_letters)
        # if not a repeat pull, append
        if chosen_item not in winning_ticket:
            print(f"Winning value: {chosen_item}")
            winning_ticket.append(chosen_item)
    return winning_ticket


def check_ticket(current_ticket, winning_ticket):
    # Check if element in current ticket matches element in winning ticket
    # If it wins return True or loses False
    for item in current_ticket:
        if item not in winning_ticket:
            return False
    # If its not False its a winning ticket
    return True


def get_random_ticket(num_letters):
    """Create a random ticket to compare to winning"""
    random_ticket = []

    while len(random_ticket) < 4:
        chosen_item = choice(num_letters)
        # No repeats again
        if chosen_item not in random_ticket:
            random_ticket.append(chosen_item)
    return random_ticket


# 10 numbers and 5 letters to compare
num_letter_base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# Winning ticket generated on base of nums/letters
winner_ticket = get_winning_ticket(num_letter_base)

# Maximum tries to stop program, 45 million as average amount of players in UK
maximum_plays = 45_000_000

# Play counter and flag variable for winner
attempts = 0
winner = False

while not winner:
    fresh_ticket = get_random_ticket(num_letter_base)
    winner = check_ticket(fresh_ticket, winner_ticket)
    attempts += 1
    if attempts >= maximum_plays:
        break

if winner:
    print(
        f"\nYour ticket {fresh_ticket} matched the winning ticket {winner_ticket} in {attempts} number of attempts")
    print("\nWould you like to play again?")
