def spam(num):
	try:
		return 42 / num
	except ZeroDivisionError:
		print("Error: Invalid argument ya busta")
print(spam(6))
print(spam(0))
print(spam(2))
