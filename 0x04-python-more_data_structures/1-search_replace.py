#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    list_len = len(new_list)

    for i in range(list_len):
        if new_list[i] == search:
            new_list[i] = replace

    return new_list
