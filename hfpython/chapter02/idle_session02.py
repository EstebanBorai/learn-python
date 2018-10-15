from exercise03 import print_lol

names = ['John', 'Eric', ['Cleese', 'Idle'], 'Michael', ['Palin']]
print_lol(names)

# John
# Eric
# Cleese
# Idle
# Michael
# Palin

# print_lol(names, True) cannot be tested
# the original function uses a second argument to
# apply indentation by default
# my version uses indentation only when defined

names = ['John', 'Eric', ['Cleese', 'Idle'], 'Michael', ['Palin']]
print_lol(names, 4)
                                # John
                                # Eric
                                #         Cleese
                                #         Idle
                                # Michael
                                #         Palin
