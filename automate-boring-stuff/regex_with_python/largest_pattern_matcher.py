import re

most_possible = re.compile(r"(ha){1,3}") # python regex will match the highest possible grouping of ha's - it'll aim for the 3 if it's possible
least_possible = re.compile(r"(ha){1,4}?") # with a question mark at the end, python will aim for the shortest possible match

str2 = "ha"
str0 = "haha"
str1 = "hahaha"
str4 = "hahahaha"


mo = most_possible.search(str0)
mo2 = most_possible.search(str1)
mo3 = most_possible.search(str2)
mo4 = least_possible.search(str4)

print("Greedy matching: " + mo.group(), mo2.group(), mo3.group(), mo2.groups())

print("Non-greedy matching: " + mo4.group())
