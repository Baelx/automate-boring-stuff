def spam():
	global eggs
	eggs = "spam" #this is the global

def bacon():
	eggs = "bacon" #this is local
def ham():
	print(eggs)

eggs = 42 #this is global
spam()
print(eggs)

