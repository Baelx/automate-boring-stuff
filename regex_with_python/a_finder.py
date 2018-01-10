import re

print("""This program checks if a sentence contains at least one a.

Enter your sentence:""")

message = input()

def a_finder(mes):
	a_regex = re.compile(r"a+")
	mo = a_regex.search(mes)
	if bool(mo.group()) == True:
		print("There's an a in there.")
	else:
		print("No a in there.")
a_finder(message)
