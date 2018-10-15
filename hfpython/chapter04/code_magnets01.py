import os
os.chdir('/Users/esteban/Repos/learn-python/hfpython/chapter04')

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
print(man)
print(other)
