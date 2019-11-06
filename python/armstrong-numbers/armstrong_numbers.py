def is_armstrong_number(number):
    num_str = str(number)
    return sum([int(digit)**len(num_str) for digit in num_str]) == number
