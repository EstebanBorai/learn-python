import os
os.chdir('/Users/esteban/Repos/learn-python/chapter03')

data = open('sketch.txt')
for line in data:
	if (line.find(':') != -1):
		(role, msg) = line.split(':', 1)
		print(role, end='')
		print(' said: ', end='')
		print(line, end='')

data.close()
