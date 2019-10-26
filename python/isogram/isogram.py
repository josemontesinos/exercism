def is_isogram(string):
    processed_string = string.replace(' ', '').replace('-', '').lower()
    for i in range(len(processed_string)):
        if processed_string[i] in processed_string[i+1:]:
            return False
    return True
