import re

print("""This program checks the dialogue of adherents of the cult of the leader.

True and devout adherents will begin all sentences with: \"I love the Leader.\"

Please enter your sentence to have it validated for allegiance.\n""")

sentence = input()

def allegiance_checker(text):
	allegiance_regex = re.compile(r"^I love the Leader. ")
	if allegiance_regex.match(text):
		print("\nThis sentence is a true and loyal sentence. You have been blessed by the Leader.")
	else:
		print("\nBegone and take your unholy sentence with you.")

allegiance_checker(sentence)
