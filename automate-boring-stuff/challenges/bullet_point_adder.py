#!/usr/bin/python3
# bullet_point_adder.py - places a star/bullet in front of every line of a copied text

import pyperclip

text = pyperclip.paste() # here we are outputting the contents of the clipboard. We assume the user has already copied the text to be modified

lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = " * " + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text) # now we copy the contents of the modified data to the clipboard with pyperclip.copy()

text = """s;lkjsd;flkjs
it's a life
sd"""
