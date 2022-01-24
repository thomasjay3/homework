#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5
sum = 0
factorial = 1


for i in range(1 ,n + 1):


	# sum += range(1, n + 1)[i]

	sum += i

	factorial = factorial * i

	# factorial = factorial * range(1, n + 1)[i]

print(n,sum,factorial)

	# if i = 0:
	# 	print(sum)



# your code goes here

"""
python3 11sumfac.py
5 15 120
"""