import re

my_reg = re.compile(r".*", re.DOTALL)

result = my_reg.search("Search the public trust.\nIncrease revenue.\nCapitulate to consumer demand.")

print("This kind of matching can be useful if you need to catch special charcters like newlines, spaces, tabs, etc: " + str(result.group()))
