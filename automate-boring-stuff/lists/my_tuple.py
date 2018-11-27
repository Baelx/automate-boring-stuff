my_tuple = ('fort', 3, 'seven')
my_list = ['fort', 3, 'seven']

print("this is my tuple " + str(my_tuple))
print("this is my list " + str(my_list))

print("Fun game: Enter a data type and I'll tell you if it's mutable or immutable")

foo = input()
if foo == "tuple":
	print("Immutable")
elif foo == "list":
	print("mutable")
elif foo == "string":
	print("immutable")
