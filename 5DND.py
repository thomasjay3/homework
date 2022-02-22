# If you have the "Piercer" feat, you may re-roll a damage die. You must take the new roll regardless if it was lower than the previous roll.
#  Assume you have a weapon that does 1d8 damage. Clearly, you should re-roll any die with an initial roll of 1 damage. 
#  But what about higher rolls? Your friend Jorg re-rolls 1-6. 
# But Gastin says that's too high and re-rolls 1-3. Who does more damage on average, and when is it optimal to re-roll?


import random
import sys




def piercer(low, high, trials):
	jorge_sum = 0
	gastin_sum = 0
	for i in range(trials):

		dice = random.randint(low, high)
		# jorge
		if dice > 6:
			jorge_sum += dice
		else:
			reroll = random.randint(low, high)
			jorge_sum += reroll
		# Gastin
		if dice > 3:
			gastin_sum += dice
		else:
			gastin = random.randint(low, high)
			gastin_sum += reroll
		print()
	print(f'Jorge average ={jorge_sum/trials}. Gastin average ={gastin_sum/trials}')


# piercer(1, 10, 100000)

# I wasn't expecting their average rolls to be so close. interesting! I wonder which is the best number to set at your reroll threshold in this sitution. 


def reroll(low, high, trials):
	group = []
	for i in range(low, high):
		group.append(0)

	for i in range(trials):
		for i in range(low, high - 1):
			dice = random.randint(low, high)
			if dice > i:
				group[i] += dice
			else:
				reroll = random.randint(low, high)
				group[i] += reroll

	for i in range(low, high -1):
		group[i] = group[i] / trials
	print(group)
	return group
reroll(1, 10, 10000)