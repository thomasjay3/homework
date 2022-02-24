import random
import DnD1 

def unconscious():
	# print("You have become unconscious and may die.")
	health  = 0
	attempts = 0
	success = 0
	failure = 0
	s = "stabilized"
	d = "died"
	r = "revived"
	while health == 0:
		dice = DnD1.roll(1, 20)
		attempts += 1
		if success > 1:
			# print("You have stabilized!")
			health += 1
			return s
		if failure ==  3: 
			# print("You have died!")
			health -= 1
			return d
		if   dice < 2:  failure += 2
		elif dice < 10: failure += 1
		elif dice < 20: success += 1
		else: 
			# print("Luck is in your favor today! You have revived!")
			health += 1
			return r

if __name__ == "__main__": 
	# Probability approximation calculator
	attempts = 100000
	stabilized = 0
	revived = 0
	died = 0
	for i in range(attempts):
		# print(unconscious())
		if unconscious() == "stabilized": stabilized += 1
		elif unconscious() == 'revived':  revived += 1
		else: died += 1
	print(f' P(stabilization) = {stabilized/attempts}, P(revival) = {revived/attempts}, P(death) = {died/attempts}')

# Death saves are a little different than normal saving throws. 
# If your health drops to 0 or below, you are unconscious and may die. 
# Each time it is your turn, roll a d20 to determine if you get closer 
# to life or fall deeper into death. If the number is less than 10, you
# record a "failure". If the number is 10 or greater, you record a "success". 
# If you collect 3 failures, you "die". If you collect 3 successes, you are "stable"
# but unconscious. If you are unlucky and roll a 1, it counts as 2 failures.
# If you're lucky and roll a 20, you gain 1 health and have "revived". 
# Write a program that simulates death saves. 
# What is the probability you die, stabilize, or revive?
