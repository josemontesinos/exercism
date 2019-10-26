mapping = {
    3: 'Pling',
    5: 'Plang',
    7: 'Plong'
}


def convert(number):
    ret = ''
    for factor in mapping:
        if not number % factor:
            ret += mapping[factor]
    if not ret:
        ret = str(number)
    return ret
