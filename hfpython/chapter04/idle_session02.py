import os

os.chdir('/Users/esteban/Repos/learn-python/hfpython/chapter04')

with open('man_data.txt') as mdf:
	print(mdf.readline())

