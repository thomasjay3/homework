#!/usr/bin/env python3

import sys

# Make a program that reports the amino acid composition in a file of proteins
# Use a dictionary to count the letters
# Sorting the amino acids by frequency is optional


A = 0
G = 0
V = 0
C = 0
P = 0
L = 0
I = 0
M = 0
W = 0
F = 0
L = 0
R = 0
H = 0
S = 0
T = 0
Y = 0
N = 0
Q = 0
D = 0
E = 0
K = 0
length = 0

assert(len(sys.argv) == 2)
with open(sys.argv[1]) as fp:
	for line in fp.readlines():
		if line[0] != '>':
			seq = line.rstrip()
			for i in seq:
				if i != "*":
					length += 1
					if i == 'A':   A += 1
					elif i == 'G': G += 1
					elif i == 'K': K += 1
					elif i == 'V': V += 1
					elif i == 'C': C += 1
					elif i == 'P': P += 1
					elif i == 'L': L += 1
					elif i == 'I': I += 1
					elif i == 'M': M += 1
					elif i == 'W': W += 1
					elif i == 'F': F += 1
					elif i == 'L': L += 1
					elif i == 'R': R += 1
					elif i == 'H': H += 1
					elif i == 'S': S += 1
					elif i == 'T': T += 1
					elif i == 'Y': Y += 1
					elif i == 'N': N += 1
					elif i == 'Q': Q += 1
					elif i == 'D': D += 1
					elif i == 'E': E += 1

print(f'W {W} {W/length}')
print(f'C {C} {C/length}')
print(f'H {H} {H/length}')
print(f'M {M} {M/length}')
print(f'Y {Y} {Y/length}')
print(f'Q {Q} {Q/length}')
print(f'F {F} {F/length}')
print(f'N {N} {N/length}')
print(f'P {P} {P/length}')
print(f'T {T} {T/length}')
print(f'R {R} {R/length}')
print(f'I {I} {I/length}')
print(f'D {D} {D/length}')
print(f'G {G} {G/length}')
print(f'A {A} {A/length}')
print(f'K {K} {K/length}')
print(f'E {E} {E/length}')
print(f'V {V} {V/length}')
print(f'L {L} {L/length}')
print(f'S {S} {S/length}')


# "Do this without dictionaries"

"""
python3 41aacomp.py ../Data/at_prots.fa
W 528 0.012054244098442994
C 801 0.018286836217524315
H 1041 0.023766038080452946
M 1097 0.025044518515136296
Y 1281 0.02924523994338158
Q 1509 0.03445048171316378
F 1842 0.04205287429797726
N 1884 0.04301173462398977
P 2051 0.046824345920277614
T 2153 0.04915300671202228
R 2320 0.05296561800831012
I 2356 0.05378749828774942
D 2573 0.05874160997214739
G 2732 0.06237158120633761
A 2772 0.06328478151682572
K 2910 0.06643532258800967
E 2989 0.06823889320122369
V 3001 0.06851285329437012
L 3950 0.09017853066070042
S 4012 0.09159399114195699
"""

