import random


def roll(low, high):
	dice = random.randint(low, high)
	return dice

if __name__ == "__main__": 
	dice1 = roll(1, 20)
	dice2 = roll(1, 20)
	
	# Normal Roll
	print(f'Normal roll:{dice1}')


	#Advantage
	if dice1 > dice2: print(f'Advantage Roll: {dice1}')
	else: print(f'Advantage Roll: {dice2}')


	# Disadvantage
	if dice1 > dice2: print(f'Disadvantage Roll: {dice2}')
	else: print(f'Disadvantage Roll: {dice1}')