# 3. Halflings are "lucky". When rolling a saving throw and the d20 comes up as a 1, 
# they can re-roll that die and take the new value, whatever that is. What are the chances
#  a halfling dies, stabilizes, or revives?

import sys
import random
			
import twoDND as two

print(two.roll(1,20))
"""
# from 2DND import unconscious

# 2DND.unconscious()


assert sys.argv[1] == "halfing"




# Probability approximation calculator
attempts = 1000000	
stabilized = 0
revived = 0
died = 0
for i in range(attempts):
	# print(unconscious())
	if unconscious() == "stabilized": stabilized += 1
	elif unconscious() == 'revived':  revived += 1
	else: died += 1
print(f' P(stabilization) = {stabilized/attempts}, P(revival) = {revived/attempts}, P(death) = {died/attempts}')




def roll(dice):
	
	return random.randint(1,dice)


"""