LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def is_pangram(sentence):
    sentence = sentence.lower()
    for letter in LETTERS:
        if letter not in sentence:
            return False
    return True
