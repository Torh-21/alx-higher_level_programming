#!/usr/bin/python3

def uniq_add(my_list=[]):
    list_copy = []
    for i in my_list:
        if i not in list_copy:
            list_copy.append(i)
    return sum(list_copy)
