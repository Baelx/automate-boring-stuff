grid = [['.', '.', '.', '.', '.', '.'],
	['.', 'O', 'O', '.', '.', '.'],
	['O', 'O', 'O', 'O', '.', '.'],
	['O', 'O', 'O', 'O', 'O', '.'],
	['.', 'O', 'O', 'O', 'O', 'O'],
	['O', 'O', 'O', 'O', 'O', '.'],
	['O', 'O', 'O', 'O', '.', '.'],
	['.', 'O', 'O', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.']]

for i in range(len(grid[0])):
	for x in range(len(grid)):
		print(grid[x][i], end="")
	print("\n")

# flipped this one 90 degrees to the right
