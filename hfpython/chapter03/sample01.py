# lets prettend the file exists here
data = 'file'

for line in data:
	try:
		(role, msg) = line.split(':', 1)
		print(role, end='')
		print(' said: ', end='')
		print(msg, end='')
	except:
		pass

# data.close()
