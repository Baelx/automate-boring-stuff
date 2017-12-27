feelings = {
"positive": ["good", "great", "fine"],
"neutral": ["ok", "okay", "meh", "not bad", "pas mal"],
"negative": ["bad", "awful", "terrible", "not good"]
} # here I've got a dictionary with lists for each mood as values

print("Hi, how are you?")
response = input()
if response.lower() in feelings["positive"]: # remember that to output the value of a certain dictionary key, you need to access it with the key
	print("Happy for you!")
elif response.lower() in feelings["neutral"]:
	print("Why just ok?")
else:
	print("Cheer up! Better days ahead.")

"""At first I was trying to loop through each dictionary and array with 
for loops, while loops, conditionals. All I needed to do was use the "in"
operator
"""
