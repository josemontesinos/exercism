EQUALS_SPACE = '-', '_'


def prepare_words(words):
    for expr in EQUALS_SPACE:
        words = words.replace(expr, ' ')
    return words.split()


def abbreviate(words):
    acronym = ''
    for word in prepare_words(words):
        acronym += word[0].upper() if word[0].isalpha() else ''
    return acronym
