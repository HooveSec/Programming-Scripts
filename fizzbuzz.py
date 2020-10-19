#!/usr/bin/env python3
num = int(input())
if num % 3 == 0 and num % 5 == 0:
   print('fizzbuzz')
elif num % 3 == 0:
   print("fizz")
elif num % 5 == 0:
   print("buzz")
else:
   print('you are wrong kiddo')
# the point of fizzbuzz is to see if a number is divisible by 3 and 5, or just one, or neither.
# for more info check out https://blog.codinghorror.com/why-cant-programmers-program/
