print("""Welcome to the String to List Converter.

If you enter a string, I'll make a list out of it.

Enter your data:""")
entry = input()
if type(entry) is str:
	print(entry.split())
else:
	print("Error, unsupported data type.")
