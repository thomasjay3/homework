#!/usr/bin/env python3
# 50kmers.py

import sys

def readdna(filename):
	with open(filename) as fp:
		seq = ""
		name =[]
		for line in fp.readlines():
			if line[0] == ">": 
				name.append(line)
			else: seq += line.rstrip()
	return seq

def kmer(filename, k):
	total = 0
	count = {}
	sequence = readdna(filename)
	for i in range(len(sequence) - int(k) + 1):
		kmer = sequence[i:i+int(k)]
		if kmer not in count: count[kmer] = 0
		count[kmer] += 1
		total += 1
	return count, total

assert(len(sys.argv) == 3) 
if __name__ == '__main__':
	count, total = kmer(sys.argv[1], int(sys.argv[2]))
	for i in count:
		print(f'{i} {count[i]} {count[i]/total:.4f}')


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