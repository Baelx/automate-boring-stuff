import re

hl_regex = re.compile(r"(ha){1,3}")

soft_laugh = "ha"
medium_laugh = "haha"
hard_laugh = "hahaha"

mo2 = hl_regex.search(hard_laugh)

print(mo2.group())

def hard_laugh_tester(laugh):
	mo = hl_regex.search(laugh)
	if len(mo.group()) == 6:
		print("gafaawww")
	elif len(mo.group()) == 4:
		print("Worth a chuckle")
	elif len(mo.group()) == 2:
		print("You have no soul")

hard_laugh_tester(soft_laugh)
hard_laugh_tester(medium_laugh)
hard_laugh_tester(hard_laugh)
