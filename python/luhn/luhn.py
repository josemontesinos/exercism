class Luhn(object):

    card_num = None

    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def valid(self):
        if not self.card_num.isdigit() or len(self.card_num) <= 1:
            return False
        digits = [int(i) for i in self.card_num]
        for i in reversed(range(len(digits) % 2, len(digits), 2)):
            num = digits[i] * 2
            digits[i] = num - 9 if num > 9 else num
        return sum(digits) % 10 == 0







