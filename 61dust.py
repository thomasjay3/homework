#!/usr/bin/env python3
# 61dust.py

import argparse
import math
import sys
from mcb185 import read_fasta

# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library


parser = argparse.ArgumentParser(description='This program finds and masks low entropy sequences with Ns')
parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='require sequence file')
parser.add_argument('--window', required=True, type=int,
	metavar='<int>', help='required window size')
parser.add_argument('--threshold', required=True, type=float,
	metavar='<float>', help='required threshold')
arg = parser.parse_args()

def entropy_calculator(probabilities):
	h = 0
	for i in probabilities:
		if i > 0:
			h += float(i) * math.log2(float(i))
	return -h

def nucleotide_probability_generator(sequence):
	dict_nucleotides = {}
	for n in range(len(sequence)):
		nucleotide = sequence[n]
		if nucleotide not in dict_nucleotides: dict_nucleotides[nucleotide] = 0
		else: dict_nucleotides[nucleotide] += 1
	nucleotide_probabilties = []
	for i in dict_nucleotides.values():
		i /= len(sequence)
		nucleotide_probabilties.append(i)
	return nucleotide_probabilties


for name,seq in read_fasta(arg.fasta):
	dust_seq = ""
	for nucleotide in range(len(seq) - arg.window + 1):
		frame = seq[nucleotide:nucleotide + arg.window]
		if entropy_calculator(nucleotide_probability_generator(frame)) < arg.threshold:
			dust_seq += 'N'
		else:
			dust_seq += seq[nucleotide]
print(dust_seq)	


# Enter this into command line to output a FASTA file
# python3 61dust.py --fasta ../Data/chr1.fa --window 5 --threshold .5 > dust.out.fa
