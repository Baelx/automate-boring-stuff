import re

find_em_all = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
str0 = "This is my number: 453-343-4444, and also this: 222-222-2222"

list_of_strs = find_em_all.findall(str0) # findall method doesn't return a matched object but a list of strs as you can see in the output below

print(list_of_strs)

match_all_groups = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)") 

mo = match_all_groups.findall(str0) # since there are groups here, this returns a list of tuples as seen below

print(mo)
