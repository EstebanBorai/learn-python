import pickle
import os

os.chdir('/Users/esteban/Repos/learn-python/hfpython/chapter04')

with open('sample02', 'wb') as savedata:
	pickle.dump([1, 2, 'three'], savedata)

with open('sample02', 'rb') as restoredata:
	a_list = pickle.load(restoredata)

print(a_list)
