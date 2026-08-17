d = {'Name': 'Max Verstappen', 'Age': 28, 'Team': 'Red Bull Racing', 'Num' : 33}
print(d)

#printing values 
print("d[Name] :", d['Name'])
print("Team for which he races currently: ", d['Team'])

#updating dictionary
d['WDC'] = 4
print(d)

#deleting an element
del d['Age']
print(d)

#printing Keys and Values together and separately
print("\nItems: ", d.items())
print("Keys: ", d.keys())
print("Values: ", d.values())

print()
d1 = {'Name': 'Carlos Sainz', 'Age': 31, 'Team': 'Williams', 'Num' : 55}
print(d1)

#Comaparing to Dictionaries
print("Comparing to dictionaries: ", d == d1)

#iterating dictionary
for key, value in d1.items():
  print(key, ": ",value)
