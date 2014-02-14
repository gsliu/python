#!/usr/bin/python

def in_the_fridge() :
    try:
        count = fridge[want_food]
    except KeyError:
        count = 0
    return count



fridge = {"milk" :1, "banana" :2, "apple":3}

want_food = "aaa"

c = in_the_fridge()
print c
