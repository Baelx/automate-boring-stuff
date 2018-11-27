import re

name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")

name_str = "First Name: Alfred Last Name: Wintfred"

mo = name_regex.search(name_str)

print("Found first name: " + mo.group(1) + "\nFound last name: " + mo.group(2))
