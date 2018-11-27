import re

def batman_finder(message):
	bat_regex_finder = re.compile(r"Bat(man|mobile|copter|rope|boat)")
	mo = bat_regex_finder.search(message)
	if len(mo.group()) > 1: 
		print("At least one instance of a batman product found: " + mo.group())
	else:
		print("No Bat things in that there sentence")

batman_finder("Hi, this is Batman wishing you a merry xmas")
