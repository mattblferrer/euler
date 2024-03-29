"""
The squares are numbered according to their position on the board in a clockwise
direction from GO, from 0 to 39.
"""
from random import random, shuffle


# returns the roll on two dice of side number num
def roll_dice(num: int) -> tuple[int]:
    return int(random()*num) + 1, int(random()*num) + 1


# shuffles the CC and CH cards (at the start of the game)
def shuffle_cards() -> tuple[list[int]]:
    # initialize CC and CH decks
    cc_cards = list(range(1, 3)) + [0]*14  # 2/16 movement cards
    ch_cards = list(range(1, 11)) + [0]*6  # 10/16 movement cards

    # shuffle
    shuffle(cc_cards)
    shuffle(ch_cards)

    return cc_cards, ch_cards


# returns position of next railway company
def next_railway(position: int) -> int:
    # always built in the middle of every side
    next_pos = (((position - 5)//10 + 1)*10 + 5) % 40
    return next_pos


# returns position of next utility company
def next_utility(position: int) -> int:
    if 12 <= position < 28:  # U1 = 12, U2 = 28
        return 28
    return 12


# returns the outcome of community chest card
def community_chest(cc_cards: list[int], position: int) -> int:
    # take top card and move to bottom
    top_card = cc_cards.pop(0)
    cc_cards.append(top_card)

    # outcomes of cards
    cards = [0, 10]  # squares to go to
    if top_card == 0:  # not movement card
        return position
    return cards[top_card - 1]


# returns the outcome of chance card
def chance(ch_cards: list[int], position: int) -> int:
    # take top card and move to bottom
    top_card = ch_cards.pop(0)
    ch_cards.append(top_card)

    # outcomes of cards
    cards = [0, 10, 11, 24, 39, 5]  # squares to go to
    if top_card == 0:  # not movement card
        return position

    elif top_card in range(1, 7):  # go to square X
        return cards[top_card - 1]
    
    elif top_card in range(7, 9):  # go to next railway
        return next_railway(position)

    elif top_card == 9:  # go to next utility
        return next_utility(position)

    # go back 3 squares
    return (position - 3) % 40


# returns the most landed on squares for a given number of turns
def simulation(turns: int) -> tuple[float]:
    # initialize counting of landed squares
    landed_squares = [0]*40

    # shuffle CC and CH cards
    cc_cards, ch_cards = shuffle_cards()

    current_square = 0  # starting square = GO
    doubles = 0  # number of consecutive doubles

    for _ in range(turns):
        raw_roll = roll_dice(4)  # tuple of two dice rolls

        # check for doubles
        if raw_roll[0] == raw_roll[1]:
            doubles += 1

        else:
            roll = sum(raw_roll)  # sum of two dice rolls
            doubles = 0  # reset doubles count if not double
            current_square = (current_square + roll) % 40

            # check for CC square
            if current_square in {2, 17, 33}:
                current_square = community_chest(cc_cards, current_square)

            # check for CH square
            elif current_square in {7, 22, 36}:
                current_square = chance(ch_cards, current_square)

            # check for go to jail square
            elif current_square == 30:
                current_square = 10

        # advance to jail on 3rd double
        if doubles == 3:
            current_square = 10

        landed_squares[current_square] += 1  # add to frequency

    # calculate probabilities
    landed_squares = [i / turns for i in landed_squares]

    # return result
    return landed_squares


# finds the modal string given an array of probabilities
def modal_string(probabilities: tuple[float]) -> str:
    # get max index of 3 biggest probabilities
    max_three = sorted(zip(probabilities, range(40)), reverse=True)[:3]
    return "".join("{:02d}".format(value[1]) for value in max_three)


# simulation results
simulatedResults = simulation(1000000)
print(simulatedResults)
print(modal_string(simulatedResults))
