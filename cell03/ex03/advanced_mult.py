#!/usr/bin/env python3

import sys

# If there is any argument, print "none"
if len(sys.argv) != 1:
    print("none")
else:
    i = 0
    while i <= 10:
        print(f"Table de {i}:", end=" ")
        j = 0
        while j <= 10:
            print(i * j, end=" ")
            j += 1
        print()
        i += 1
