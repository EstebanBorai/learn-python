import sys
import os

os.chdir('/Users/esteban/Repos/learn-python/hfpython/chapter04')
# I decided to rewrite the function

def print_lol(the_list, indent=False, level=0, destiny=sys.stdout):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, indent, level+1, destiny)
		else:
			if indent:
				for tab_stop in range(level):
					try:
						print('\t', end='', file=destiny)
					except IOError as error:
						print('Error while attempting to write the file:\n' + str(error))
						print('Maybe you forgot to use the "w" flag in order to open the file!')
				print(each_item, file=destiny)
