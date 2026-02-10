#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	print("none")
else:
	s = sys.argv[1]
	count = 0
	for c in s:
		if c == 'z':
			count += 1
	if count == 0:
		print("none")
	else:
		print("z" * count)
