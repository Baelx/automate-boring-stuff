
def list_to_string(list):
	new_str = ", ".join(str(e) for e in list)
	last_comma = new_str.rfind(",")
	newer_str = new_str[:last_comma + 1] + " and" + new_str[last_comma + 1:]
	print(newer_str)		
list_to_string(['hello',45,'me'])
