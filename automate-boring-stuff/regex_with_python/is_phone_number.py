import re

phone_num_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d") # this will create a regex object which has methods such as search and findall

message = "Hello my name is Jimbo Jones and my phone number is 435-234-2342."

mo = phone_num_regex.search(message) # the search method will return a MATCH OBJECT which has the group and groups methods

print("Phone number found: " + mo.group())
