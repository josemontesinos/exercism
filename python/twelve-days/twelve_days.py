VERSES = {
    1: ('first', 'a Partridge in a Pear Tree'),
    2: ('second', 'two Turtle Doves'),
    3: ('third', 'three French Hens'),
    4: ('fourth', 'four Calling Birds'),
    5: ('fifth', 'five Gold Rings'),
    6: ('sixth', 'six Geese-a-Laying'),
    7: ('seventh', 'seven Swans-a-Swimming'),
    8: ('eighth', 'eight Maids-a-Milking'),
    9: ('ninth', 'nine Ladies Dancing'),
    10: ('tenth', 'ten Lords-a-Leaping'),
    11: ('eleventh', 'eleven Pipers Piping'),
    12: ('twelfth', 'twelve Drummers Drumming'),
}

PREFIX_VERSE = 'On the {day} day of Christmas my true love gave to me:'


def recite(start_verse, end_verse):
    output = []
    for verse in range(start_verse, end_verse + 1):
        text = PREFIX_VERSE.format(day=VERSES[verse][0])
        for gift in reversed(range(1, verse + 1)):
            text += ' and ' if gift == 1 and verse != 1 else ' '
            text += VERSES[gift][1]
            text += '.' if gift == 1 else ','
        output.append(text)
    return output
