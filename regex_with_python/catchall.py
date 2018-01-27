import re

my_reg = re.compile(r".at")

my_str = "You're a fat cat, Garfield."

mo = my_reg.search(my_str)

print(my_reg.findall(my_str))
