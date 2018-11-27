import random

messages = ['It is certain',
	'It is decidedly so',
	'It\'s a me, Mario',
	'No way, Jose',
	'Outcome seems fuzzy',
	'Ask again, friend',
	'Something seems fishy']

print(messages[random.randint(1, len(messages) -1)])
