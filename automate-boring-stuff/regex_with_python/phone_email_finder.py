import pyperclip
import re

phone_regex = re.compile(r"""(
        (\d{3}|\(\d{3}\))?              # area code
        (\s|-|\.)?                      # separator
        \d{3}                           # first 3 digits
        (\s|-|\.)                       # separator
        \d{4}                           # last 4 digits
		|								# or the following
		\d{10}							# a digit char 10 times in a row
        )""", re.VERBOSE)

email_regex = re.compile(r"""(
        [a-zA-Z!#$%&'*+/=?^_`{|}~.0-9-]+    # local-part
        \@                                  # @ symbol
        [a-zA-Z0-9_-]+                      # domain
        \.                                  # dot between domain and TLD
        [a-z]+                              # TLD
        )""", re.VERBOSE)

phone_match = phone_regex.findall(pyperclip.paste())
email_match = email_regex.findall(pyperclip.paste())
phone_list = []

if (len(phone_match) > 0 or len(email_match) > 0):
	for i in range(len(phone_match)):
		phone_list.append(phone_match[i][0])

	results1 = " ".join(phone_list)
	results2 = " ".join(email_match)
	results = results1 + " " + results2

	pyperclip.copy(results)
else:
	print("No matches buddy")
