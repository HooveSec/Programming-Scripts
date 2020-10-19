#!/usr/bin/env python3
import random
a = random.randint(1,100)#how high you want the range

def guess_number(a):
   import random
   guess = int(input())
   a = random.randint(1, 100)#how high you want the range
   guesses = 0
   while guesses < 6:
       if guess == a:
           print('How did you know')
           break
       if guess > a:
           print('Your number is higher then mine, Guess Again')
           guesses += 1
           guess = int(input())
           print('you have guessed this many times:',guesses + 1)
           continue
       if guess < a:
           print('Your number is lower then mine, Guess Again')
           guesses  += 1
           guess = int(input())
           print('you have guessed this many times:',guesses + 1)
           continue
       if guesses == 6:
           print('Out of chances dawg')
   if guess == a:
       print('you got it')

