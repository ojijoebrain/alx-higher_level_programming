#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list.copy()
    if idx < 0:
        return copy_list
    elif idx > len(copy_list):
        return copy_list
    else:
        copy_list[idx] = element
        return copy_list
    return copy_list
