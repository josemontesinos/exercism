"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    dice = sorted(dice)
    if category == YACHT:
        return 50 if all(dice[i] == dice[i+1] for i in range(4)) else 0
    elif category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return category * dice.count(category)
    elif category == FULL_HOUSE:
        return 0 if (
                dice[0] != dice[1] or
                dice[3] != dice[4] or
                dice[2] not in (dice[0], dice[4]) or
                dice[0] == dice[4]
        ) else sum(dice)
    elif category == FOUR_OF_A_KIND:
        return 4 * dice[0] if all(dice[i] == dice[i+1] for i in range(0, 3)) else \
            4 * dice[1] if all(dice[i] == dice[i+1] for i in range(1, 4)) else 0
    elif category == LITTLE_STRAIGHT:
        return 30 if list(dice) == [1, 2, 3, 4, 5] else 0
    elif category == BIG_STRAIGHT:
        return 30 if list(dice) == [2, 3, 4, 5, 6] else 0
    elif category == CHOICE:
        return sum(dice)
