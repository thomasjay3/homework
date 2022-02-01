#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
num = 0


for i in range(len(dna)):
	if   dna[i] == 'G':
		num += 1
	elif dna[i] == 'C':
		num += 1



percent = num/len(dna)
print('%.2f' % (percent))
print('{:.2f}'.format(percent))
print(f'{percent:.2f}')

# I worked with Tiffany, krikor, and Bree


"""
python3 21gc.py
0.42
0.42
0.42
"""
