import re

test_regex = re.compile(r"\w+") # find all words in a sentence.

test_str = "This is an example sentence."

matches = test_regex.findall(test_str)

print(matches)
