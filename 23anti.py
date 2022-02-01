#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
complement = ''

for i in range(len(dna)+1):
	if   dna[-i] == 'A':
		complement += 'T'
	elif dna[-i] == 'T':
		complement += 'A'
	elif dna[-i] == 'C':
		complement += 'G'
	else:
		complement += 'C'

print(complement)	

# I worked with Tiffany, krikor, and Bree


"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
