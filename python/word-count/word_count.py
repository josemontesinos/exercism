IGNORE = '\n', '"', '!', '?', ':', '&', '@', '$', '%', '^'
EQUALS_SPACE = '\t', " '", "' ", '_', ',', '.'
REMOVE_FROM_START_AND_END = '"', "'"


def prepare_sentence(sentence):
    for expr in IGNORE:
        sentence = sentence.replace(expr, '')
    for expr in EQUALS_SPACE:
        sentence = sentence.replace(expr, ' ')
    if sentence[0] in REMOVE_FROM_START_AND_END:
        sentence = sentence[1:]
    if sentence[-1] in REMOVE_FROM_START_AND_END:
        sentence = sentence[:-1]
    return sentence.lower().split()


def count_words(sentence):
    sentence = prepare_sentence(sentence)
    word_count = {}
    for word in sentence:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
