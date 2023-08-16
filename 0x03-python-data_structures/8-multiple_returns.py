#!/usr/bin/python3

#!/usr/bin/python3

def multiple_returns(sentence):
    sen_len = len(sentence)
    if sen_len == 0:
        first_char = None
        return (0, first_char)
    first_char = sentence[0]
    return (sen_len, first_char)
