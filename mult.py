#!/usr/bin/env python
# ECE 2524 | Homework 3, Problem 1 | Brandon Fairburn

import sys

argv = sys.argv
argc = len(argv)

help_msg = """usage: mult.py [-h]

Process some numbers.

optional arguments:
	-h, --help	show this help message and exit"""

def mult( numbers ):
	product = 1
	for x in numbers:
		product = float(x) * product
	return product

if argc > 2:
	sys.stderr.write(help_msg)
	quit(1)

if argc == 2:
	if argv[1] == "-h" or argv[1] == "--help":
		print help_msg
		quit(0)
	else:
		sys.stderr.write("usage: mult.py [-h]")
		sys.stderr.write("\n\n%s: error: unrecognized arguments: %s" %(argv[0],argv[1])) 
		quit(1)
		
nums = []
for line in sys.stdin:
	# print product and reset on blank lines
	if line == '\n':
		product = mult(nums)
		del nums[:]
		print "Product is: ", product
		continue
		
	# error if non-numeric line is entered
	try:
		val = float(line)
	except ValueError:
		sys.stderr.write("could not convert string to float: %s" %line)
		quit(1)
	nums.append(line)

product = mult(nums)
	
print "\nProduct is: ", product