person = {'name':'Rafiqul', 'age':22, 'location': 'Dhaka'}
print(person)
# key value pair
# object
# hashtable
# overlap with set
#{key:val, key:val, key:val}
print(person['age'])
print(person.keys())
print(person.values())
person['age'] = 100
print(person)
del person['location']
print(person)

# special dictionary looping
for key, val in person.items():
    print(key, val)