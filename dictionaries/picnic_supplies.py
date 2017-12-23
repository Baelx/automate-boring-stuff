all_guests = {
"Alice": {"apples": 5, "pretzels": 2},
"Bob": {"oranges": 10, "sandwiches": 4},
"Cheryl": {"napkins": 99, "hand lotion in ml": 500}
}

def total_brought(guests, item):
	num_brought = 0
	for k, v in guests.items():
		num_brought = num_brought + v.get(item, 0)
	return num_brought

print("Number of things being brought:")
print(" - Apples " + str(total_brought(all_guests, "apples")))
print(" - Oranges " + str(total_brought(all_guests, "oranges")))
print(" - Napkins " + str(total_brought(all_guests, "napkins")))
print(" - Sandwiches " + str(total_brought(all_guests, "sandwiches")))
