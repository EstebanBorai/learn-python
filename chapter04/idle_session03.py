import os
import pickle
from print_lol import print_lol as nester

os.chdir('/Users/esteban/Repos/learn-python/chapter04')

# Holds data to unpickle
new_man = []

try:
	with open('man_data.txt', 'rb') as man_file:
		new_man = pickle.load(man_file)
except IOError as err:
	print('File Error: ' + str(err))
except pickle.PickleError as prr:
	print('Pickle Error: ' + str(prr))

nester(new_man)
# If the file is modified or is not a list (its contents)
# nester will not print a thing in the console
# :_(
