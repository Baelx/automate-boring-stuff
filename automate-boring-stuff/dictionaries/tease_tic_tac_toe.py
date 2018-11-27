# modeling a tic tac toe board with a dictionary

the_board = {
"tl": " ", "tm": " ", "tr": " ",
"ml": " ", "mm": " ", "mr": " ",
"bl": " ", "bm": " ", "br": " "
} # this is the starting board with all blank spaces as dictionary values

def print_board(board): # this prints the values of those dictionary keys that correspond to spaces
	print(board["tl"] + "|" + board["tm"] + "|" + board["tr"])
	print("-+-+-")
	print(board["ml"] + "|" + board["mm"] + "|" + board["mr"])
	print("-+-+-")
	print(board["bl"] + "|" + board["bm"] + "|" + board["br"])

turn = "X" # turn value, starting with X's turn

for i in range(9):
	print_board(the_board)
	print("It's time for " + turn + " to move. Which space ya want?")
	move = input()
	the_board[move] = turn
	if turn == "X":
		turn = "O"
	else:
		turn = "X"

print_board(the_board)
