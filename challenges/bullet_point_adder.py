#!/usr/bin/python3
# bullet_point_adder.py - places a star/bullet in front of every line of a copied text

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = " * " + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
