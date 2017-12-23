import pprint # This module helps pretty print data like our dictionary below

message = "Sitting in a speeding box, watching the icey air fill with standing twigs."
count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1

pprint.pprint(count)
