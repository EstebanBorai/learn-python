from code_magnets01 import sanitize
from os import chdir

chdir('/Users/esteban/Repos/learn-python/hfpython/chapter05')

def read_and_split(file):
	data = file.readline()
	return data.strip().split(',')

with open('james.txt') as james_file:
	james = read_and_split(james_file)

with open('julie.txt') as julie_file:
	julie = read_and_split(julie_file)

with open('mikey.txt') as mikey_file:
	mikey = read_and_split(mikey_file)

with open('sarah.txt') as sarah_file:
	sarah = read_and_split(sarah_file)

def apply_sanitize(_list):
	new_list = []
	for item in _list:
		new_list.append(sanitize(item))
	return new_list

james = apply_sanitize(james)
julie = apply_sanitize(julie)
mikey = apply_sanitize(mikey)
sarah = apply_sanitize(sarah)

print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))
