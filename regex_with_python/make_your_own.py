import re

my_char_class = re.compile(r"[a-d]+")

mo = my_char_class.findall("forty six and two are just ahead of me")

print(mo)
