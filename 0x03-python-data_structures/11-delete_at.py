#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    lists = my_list

    if idx < 0 or idx > (len(my_list))-1:
        return lists
    else:
        del lists[idx]
    return lists
