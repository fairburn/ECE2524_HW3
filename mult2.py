#!/usr/bin/env python
# ECE 2524 | Homework 3, Problem 1 | Brandon Fairburn

import sys
import os
import fileinput

argv = sys.argv
argc = len(argv)

help_msg = """usage: mult.py [-h]

Process some numbers.

optional arguments:
	-h, --help	show this help message and exit"""

ignore_blank = False
ignore_nonn = False

# create dummy files so fileinput won't complain
# (it opens every string given on the command line)
open('--ignore-blank', 'w').close()
open('--ignore-non-numeric', 'w').close()
	
# process command line args
for arg in argv:
	if arg == "--ignore-blank":
		ignore_blank = True
	if arg == "--ignore-non-numeric":
		ignore_nonn = True
	if arg == "-h" or arg == "--help":
		print help_msg
		quit(0)

# returns product of all numbers given as input
def mult( numbers ):
	product = 1
	for x in numbers:
		product = float(x) * product
	return product

nums = [] # array of input numbers

# executes if given files
# logic explained:
# open in fileinput mode in the following cases:
#	case 1: mult.py --ignore-xxxx [files] --> argc >= 3, ignore_blank XOR ignore_nonn
#	case 2: mult.py --ignore-blank --ignore-non-numeric [files] --> argc >= 4, ignore_blank AND ignore_nonn
#	case 3: mult.py [files] --> argc > 1, ~ignore_blank AND ~ignore_nonn
if ( (argc >= 3) and (ignore_blank != ignore_nonn) ) \
or ( (argc >= 4) and (ignore_blank and ignore_nonn) ) \
or ( (argc > 1) and (not ignore_blank and not ignore_nonn) ):
	for line in fileinput.input():
		if fileinput.filename() == "--ignore-blank" or fileinput.filename() == "--ignore-non-numeric":
			continue
		# handle blank lines
		if line == '\n':
			if ignore_blank:
				continue
			product = mult(nums)
			del nums[:]
			print "Product is: ", product
			continue
			
		# handle non-numeric lines
		try:
			val = float(line)
		except ValueError:
			if ignore_nonn:
				continue
			sys.stderr.write("could not convert string to float: %s" %line)
			quit(1)
		nums.append(line)
	
# otherwise take input from stdin
else:
	for line in sys.stdin:
		# handle blank lines
		if line == '\n':
			if ignore_blank:
				continue
			product = mult(nums)
			del nums[:]
			print "Product is: ", product
			continue
			
		# handle non-numeric lines
		try:
			val = float(line)
		except ValueError:
			if ignore_nonn:
				continue
			sys.stderr.write("could not convert string to float: %s" %line)
			quit(1)
		nums.append(line)

# calculate and display product
product = mult(nums)
print "\nProduct is: ", product

# remove dummy files
os.remove('--ignore-non-numeric')
os.remove('--ignore-blank')