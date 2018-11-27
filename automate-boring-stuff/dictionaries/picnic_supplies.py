all_guests = {
"Alice": {"apples": 5, "pretzels": 2},
"Bob": {"oranges": 10, "sandwiches": 4},
"Cheryl": {"napkins": 99, "hand lotion in ml": 500},
"Alfred": {"apples": 6, "sandwiches": 8},
"Alice2": {"napkins": 2, "quik chocolate syrup bottles": 4}
} # two-dimensional dictionary

def total_brought(guests, item): # accepts dictionary as first arg and key as second arg
	num_brought = 0
	for k, v in guests.items(): # k is each guests name and v is what each of them brought(the second dictionary)
		num_brought = num_brought + v.get(item, 0) # the get method looks for keys. "item" is being used to access a key witin 2nd dict
	return num_brought

print("Number of things being brought:")
print(" - Apples " + str(total_brought(all_guests, "apples")))
print(" - Oranges " + str(total_brought(all_guests, "oranges")))
print(" - Pamplemouses " + str(total_brought(all_guests, "pamplemouses"))) # dmonstrates fallback of 0 if key doesn't exist(line 12)
print(" - Napkins " + str(total_brought(all_guests, "napkins")))
print(" - Sandwiches " + str(total_brought(all_guests, "sandwiches")))
