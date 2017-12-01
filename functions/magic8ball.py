import random

# jumped ahead and used a definition instead of if, elif, etc.

results = {
	1 : 'It is certain',
	2 : 'It is decidedly so',
	3 : 'Yes',
	4 : 'Reply hazy try again',
	5 : 'Ask again later',
	6 : 'Concentrate and ask again',
	7 : 'My reply is no',
	8 : 'Outlook not so good',
	9 : 'Very doubtful'
} 

def get_answer(num):
	return results[num]	

r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)
