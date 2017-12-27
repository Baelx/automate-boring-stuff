while True:
	print('Enter your age:')
	age = input()
	if age.isdecimal():
		break
	print('Please enter a number for your age.')

while True:
	print('Select a new password(numbers and letters only, dude)')
	password = input()
	if password.isalnum():
		break
	print('What did I just say about the numbers and letters, guy?')

