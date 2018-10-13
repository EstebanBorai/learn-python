import os
os.chdir('/Users/esteban/Repos/learn-python/chapter04')

man = []
other = []
try:
	data = open('sketch.txt')
	for line in data:
		try:
			(role, msg) = line.split(':', 1)
			msg = msg.strip()
			if role == 'Man':
				man.append(msg)
			elif role == 'Other Man':
				other.append(msg)
		except ValueError:
			pass
	data.close()
except IOError:
	print('The datafile is missing!')

try:
	man_data = open('man_data.txt', 'w')
	other_data = open('other_data.txt', 'w')
	print(man, file=man_data)
	print(other, file=other_data)
except IOError as err:
	print('Something with the files went wrong!' + str(err))
finally:
	# either try/except occurs, finally will run
	# ensure closing the file
	man_data.close()
	other_data.close()
	
