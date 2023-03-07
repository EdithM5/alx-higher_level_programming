#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastdigit = number % 10
else:
    lastdigit = (-number % 10) * -1
saythis = "and is less than 6 and not 0"
if lastdigit > 5:
    print("Last digit of", number, "is", lastdigit, "and is greater than 5")
elif lastdigit == 0:
    print("Last digit of", number, "is", lastdigit, "and is zero")
elif lastdigit < 6 and not 0:
    print("Last digit of", number, "is", lastdigit, saythis)
