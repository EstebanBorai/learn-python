from os import chdir

chdir('/Users/esteban/Repos/learn-python/hfpython/chapter05')

def split_and_log(file):
	log = (file.readline()).strip().split(',')
	print(log)

with open('james.txt') as james, open('julie.txt') as julie, open('mikey.txt') as mikey, open('sarah.txt') as sarah:
	split_and_log(james)
	split_and_log(julie)
	split_and_log(mikey)
	split_and_log(sarah)
