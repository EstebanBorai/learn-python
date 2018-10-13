import os

# if os.path.exists('sketch.txt'):
try:
	data = open('sketch.txt')

	for line in data:
		if not line.find(':') == -1:
			(role, msg) = line.split(':', 1)
			print(role, end='')
			print(' said: ', end='')
			print(line, end='')
	data.close()
# else:
except:
	print('The data file is missing!')
