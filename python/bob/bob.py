CHARS_TO_REMOVE = ' \n\t\r'


def response(hey_bob):
    # Remove unwanted chars from input
    sentence = hey_bob.translate(hey_bob.maketrans({char: None for char in CHARS_TO_REMOVE}))
    # Choose Bob's answer
    if sentence:
        yelling = sentence.isupper()
        question = sentence.endswith('?')
        resp = "Calm down, I know what I'm doing!" if yelling and question \
            else 'Sure.' if question \
            else 'Whoa, chill out!' if yelling \
            else 'Whatever.'
    else:
        resp = 'Fine. Be that way!'
    return resp
