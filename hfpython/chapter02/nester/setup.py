# python3 setup.py sdist
# python3 setup.py install

from distutils.core import setup

setup(
	name = 'nester',
	version = '1.0.0',
	py_modules = ['nester'],
	author = 'Esteban Borai',
	author_email = 'estebanborai@outlook.com',
	url = 'https://github.com/gitpullsh/learn-python',
	description = 'A simple function that takes a list and print items inside the list recursively'
)
