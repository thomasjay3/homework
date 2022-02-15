#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

genome_size = int(sys.argv[1])

read_number = int(sys.argv[2])

read_length = int(sys.argv[3])


genome = []

# Create empty genome
for  i in range(genome_size):
	genome.append(0)

for i in range(read_number):
	r = random.randint(0, genome_size - read_length + 1)
	for j in range(r, r + read_length - 1):
		genome[j] += 1


# find in the min/max in this loop
sum = 0
for k in genome:
	sum += k

average = sum/ len(genome)
sorted_genome = genome[read_length:genome_size - read_length]
sorted_genome.sort()


print(sorted_genome[0], sorted_genome[-1], average)


# print(genome_size, read_number, read_length, average)


"""
python3 32xcoverage.py 1000 100 100
	5 20 10.82375
"""
