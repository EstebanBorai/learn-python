from os import chdir

chdir('/Users/esteban/Repos/learn-python/hfpython/chapter06')

def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(mins, secs) = time_string.split(splitter)
	return mins + '.' + secs

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
			data = data.strip().split(',')
	except IOError as ioerr:
		print('File Error! ' + str(ioerr))
	dic = {
		'Name': data.pop(0),
		'Birthdate': data.pop(0),
		'Best Times': str(sorted(set([sanitize(t) for t in data]))[0:3])
	}
	return dic

sarah = get_coach_data('sarah2.txt')
print(sarah)

james = get_coach_data('james2.txt')
print(james)

julie = get_coach_data('julie2.txt')
print(julie)

mikey = get_coach_data('mikey2.txt')
print(mikey)
