import random

dice1 = random.randint(1, 20)

dice2 = random.randint(1,20)
print(dice1, dice2)

# Normal Roll
print(f'Normal roll:{dice1}')


#Advantage
if dice1 > dice2: print(f'Advantage Roll: {dice1}')
else: print(f'Advantage Roll: {dice2}')


# Disadvantage
if dice1 > dice2: print(f'Disadvantage Roll: {dice2}')
else: print(f'Disadvantage Roll: {dice1}')