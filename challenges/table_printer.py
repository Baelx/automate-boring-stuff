table_data = [
["apples", "pears", "peaches", "tomatoes"],
["Alex", "Ali","Justine","Kevin"],
["spam", "cheese", "bread", "sausage"]
]

def print_table(table):
	col_widths = [0] * len(table)
	for i in range(len(table)):
		for x in range(len(table[i])):
			if len(table[i][x]) > col_widths[i]:
				col_widths[i] = len(table[i][x]) # checks for longest str in "column"

	for i in range(len(table[0])): # works like the "flip_pattern.py" function
		for x in range(len(table)):
			print(table[x][i].rjust(col_widths[x]), end=" ")
		print("\n")

print_table(table_data)
