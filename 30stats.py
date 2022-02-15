#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

numbers = [3, 1, 4, 1, 5]
count = 0
sum = 0
std_sum = 0
print(numbers)

for i in enumerate(numbers):
	numbers.sort()
	numbers
	count += 1

for j in range(len(numbers)): 
	sum += numbers[j]

for k in range(len(numbers)):
	std_sum += (numbers[k]-sum/count)**2

for k in range(len(numbers)):
	if numbers[k] == numbers[-k-1]: median = numbers[k]


print(f'Count: {count}')
print(f'Minimum: {numbers[0]:.1f}')
print(f'Maximum: {numbers[-1]:.1f}')
print(f'Mean: {sum/count:.3f} ')
print(f'Std. {std_sum/count-1:.3f}')
print(f'Median: {median:.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
