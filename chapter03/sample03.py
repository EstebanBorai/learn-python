import os

try:
	data = open('sketch.txt')

	for line in data:
		try:
			if not line.find(':') == -1:
				(role, msg) = line.split(':', 1)
				print(role, end='')
				print(' said: ', end='')
				print(line, end='')
		except ValueError:
			pass
except IOError:
	print('The data file is missing!')
