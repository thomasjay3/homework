#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys


length = len(sys.argv[1:])
sum = 0
	
for i in range(1, length+1):
	y = 1
	y *= float(sys.argv[i]) * math.log(float(sys.argv[i]), 2)
	sum += y

print(f'{-sum:.3f}')






"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
