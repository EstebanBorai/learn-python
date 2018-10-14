from os import chdir

chdir('/Users/esteban/Repos/learn-python/chapter06')

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
		return data.strip().split(',')
	except IOError as ioerr:
		print('File Error! ' + str(ioerr))
		return None

sarah_data = get_coach_data('sarah2.txt')
sarah = {
	'FullName': sarah_data.pop(0),
	'Birthdate': sarah_data.pop(0),
	'Best Times': str(sorted(set([sanitize(t) for t in sarah_data]))[0:3])
}

print(sarah)
# {'FullName': 'Sarah Sweeney', 'Birthdate': '2002-6-17', 'Best Times': "['2.18', '2.21', '2.22']"}
