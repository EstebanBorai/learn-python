import os

os.chdir('/Users/esteban/Repos/learn-python/hfpython/chapter04')

man = 'Test Man Data'
other = 'Test Other Man Data'

try:
	with open('man_data.txt', 'w') as man_file:
		print(man, file=man_file)
	with open('other_data.txt', 'w') as other_data:
		print(other, file=other_data)
except IOError as error:
	print('File Error ' + str(error))
