import sys
import random
import argparse

def random_seq(length):
	sequence = ""
	for i in range(length):
		r = random.randint(0, 1000)
		if  r < 250: sequence += "A"
		elif  250 < r < 500: sequence += "T"
		elif  500 < r < 750: sequence += "C"
		else: sequence += "G"
	return sequence
seq1 = random_seq(10)
seq2 = random_seq(100)


def generate_matrix():
	matrix = []
	direction_matrix = []
	if len(seq1) > len(seq2):
		sequence = seq1
	else: sequence = seq2
	for i in range(len(sequence)+1):
		matrix.append([])
		direction_matrix.append([])
		for k in range(len(sequence)+1):
			matrix[i].append(0)
			direction_matrix[i].append(0)
	return matrix, direction_matrix

def fill_matrix(matrix, seq1, seq2, match, mismatch, gap):
	print(f'seq1:{seq1}')
	print(f'seq2:{seq2}')
	for i in range(1, len(seq1)+1):
		for k in range(1, len(seq2)+1):
			vertical = matrix[i-1][k]
			horizontal = matrix[i][k-1]
			diag = matrix[i-1][k-1]
			# Match or mismatch
			if seq1[i-1] == seq2[k-1]: 
				diag += match
			else:
				diag += mismatch

			# Gap penalty
			vertical += gap
			horizontal += gap

			#is diag, vertical, or horizontal greater?
			# carry over greatest of the 3 to next positon in matrix
			if diag > vertical and diag > horizontal and diag > 0: 
				matrix[i][k] = diag
				direction_matrix[i][k] = 'd'
			elif horizontal > vertical and horizontal > diag and horizontal > 0: 
				matrix[i][k] = horizontal
				direction_matrix[i][k] = 'l'
			elif vertical > diag and vertical > horizontal and vertical > 0: 
				matrix[i][k] = vertical
				direction_matrix[i][k] = 'u'
			# elif vertical > 0 and horizontal > 0 and vertical > 0:
			# 	matrix[i][k] = diag
			# 	direction_matrix[i][k] = 'd'
			else:
				matrix[i][k] = 0
				direction_matrix[i][k] = 'n'

	# Just for nice matrix formatting of matrix :)
	for a in matrix:
		print(a)
	print(f'-----------------------------------------------------------------')
	for b in direction_matrix:
		print(b)

	return matrix, direction_matrix

def traceback(matrix, direction_matrix, seq1, seq2):
	max = matrix[0][0]
	x_max_position = 0
	y_max_position = 0
	# Find maximum in matrix
	# This is the position where there is the highest confidence that 
	# this is a part of a shared sequence in seq1 and seq2
	for i in range(1, len(seq1)+1):
		for k in range(1, len(seq2)+1):
			if matrix[i][k] > max: 
				max = matrix[i][k]
				y_position = k
				x_position = i
	print(max)
	trace = [max]
	seq1_list = [x_position]
	seq2_list = [y_position]
	# Make traceback list
	for ok in range(1, len(seq1)+1):
		trace.append(0)
		seq1_list.append(0)
		seq2_list.append(0)
	# print(seq1, len(seq1))
	for position in range(len(seq1)):
		if direction_matrix[x_position][y_position] == 'd':
			trace[position+1] = matrix[x_position-1][y_position-1]
			y_position -= 1
			x_position -= 1

		elif direction_matrix[x_position][y_position] == 'l':
			trace[position+1] = matrix[x_position][y_position-1]
			y_position -= 1

		elif direction_matrix[x_position][y_position] == 'u':
			trace[position+1] = matrix[x_position-1][y_position]
			x_position -= 1

		else: break

		seq1_list[position +1] = x_position
		seq2_list[position +1] = y_position
	print(f'Trace:{trace}')
	# print(f'seq1_list:{seq1_list}')
	# print(f'seq2_list:{seq2_list}')

	return seq1_list, seq2_list, trace


# Now need to align them and reurn the best matching nucleotides
def align(seq1, seq2, seq1_order, seq2_order, matrix, direction_matrix, trace):
	for i in range(len(trace)):
		if trace[i] == 0:
			seq1_list.pop()
			seq2_list.pop()
	aligned_seq1 = []
	aligned_seq2 = []
	for a in range(len(seq1_list )):
		aligned_seq1.append(seq1[seq1_list[a] - 1])
	for b in range(len(seq2_list)):
		aligned_seq2.append(seq2[seq2_list[b] - 1])

	for k in range(len(aligned_seq2)):
		if aligned_seq1[k] != aligned_seq2[k]:
			aligned_seq2[k] = '-'

	return aligned_seq1, aligned_seq2



parser = argparse.ArgumentParser(description='This program finds the best alignment between two DNA sequences')

parser.add_argument('--match', required=True, type=int,
	metavar='<int>', help='required window size')
parser.add_argument('--mismatch', required=True, type=int,
	metavar='<int>', help='required window size')
parser.add_argument('--gap', required=True, type=int,
	metavar='<int>', help='required window size')

arg = parser.parse_args()


matrix, direction_matrix = generate_matrix()
matrix, direction_matri = fill_matrix(matrix, seq1, seq2,arg.match,arg.mismatch,arg.gap)
seq1_list, seq2_list, trace = traceback(matrix, direction_matrix, seq1, seq2)
aligned_seq1, aligned_seq2 = align(seq1, seq2, seq1_list, seq2_list, matrix, direction_matrix, trace)

print("".join(aligned_seq1))
print("".join(aligned_seq2))