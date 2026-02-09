#!/usr/bin/env python3

import math

number = float(input("Give me a number: "))
print(math.ceil(number))

'''
math.ceil(): Rounds a number up to the nearest integer

verson without math:
number = float(input("Give me a number: "))

if number.is_integer():
if number == int(number):
	print(int(number))
else:
	print(int(number) + 1)
'''