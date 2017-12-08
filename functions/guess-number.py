# guess the number game

import random

secret_number = random.randint(1,20)
print("Guess a number between 1 and 20")

# Ask player to guess six times
for guesses_taken in range(1,7):
	try:
		guess = int(input("What's your guess? \n"))
	except ValueError:
		print("that's not even a number")
		continue
	
	if guess < secret_number:	
		print("Ha Ha, too low.")
	elif guess > secret_number:
		print("Ha Ha, too high.")
	else:
		break # This means they got it.

if guess == secret_number:
	print("Fine you win. It took you " + str(guesses_taken) + " guesses." )
else:
	print("Forget it, I'm not going to sit around here and let you be wrong all day")
