#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 100, 2, 13, 34, 35, -13, 98]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
