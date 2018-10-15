cleese = {} # using curly braces
palin = dict() # using factory function
print(type(cleese))
# <class 'dict'>
print(type(palin))
# <class 'dict'>

cleese['Name'] = 'John Cleese'
cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film producer']
palin = { 'Name': 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writter', 'tv'] }

print(palin['Name'])
# Michael Palin
print(cleese['Occupations'][-1])
# film producer

palin['Birthplace'] = 'Broomhill, Sheffield, England'
cleese['Birthplace'] = 'Weston-super-Mare, North Somerset, England'

print(palin)
# {'Name': 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writter', 'tv'], 'Birthplace': 'Broomhill, Sheffield, England'}
print(cleese)
# {'Name': 'John Cleese', 'Occupations': ['actor', 'comedian', 'writer', 'film producer'], 'Birthplace': 'Weston-super-Mare, North Somerset, England'}
