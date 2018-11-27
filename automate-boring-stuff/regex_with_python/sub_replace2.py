import re

my_reg = re.compile(r"Agent (\w)\w*")

my_str = my_reg.sub(r"\1****", "Agent Alice was better than Agent Teddy but lacked Agent Johnny's cunning.")

print(my_str)
