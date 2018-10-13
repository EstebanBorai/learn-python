import os
path = os.getcwd()
print(path)
# /learn-python
correct = os.chdir('/Users/esteban/Repos/learn-python/chapter03')
print(os.getcwd())
# /learn-python/chapter03

data = open('./sketch.txt')
print(data.readline(), end='')
# Man: Is this the right room for an argument? Other Man: I’ve told you once.

print(data.seek(0))
# 0
for line in data:
	print(line, end='')
# Man: Is this the right room for an argument? Other Man: I’ve told you once.
# Man: No you haven’t!
# Other Man: Yes I have.
# Man: When?
# Other Man: Just now. Man: No you didn’t!
data.close()
