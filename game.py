import json
from random import *
import re

def get_random_country():
	random_index = randint(1, 100)
	with open('countries.json') as data_file:
	    data = json.load(data_file)
	country = data["countries"][random_index]["name"]["common"].strip()

	no_vowels_country = re.sub(r'[AEIOU]', '', country, flags=re.IGNORECASE).strip()

	return [country, no_vowels_country]

def opening_message():
	print """
	Welcome to the country game. You will be given a country without its vowels,
	and you must correctly type the name of the country. If you want to skip the question, type skip.
	If you want to exit the game, type quit at any time. Here is your first question:
	"""

def check_answer(answer, country):
	if answer == country:
		return 'correct!'
	while answer != country:
		if answer == 'quit':
			return 'thanks for playing!'
			break
		elif answer == 'skip':
			return 'correct answer was: ' + country
		else:
			print 'try again, skip, or quit.'
			answer = raw_input().strip()

def run_game():
	opening_message()
	user_answer = ''

	while user_answer != 'quit':
		country = get_random_country()
		print country[1]
		user_answer = raw_input().strip()
		print check_answer(user_answer, country[0])

run_game()
