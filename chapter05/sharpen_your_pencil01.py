from os import chdir

chdir('/Users/esteban/Repos/learn-python/chapter05')

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

print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))
