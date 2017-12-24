player_inventory = {
"rope": 3,
"torch": 5,
"knife": 2,
"rations": 10,
"suicide pill": 1
}

def display_inventory(my_inventory): # just takes a dict as argument
	total_num = 0
	print("Inventory:")
	for k, v in my_inventory.items(): # essentially you're iterating over a tuple since this what the items() method generates
		print(k, ":", v) # instead of making this whole thing a string, you can just use commas within the print statement
		total_num = total_num + v
	print("The total number of items is: ")
	return total_num

print(display_inventory(player_inventory))

# notice that each time you run this function, the output order is different
