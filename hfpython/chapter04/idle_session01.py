import os

os.chdir('/Users/esteban/Repos/learn-python/hfpython/chapter04')

try:
	with open('its.txt', 'w') as data:
		print('It\'s...', file=data)
except IOError as err:
	# File error: [Errno 2] No such file or directory: 'missing.txt'
	print('File error: ' + str(err))
# with statement takes advantage of Python technology
# called the context management protocol
