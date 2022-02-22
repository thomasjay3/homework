# 4. You are a mage with the Fire Bolt spell. This does 1d10 damage, 
# or 5.5 points of damage on average. If you have the Elemental Adept feat, 
# damage rolls of 1 become 2. How much more damage do you do on average if you are an Elemental Adept?

import random
import sys

trials = 10000



def fire_bolt():
	if sys.argv[1] == "adept":
		sum = 0
		for i in range(trials):
			dice = random.randint(1,10)
			if dice == 1:
				dice2 = random.randint(1,10)
				sum += dice2
				# print(dice2)

			else: 
				# print(dice)	
				sum += dice

		average = sum/trials
		print(average)


	elif sys.argv[1] != "adept":
		sum = 0
		for i in range(trials):
			dice = random.randint(1,10)
			# print(dice)
			sum += dice
		average = sum/trials
		print(average)




fire_bolt()