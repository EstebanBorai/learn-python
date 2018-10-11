movies = ['The Holy Grail', 1975, 'Terry Jones & terry Gilliam', 91,
	['Graham Chapman', ['Michael Palin', 'John Cleese',
		'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]

for item in movies:
	if isinstance(item, list):
		for nested in item:
			if isinstance(nested, list):
				for inner in nested:
					print(inner)
			else:
				print(nested)
	else:
		print(item)

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
