import os
# First go to the right directory
os.chdir('/Users/esteban/Repos/learn-python/hfpython/chapter03')
data = open('sketch.txt')

for line in data:
	(role, said) = line.split(': ')
	print(role, end='')
	print(' said: ', end='')
	print(said, end='')
# This code will not run as some bugs of this algorithm
# will be solved in other files.
# Left for reference.
# The fixed version relies on "chapter03/idle_session03.py"
