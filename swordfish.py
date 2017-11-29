while True:
	print("Enter valid username")
	name = input()
	if name != "Alex":
		print("Wrong.")
		continue
	print("Hello " + name + ", what is the numerical password?")
	password = input()
	if password != "12345":
		print("Wrong password. Restarting.")
		continue
	print("Thank you. Would you like to keep this password or change it?(Enter \"keep\" or \"change\")")
	response = input()
	if response == "change":
		print("Enter new numerical password")
		password = input()
		print("Your new password is " + str(password) + ".")
		break
	elif response == "keep":
		break
print("Welcome to this place")
