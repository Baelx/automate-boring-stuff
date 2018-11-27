def spam():
	eggs = "spam local"
	print(eggs) #prints "spam local"
def bacon():
	eggs = "bacon local"
	print(eggs) #prints "bacon local"
	spam()
	print(eggs) #prints "bacon local"

eggs = "global variable"
bacon()
print(eggs) #prints "global variable"

print("The lesson here is: \"Don't have the same name for variables in different scopes\"")
