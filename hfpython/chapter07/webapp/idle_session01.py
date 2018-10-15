import os
from athletemodel import get_coach_data, get_from_store, put_to_store

os.chdir('/Users/esteban/Repos/learn-python/hfpython/chapter07/webapp')

the_files = ['data/sarah.txt', 'data/james.txt', 'data/mikey.txt', 'data/julie.txt']

data = put_to_store(the_files)
print(data)
# {'Sarah Sweeney': {'Name': 'Sarah Sweeney', 'Birthdate': '2002-6-17', 'Best Times': "['2.18', '2.21', '2.22']"}, 
# 	'James Lee': {'Name': 'James Lee', 'Birthdate': '2002-3-14', 'Best Times': "['2.01', '2.16', '2.22']"}, 
# 	'Mikey McManus': {'Name': 'Mikey McManus', 'Birthdate': '2002-2-24', 'Best Times': "['2.22', '2.31', '2.38']"}, 
# 	'Julie Jones': {'Name': 'Julie Jones', 'Birthdate': '2002-8-17', 'Best Times': "['2.11', '2.23', '2.59']"}
# 	}

for each in data:
	print(data[each]['Name'] + ' ' + data[each]['Birthdate'])
# Sarah Sweeney 2002-6-17
# James Lee 2002-3-14
# Mikey McManus 2002-2-24
# Julie Jones 2002-8-17

data_copy = get_from_store()

for athlete in data_copy:
	print(data_copy[athlete]['Name'] + ' ' + data_copy[athlete]['Birthdate'])
# Sarah Sweeney 2002-6-17
# James Lee 2002-3-14
# Mikey McManus 2002-2-24
# Julie Jones 2002-8-17
