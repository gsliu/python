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


A = 1
B = 2
C = 3

if (A == 1 and
	B == 2 and
	C == 3) :
	print('spam'*3)



while True:
	reply = raw_input()
	if (reply == "stop") :
		break
	print("input %s wrong"  % (reply.upper()))

