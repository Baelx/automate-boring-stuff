cat_names = []
while True:
	print("Enter the name of a cat " + str(len(cat_names) + 1) + " or just enter nothing and this will all be over.")
	name = input()
	if name == '':
		break
	cat_names = cat_names + [name] # list concatenation
print("The cat names are:")
for name in cat_names:
	print(' ' + name)
