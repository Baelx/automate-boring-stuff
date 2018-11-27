my_pets = ['Louie', 'Murphy', 'Zax']
print("Try to guess all my pets' names.")
name = input()
if name not in my_pets:
	print("Wrong dude")
else:
	print("Yeah " + name + " is one of them, so what?")

