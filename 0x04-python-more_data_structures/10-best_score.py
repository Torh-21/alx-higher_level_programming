#!/usr/bin/python3

def best_score(a_dictionary):
    max_score = 0
    max_key = ""
    if a_dictionary is None:
        return None
    else:
        for key, value in a_dictionary.items():
            if a_dictionary[key] > max_score:
                max_score = a_dictionary[key]
                max_key = key
    return max_key
