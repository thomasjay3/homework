#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix

protein_list = []
names = []

# Amino Acid One Letter Code Hydropathy Score
# I = 4.5
# V = 4.2
# L = 3.8
# F = 2.8
# C = 2.5
# M = 1.9
# A = 1.8
# G = -0.4
# T = -0.7
# S = -0.8
# W = -0.9
# Y = -1.3
# P = -1.6
# H = -3.2
# E = -3.5
# Q = -3.5
# D = -3.5
# N = -3.5
# K = -3.9
# R = -4.5

# Open protein file and creating a list for proteins and corresponding protein names
assert(len(sys.argv) == 2)
with open(sys.argv[1]) as fp:
	seq = ""
	for line in fp.readlines():
		if line[0] == ">":
			protein_list.append(seq)
			names.append(line.rstrip())
			seq = ""
		else:seq += line.rstrip()

# Lining up proteins with their correct names 
protein_list = protein_list[1:]




# KD calculation
def kd(protein):
	hydrophobicity = 0
	for aa in protein:
		if aa ==   "I": hydrophobicity += 4.5
		elif aa == "V": hydrophobicity += 4.2
		elif aa == "L": hydrophobicity += 3.8
		elif aa == "F": hydrophobicity += 2.8
		elif aa == "C": hydrophobicity += 2.5
		elif aa == "M": hydrophobicity += 1.9
		elif aa == "A": hydrophobicity += 1.8
		elif aa == "G": hydrophobicity -= 0.4
		elif aa == "T": hydrophobicity -= 0.7
		elif aa == "S": hydrophobicity -= 0.8
		elif aa == "W": hydrophobicity -= 0.9
		elif aa == "Y": hydrophobicity -= 1.3
		elif aa == "P": hydrophobicity -= 1.6
		elif aa == "H": hydrophobicity -= 3.2
		elif aa == "E": hydrophobicity -= 3.5
		elif aa == "Q": hydrophobicity -= 3.5
		elif aa == "D": hydrophobicity -= 3.5
		elif aa == "N": hydrophobicity -= 3.5
		elif aa == "K": hydrophobicity -= 3.9
		elif aa == "R": hydrophobicity -= 4.5
	return hydrophobicity

def fatty_seq(protein, window, threshold):
	for i in range(len(protein) - window + 1):
		pep = protein[i : i + window]
		# print(pep, kd(pep))
		if kd(pep) > threshold and 'P' not in pep:
			print(pep, kd(pep))
			return True
	return False

# print(fatty_seq(protein_list[35], 11, 2.5))

total = 0
for protein, name in zip(protein_list, names):
	if fatty_seq(protein[:30], 8, 2.5) and fatty_seq(protein[30:], 11, 2.0):
		total += 1
		print(name[1:13])

print(f'Total:{total}')

"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
