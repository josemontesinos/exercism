ONE_POINT = (('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'), 1)
TWO_POINTS = (('D', 'G'), 2)
THREE_POINTS = (('B', 'C', 'M', 'P'), 3)
FOUR_POINTS = (('F', 'H', 'V', 'W', 'Y'), 4)
FIVE_POINTS = (('K', ), 5)
EIGHT_POINTS = (('J', 'X'), 8)
TEN_POINTS = (('Q', 'Z'), 10)
SCORE_TUPLES = (ONE_POINT, TWO_POINTS, THREE_POINTS, FOUR_POINTS, FIVE_POINTS, EIGHT_POINTS, TEN_POINTS)


def get_letter_score(letter):
    for tuple in SCORE_TUPLES:
        if letter.upper() in tuple[0]:
            return tuple[1]


def score(word):
    points = 0
    for letter in word:
        points += get_letter_score(letter)
    return points
