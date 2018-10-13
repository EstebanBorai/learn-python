import os

os.chdir('/Users/esteban/Repos/learn-python/chapter03')
data = open('sketch.txt')

for line in data:
	(role, msg) = line.split(':', 1)
	print(role, end='')
	print(' said: ', end='')
	print(msg, end='')

data.close()
