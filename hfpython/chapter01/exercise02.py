movies = ['The Holy Grail', 1975, 'Terry Jones & terry Gilliam', 91,
	['Graham Chapman', ['Michael Palin', 'John Cleese',
		'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
print(movies)

def print_list(list_):
	for item in list_:
		if isinstance(item, list):
			print_list(item)
		else:
			print(item)

print_list(movies)

# The Holy Grail
# 1975
# Terry Jones & terry Gilliam
# 91
# Graham Chapman
# Michael Palin
# John Cleese
# Terry Gilliam
# Eric Idle
# Terry Jones
