while True:
	try:
		x = int(input("Can I get yo numbah? \n"))
		break
	except ValueError:
		print("That ain't a numbah")
