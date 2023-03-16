#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_to_list1 = set(set_1).symmetric_difference(set(set_2))
    return unique_to_list1
