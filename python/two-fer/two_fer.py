def two_fer(name=None):
    msg = "One for {}, one for me."
    return msg.format(name or 'you')
