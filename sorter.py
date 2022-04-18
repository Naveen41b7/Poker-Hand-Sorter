from collections import defaultdict
import sys


def one_pair(hand):

    """This funtion will check whether a pair exist in the hand or not.
    It will give 2 outputs, the first one is a boolean value and the second one is the pair value (if it exists)"""

    values = [v[0] for v in hand]
    value_counter = defaultdict(lambda: 0)
    for i in values:
        value_counter[i] += 1
    key_list = list(value_counter.keys())
    val_list = list(value_counter.values())
    if 2 in value_counter.values():
        return True, key_list[val_list.index(2)]
    else:
        return False, None


def two_pairs(hand):

    """This funtion will check whether there are two set of pairs in the hand or not.
    It will give 3 outputs, the first one is a boolean value, the second one is a list of 2 values whose pair exist in the hand and finally the 3rd output is a number whose pair doesn't exist."""

    pairs = []
    non_pair_value = 0
    values = [v[0] for v in hand]
    value_counter = defaultdict(lambda: 0)
    for i in values:
        value_counter[i] += 1
    key_list = list(value_counter.keys())
    val_list = list(value_counter.values())
    # For loop below finds the card's which form a pair in this hand
    for i in range(len(val_list)):
        if val_list[i] == 2:
            pairs.append(key_list[i])
        else:
            non_pair_value = key_list[i]
    if sorted(value_counter.values()) == [1, 2, 2]:
        return True, pairs, non_pair_value
    else:
        return False, None, None


def three_of_kind(hand):

    """This funtion will check whether a Three of a kind is present in the hand or not.
    It will give 2 outputs, the first one is a boolean value and the second one is the card value whose Three of a Kind exists."""

    values = [v[0] for v in hand]
    value_counter = defaultdict(lambda: 0)
    for i in values:
        value_counter[i] += 1
    key_list = list(value_counter.keys())
    val_list = list(value_counter.values())
    if 3 in value_counter.values():
        return True, key_list[val_list.index(3)]
    else:
        return False, None


def straight(hand):

    """This funtion will check whether a Straight is present in the hand or not.
    It will give 1 output which is a boolean value."""

    values = [v[0] for v in hand]
    values_only_numbers = []
    for i in values:
        values_only_numbers.append(card_sequence[i])
    if sorted(values_only_numbers) == [
        k for k in range(min(values_only_numbers), max(values_only_numbers) + 1)
    ]:
        return True
    else:
        return False


def flush(hand):

    """This funtion will check whether a Flush is present in the hand or not.
    It will give 1 output which is a boolean value."""

    suits = [s[1] for s in hand]
    if len(set(suits)) == 1:
        return True
    else:
        return False


def full_house(hand):

    """This funtion will check whether a Full House is present in the hand or not.
    It will give 1 output which is a boolean value."""

    if one_pair(hand)[0] and three_of_kind(hand)[0]:
        return True
    else:
        return False


def four_of_kind(hand):

    """This funtion will check whether a Four of a Kind is present in the hand or not.
    It will give 2 outputs. The first one is a boolean value and the 2nd one is a card value whose Four of a Kind exists."""

    values = [v[0] for v in hand]
    value_counter = defaultdict(lambda: 0)
    for i in values:
        value_counter[i] += 1
    key_list = list(value_counter.keys())
    val_list = list(value_counter.values())
    if 4 in value_counter.values():
        return True, key_list[val_list.index(4)]
    else:
        return False, None


def straight_flush(hand):

    """This funtion will check whether a Straight Flush is present in the hand or not.
    It will give 1 output which is a boolean value."""

    if straight(hand) and flush(hand):
        return True
    else:
        return False


def royal_flush(hand):

    """This funtion will check whether a Royal Flush is present in the hand or not.
    It will give 1 output which is a boolean value."""

    values = [v[0] for v in hand]
    values_only_numbers = []
    for i in values:
        values_only_numbers.append(card_sequence[i])
    if straight(hand) and flush(hand):
        if sorted(values_only_numbers)[0] == 10:
            return True
        else:
            return False


def rank_hand(hand):

    """This function will run 9 different functions where each one is checking for a possible combination of five playing cards.
    Once the combination is found it will then output a suitable rank. The default combination is High Card whose rank is 1."""

    if royal_flush(hand):
        return 10
    if straight_flush(hand):
        return 9
    if four_of_kind(hand)[0]:
        return 8
    if full_house(hand):
        return 7
    if flush(hand):
        return 6
    if straight(hand):
        return 5
    if three_of_kind(hand)[0]:
        return 4
    if two_pairs(hand)[0]:
        return 3
    if one_pair(hand)[0]:
        return 2
    return 1  # High Card


def list_comparison(
    a, b
):  # a and b have to be list with only numbers for example if it is Ace than its corresponding number would be 14

    """This function will compare two lists of numbers (with no duplicate values). This function helps in determining a winner (tie breaker) based on the highest value of card."""

    listA = sorted(a, reverse=True)
    listB = sorted(b, reverse=True)
    for i in range(0, len(a)):
        if listA[i] != listB[i]:
            if listA[i] > listB[i]:
                return "Player1"
            elif listA[i] < listB[i]:
                return "Player2"
            break  # Exit the loop
        else:
            continue  # Skip


def tie(hand1, hand2, rank):

    """When the ranks are same than this funtion is used as a tie breaker.

    How  does it work ?

    It works by comparing the highest cards in each hand; if the highest cards tie then the next highest cards are compared and so on."""

    values1 = [v[0] for v in hand1]
    values2 = [v[0] for v in hand2]
    # Converting card value to their corresponding numeric value using 'card_sequence' dictionary which is defined under the main function.
    values1_only_numbers = []
    for i in values1:
        values1_only_numbers.append(card_sequence[i])
    values2_only_numbers = []
    for i in values2:
        values2_only_numbers.append(card_sequence[i])

    if (
        rank == 1 or rank == 5 or rank == 6 or rank == 9
    ):  # High Card, Straight, Flush and Straight Flush
        return list_comparison(values1_only_numbers, values2_only_numbers)

    if rank == 2:  # One Pair
        a1, b1 = one_pair(hand1)
        a2, b2 = one_pair(hand2)
        b1 = card_sequence[b1]
        b2 = card_sequence[b2]
        # Compare the values whose pair exist in the hand
        if b1 > b2:
            return "Player1"
        elif b1 < b2:
            return "Player2"
        # If the pair card value in both players is the same than remove those card values from their respective lists and then compare the next highest card to determine a winner.
        elif b1 == b2:
            values1_only_numbers.remove(b1)
            values1_only_numbers.remove(b1)
            values2_only_numbers.remove(b2)
            values2_only_numbers.remove(b2)
            return list_comparison(values1_only_numbers, values2_only_numbers)

    if rank == 3:  # Two Pairs

        a1, b1, c1 = two_pairs(hand1)
        a2, b2, c2 = two_pairs(hand2)
        b1a = card_sequence[b1[0]]
        b1b = card_sequence[b1[1]]
        b2a = card_sequence[b2[0]]
        b2b = card_sequence[b2[1]]
        c1 = card_sequence[c1]
        c2 = card_sequence[c2]
        b1_numbers = sorted([b1a, b1b])
        b2_numbers = sorted([b2a, b2b])
        # Compare the corresponding pair value to determine a winner
        if b1_numbers[0] > b2_numbers[0]:
            return "Player1"
        elif b1_numbers[0] < b2_numbers[0]:
            return "Player2"
        elif b1_numbers[1] > b2_numbers[1]:
            return "Player1"
        elif b1_numbers[1] < b2_numbers[1]:
            return "Player2"
        # If Two Pair values are same for both players than compare the leftover card to determine a winner.
        elif c1 > c2:
            return "Player1"
        elif c1 < c2:
            return "Player2"

    if rank == 4:  # Three of a kind
        a1, b1 = three_of_kind(hand1)
        a2, b2 = three_of_kind(hand2)
        b1 = card_sequence[b1]
        b2 = card_sequence[b2]
        # Compare the card value whose Three of a Kind exists. No need to compare the remaining 2 cards in the hand as there is no chance for these card values to be same.
        if b1 > b2:
            return "Player1"
        elif b1 < b2:
            return "Player2"

    if rank == 7:  # Full House
        a1, b1 = three_of_kind(hand1)
        a2, b2 = three_of_kind(hand2)
        c1, d1 = one_pair(hand1)
        c2, d2 = one_pair(hand2)
        b1 = card_sequence[b1]
        b2 = card_sequence[b2]
        d1 = card_sequence[d1]
        d2 = card_sequence[d2]
        # Compare the Three of a Kind card value
        if b1 > b2:
            return "Player1"
        elif b1 < b2:
            return "Player2"
        # Compare the card value that has a pair in the hand.
        elif d1 > d2:
            return "Player1"
        elif d1 < d2:
            return "Player2"

    if rank == 8:  # Four of a Kind
        a1, b1 = four_of_kind(hand1)
        a2, b2 = four_of_kind(hand2)
        b1 = card_sequence[b1]
        b2 = card_sequence[b2]
        # Compare the Four of a Kind card value.
        if b1 > b2:
            return "Player1"
        elif b1 < b2:
            return "Player2"


if __name__ == "__main__":

    card_sequence = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }  # This dictionary helps in converting the hand of 5 playing cards to corresponding numeric values which helps in comparison whenever there is a tie.
    win_counter = {"Player1": 0, "Player2": 0}

    # Change filepath for different results
    filepath = "poker-hands.txt"
    hands = []
    with open(filepath, "r") as file_content:
        hands = file_content.readlines()

    for line in hands:
        line_updated = line.strip().split()
        player1_cards = line_updated[:5]
        player2_cards = line_updated[5:]

        # Ranks are different

        if rank_hand(player1_cards) > rank_hand(player2_cards):
            win_counter["Player1"] += 1
        elif rank_hand(player1_cards) < rank_hand(player2_cards):
            win_counter["Player2"] += 1

        # Ranks are same than check for the highest card in each hand

        elif rank_hand(player1_cards) == rank_hand(player2_cards):
            rank = rank_hand(
                player1_cards
            )  # You can even change the parameter to player2_cards and the result will be same as the rank for both players are same
            winner = tie(player1_cards, player2_cards, rank)
            if winner == "Player1":
                win_counter["Player1"] += 1
            elif winner == "Player2":
                win_counter["Player2"] += 1

    print(
        win_counter
    )  # The output is a dictionary summarizing the number of wins by each player.
