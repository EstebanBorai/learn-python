import os
import pickle

os.chdir('/Users/esteban/Repos/learn-python/hfpython/chapter04')

# Warning The pickle module is not secure against erroneous
#  or maliciously constructed data. Never unpickle data received
#  from an untrusted or unauthenticated source.

man = ['Man file data']
other = ['Other Man data']

try:
	with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
		pickle.dump(man, man_file)
		pickle.dump(other, other_file)
except IOError as error:
	print('File Error!:' + str(error))
except pickle.PickleError as error:
	print('Error!:' + str(error))
