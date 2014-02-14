#!/usr/bin/python
# -*- coding: utf-8 -*-
# guess.py
import random
 
guessesTaken = 0
 
print ('Hello! what is your name')
#myName = raw_input()
myName = input()
number = random.randint(1, 23)
print ('well, ' + myName + ', i am thinking of a number between 1 and 23.')
 
while guessesTaken < 7:
    print ('Take a guess')
    guess = input()
    #guess = int(guess)
 
    guessesTaken = guessesTaken + 1
 
    if guess < number:
        print ('your guess is too low')
    if guess > number:
        print ('your guess is too high')
    if guess == number:
        break
 
if guess == number:
    print ('good job! you guess in %d guesses!' %guessesTaken)
 
if guess != number:
    print ('sorry! your guess is wrong')
