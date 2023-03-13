#!/usr/bin/python3
def max_integer(my_list=[]):
    count = len(my_list)

    if count == 0:
        return None
    else:
        maxi = my_list[0]

        for i in range(count):
            if my_list[i] > maxi:
                maxi = my_list[i]
        return maxi
