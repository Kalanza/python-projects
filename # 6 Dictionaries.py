#An example of a dictionary
person = {'name': 'Kalanza','age' : 25 ,'gender' : 'Male'}
print(person['name'])
person['newkey'] = 67#this is how you add a newkey in a dictionary
print(person)

#Items - returns a tuple of a list of items in the dictionary
#person.items()
#Keys - it returns a list of all the keys in the dictionary
#person.keys()
#Values - it returns all the respective  values in the dictionary
#person.values()
person = {'name': 'Kalanza','age' : 25 ,'gender' : 'Male'}
print(person['name'])
person['newkey'] = 67#this is how you add a newkey in a dictionary
print(person.items())
# it returns - dict_items([('name', 'Kalanza'), ('age', 25), ('gender', 'Male'), ('newkey', 67)])
print(person.keys())
# it returns - dict_keys(['name', 'age', 'gender', 'newkey'])
print(person.values())
# it returns dict_values(['Kalanza', 25, 'Male', 67])
