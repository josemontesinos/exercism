VALID_CHARS = '0123456789X'


def is_valid(isbn):
    isbn = isbn.replace('-', '').upper()
    if not isbn or len(isbn) != 10 or any(c not in VALID_CHARS for c in isbn) or VALID_CHARS[-1] in isbn[:-1]:
        return False
    digits = [10 if n == VALID_CHARS[-1] else int(n) for n in isbn]
    return (sum(digits[i] * (10 - i) for i in range(10)) % 11) == 0
