#!/usr/bin/python3
# An insecure password storage program

PASSWORDS = {
"email": "ssjdslk23d230",
"blog": "ad9232n9d98s",
"luggage": "12345"
}

import sys, pyperclip
if len(sys.argv) < 2:
	print("Usage: python pw.py [account] - copy account's password")
	sys.exit()

account = sys.argv[1] # first command line argument is the account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print("Password for " + account + " copied to clipboard.")
else:
	print("No password stored for " + account)
