from os import chdir
from code_magnets01 import sanitize

chdir('/Users/esteban/Repos/learn-python/hfpython/chapter05')

def read_and_split(file):
	with open(file) as the_file:
		data = the_file.readline()
		return data.strip().split(',')

james = [float(sanitize(t)) for t in read_and_split('james.txt')]
print(sorted(james))

julie = [float(sanitize(t)) for t in read_and_split('julie.txt')]
print(sorted(julie))

mikey = [float(sanitize(t)) for t in read_and_split('mikey.txt')]
print(sorted(mikey))

sarah = [float(sanitize(t)) for t in read_and_split('sarah.txt')]
print(sorted(sarah))
