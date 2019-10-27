import re


def set_header(text):
    for hashtag_set in ('######', '##', '#'):
        if re.match(hashtag_set + ' (.*)', text):
            text = '<h{}>'.format(len(hashtag_set)) + text[len(hashtag_set) + 1:] + '</h{}>'.format(len(hashtag_set))
    return text


def set_bold(text):
    match = re.match('(.*)__(.*)__(.*)', text)
    if match:
        text = match.group(1) + '<strong>' + match.group(2) + '</strong>' + match.group(3)
    return text


def set_italic(text):
    match = re.match('(.*)_(.*)_(.*)', text)
    if match:
        text = match.group(1) + '<em>' + match.group(2) + '</em>' + match.group(3)
    return text


def set_paragraph(text):
    if not re.match('<h|<ul|<p|<li', text):
        text = '<p>' + text + '</p>'
    return text


def parse(markdown):
    result = ''
    in_list = False
    in_list_append = False
    for line in markdown.split('\n'):
        line = set_header(line)
        list_item = re.match(r'\* (.*)', line)
        if list_item:
            line = ('<ul>' if not in_list else '') + '<li>' + set_italic(set_bold(list_item.group(1))) + '</li>'
            in_list = True
        else:
            if in_list:
                in_list_append = True
                in_list = False
        line = set_paragraph(line)
        line = set_bold(line)
        line = set_italic(line)
        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        result += line
    if in_list:
        result += '</ul>'
    return result
