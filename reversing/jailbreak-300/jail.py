#!/usr/bin/env python 

from __future__ import print_function

print("Escape the python sandbox.")

banned = [  
    "import",
    "exec",
    "eval",
    "pickle",
    "os",
    "subprocess",
    "input",
    "banned",
    "sys"
]

targets = __builtins__.__dict__.keys()
targets.remove('raw_input')
targets.remove('print')
targets.remove('NameError')
for x in targets:  
    del __builtins__.__dict__[x]

while 1:  
    try:
	print(">>>", end=' ')
	data = raw_input()

	for no in banned:
	    if no.lower() in data.lower():
		print("Nuh uh uhhhhh")
		break
	else: # this means nobreak
	    exec data
    except NameError as e:
        print("NameError: ", e)
