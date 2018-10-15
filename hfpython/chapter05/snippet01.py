from os import chdir

chdir('/Users/esteban/Repos/learn-python/hfpython/chapter05')

def find_best(times_file):
	times = times_file.readline()
	splitted = str(times).split(',')
	best = 0
	for time in splitted:
		time = float(time)
		if time > best:
			best = time
	print(best)

with open('james.txt') as james, open('julie.txt') as julie, open('mikey.txt') as mikey, open('sarah.txt') as sarah:
	find_best(james)
	find_best(julie)
	find_best(mikey)
	find_best(sarah)
