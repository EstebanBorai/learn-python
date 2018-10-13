# open file in write mode
out = open('data.out', 'w')

# specify where to print with print BIF
print('Norwegian Blues stun easily.', file=out)

# close the file (flushing)
out.close()
