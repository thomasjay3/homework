#!/usr/bin/env python3

import random

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

calendar = []
attempts = 100000
total = 0
number_of_people = 23
days = 365
a = 0


# More efficient method I worked on with TA Keith

for i in range(days):
	calendar.append(0)

for sample in range(attempts):
	for people in range(number_of_people):
		ri = random.randint(0, days - 1)
		calendar[ri] += 1
		a += 1
	for day in calendar:
		if day > 1: 
			total += 1
			break

	calendar = [0] * days
print(total/attempts)


# I made this one
"""
# create calendar
for i in range(1,366):
	calendar.append(i)

# how many attempts to run
for n in range(attempts):
	hits = 0
	people = []

# making group of people with random birthdays
	for person in range(number_of_people):
		person = random.choice(calendar)
		people.append(person)
	# print(people)

# do any of those people share birthdays?
	for j in range(len(people)):
		for k in range(len(people)):
			if people[j] == people[k] and j != k: 
				print("hit", people[j], people[k])
				hits += 1

# what is the percentage of attempts run where at least one pair of people share a birthday?
	if hits > 1:
		total += 1
print(total/attempts)
"""

"""
python3 33birthday.py
0.571
"""

