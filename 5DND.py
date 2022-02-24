# If you have the "Piercer" feat, you may re-roll a damage die. You must take the new roll regardless if it was lower than the previous roll.
#  Assume you have a weapon that does 1d8 damage. Clearly, you should re-roll any die with an initial roll of 1 damage. 
#  But what about higher rolls? Your friend Jorg re-rolls 1-6. 
# But Gastin says that's too high and re-rolls 1-3. Who does more damage on average, and when is it optimal to re-roll?


import random
import sys
import matplotlib.pyplot as mpl
import DnD1

def piercer(low, high, trials):
	jorge_sum = 0
	gastin_sum = 0
	for i in range(trials):

		dice = DnD1.roll(low, high)
		# jorge
		if dice > 6:
			jorge_sum += dice
		else:
			reroll = DnD1.roll(low, high)
			jorge_sum += reroll
		# Gastin
		if dice > 3:
			gastin_sum += dice
		else:
			gastin = DnD1.roll(low, high)
			gastin_sum += reroll
	print(f'Jorge average ={jorge_sum/trials}. Gastin average ={gastin_sum/trials}')

piercer(1, 10, 1000)

# I wasn't expecting their average rolls to be so close. interesting! I wonder which is the best number to set at your reroll threshold in this sitution. 


# This function returns the best number to reroll on given the type of dice. seems to be 6 on a d10 and 12 for a d20, pretty cool!
# wow 63 on a d100 and 638 on a d1000
# I want to know what number its approaching and why!



def reroll(low, high, trials):
	group = []
	for i in range(low, high):
		group.append(0)

	for i in range(trials):
		for i in range(low, high - 1):
			dice = DnD1.roll(low, high)
			if dice > i:
				group[i] += dice
			else:
				reroll = DnD1.roll(low, high)
				group[i] += reroll

	for i in range(low, high -1):
		group[i] = group[i] / trials
	max_average = 0
	for i in range(len(group)):
		if group[i] > max_average:
			max_average = i
	print(group)
	print(max_average - 1)
	return max_average - 1, group[1:]

if __name__ == "__main__": 
	ma, grp = reroll(1, 20, 100)
	mpl.plot(grp)
	mpl.show()
