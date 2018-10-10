cast = ["Cleese", 'Palin', 'Jones', "Idle"]
print(cast)
# ['Cleese', 'Palin', 'Jones', 'Idle']

print(len(cast))
# 4

print(cast[1])
# Palin

cast.append("Gilliam")
print(cast)
# ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']

print(cast.pop())
# Gilliam

cast.extend(["Gilliam", "Chapman"])
print(cast)
# ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam', 'Chapman']

cast.remove("Chapman")
print(cast)
# ['Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']

cast.insert(0, "Chapman")
print(cast)
# ['Chapman', 'Cleese', 'Palin', 'Jones', 'Idle', 'Gilliam']
