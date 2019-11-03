def decode(string):
    result = ''
    count = ''
    for i in range(len(string)):
        if string[i].isnumeric():
            count += string[i]
        else:
            result += string[i] * int(count or 1)
            count = ''
    return result


def encode(string):
    result = ''
    count = 0
    for i in range(len(string)):
        count += 1
        if i == len(string) - 1 or string[i] != string[i+1]:
            result += (str(count) if count > 1 else '') + string[i]
            count = 0
    return result
