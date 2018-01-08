import re

phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

message = "Hello my name is Jimbo Jones and my phone number is 435-234-2342."

mo = phone_num_regex.search(message)

print("Phone number found: " + mo.group())
