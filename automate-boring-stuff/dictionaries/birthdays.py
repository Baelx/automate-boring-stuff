birthdays = {"Alice": "Apr 1", "Bob": "Mar 3", "Me": "May 13"}

while True:
	print("Enter a name: (Blank to quit)")
	name = input()
	if name == "":
		break

	if name in birthdays:
		print(birthdays[name] + " is the birthday of " + name)
	else:
		print("I don't know who that is or what their birthday is")
		print("Enter their birthday and I'll save it for next time")
		bday = input()
		birthdays[name] = bday
		print("Cool, now I know what the hell you're talking about")
