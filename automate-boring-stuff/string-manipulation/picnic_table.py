def print_picnic(items_dict, left_width, right_width): # parameters include picnic dict and how spaced apart keys and values will be
	print("Picnic Items".center(left_width + right_width, "-")) # this is setup to match the columns below so everything is nicely spaced
	for k, v in items_dict.items():
		print(k.ljust(left_width, ".") + str(v).rjust(right_width, "."))

picnic_items = {"sandwiches": 10, "people": 45, "pork snouts": 99}

print_picnic(picnic_items, 2, 3)
print_picnic(picnic_items, 10, 10)
