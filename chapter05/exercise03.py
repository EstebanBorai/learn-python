# Let's prettend
james = [2.01, 2.01, 2.22, 2.34, 2.34, 2.45, 3.01, 3.1, 3.21]

def remove_duplicated(_list):
	unique = []
	for item in _list:
		if not item in unique:
			unique.append(item)
	return unique

james_times = remove_duplicated(james)

# prints the best 3 times
print(james_times[0:3])
