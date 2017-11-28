while True:
	print("Who are you?")
	name = input()
	if name == "Alex":
		continue
	print("Hello " + name + ", what is the numerical password?")
	password = input()
	if password == "13":
		continue
	print("Thank you. Would you like to keep this password or change it?(Enter \"keep\" or \"change\")")
	response = input()
	if response == "change":
		print("Enter new numerical password")
		password = input()
		print("Your new password is " + str(password) + ".")
	elif response == "keep":
		break
print("Welcome to this place")
