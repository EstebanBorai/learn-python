from code_magnets01 import sanitize

mins = [1, 2, 3]
secs = [m * 60 for m in mins]
print(secs)
# [60, 120, 180]

meters = [1, 10, 3]
feet = [m * 3.281 for m in meters]
print(feet)
# [3.281, 32.81, 9.843]

lower = ['I', 'don\'t', 'like', 'spam']
upper = [s.upper() for s in lower]
print(upper)
# ['I', "DON'T", 'LIKE', 'SPAM']

dirty = ['2-22', '2:22', '2.22']
clean = [sanitize(t) for t in dirty]
print(clean)
# ['2.22', '2.22', '2.22']

clean = [float(sanitize(t)) for t in ['2-22', '3:33', '4.44']]
print(clean)
# [2.22, 3.33, 4.44]
