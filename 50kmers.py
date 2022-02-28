#!/usr/bin/env python3
# 50kmers.py

import sys

# Need to make function that opens data file
# Can sort in unix command line with "python 3 filename | sort"
# sort -k2 will sort the second column alphabetically
# sort -n -k  sorts numerically on k
# End of gumpy has the linux commands for the class


def readdna():
	with open(sys.argv[1]) as fp:
		seq = ""
		name =[]
		for line in fp.readlines():
			if line[0] == ">": 
				name.append(line)
			else: seq += line.rstrip()
	# print(len(seq))		
	return seq
# print(readfasta())

def kmer():
	k = int(sys.argv[2])
	total = 0
	count = {}
	sequence = readdna()
	# print(sequence)	
	for i in range(len(sequence) - int(k) + 1):
		kmer = sequence[i:i+int(k)]
		if kmer not in count: count[kmer] = 0
		count[kmer] += 1
		total += 1
	return count, total


if __name__ == '__main__':
	count, total = kmer()
	for i in count:
		print(i, count[i], count[i]/total)


# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
"""
python3 50kmers.py ../Data/chr1.fa 2
AA	33657	0.1106
AC	15836	0.0520
AG	18244	0.0600
AT	27223	0.0895
CA	18965	0.0623
CC	10517	0.0346
CG	8147	0.0268
CT	18142	0.0596
GA	19994	0.0657
GC	9673	0.0318
GG	10948	0.0360
GT	16348	0.0537
TA	22344	0.0734
TC	19744	0.0649
TG	19624	0.0645
TT	34869	0.1146
"""