#!/usr/bin/env python3
import sys

# params = sys.argv[1:]

if len(sys.argv) < 3:
	print("none")
else:
	for p in sys.argv[-1:0:-1]:
		print(p)

'''
Slicing syntax:
[start : stop : step]

start = -1 ; start from the last element
stop = 0 ; stop before index 0 (stop is excluded)
step = -1 ; move backwards

[-1:0:-1] = [1:][::-1] = [start at index 1 to the end, then reverse]
= reversed(sys.argv[1:])
'''
