#!/usr/bin/env python3

import random
# random.seed(55) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

random_nucleotide = ''
num = 0


for i in range(30):
	r = random.random()
	if  r < .2: random_nucleotide += "G"
	elif  .2 <= r < .4: random_nucleotide += "C"
	elif  .4 <= r < .7: random_nucleotide += "A"
	else: random_nucleotide += "T"



for i in range(len(random_nucleotide)):
	if random_nucleotide[i] == 'A':
		num += 1
	elif random_nucleotide[i] == 'T':
		num += 1
percent = num/len(random_nucleotide)



print(percent, random_nucleotide)



"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
