#tuple and set operations
t= (45, 89, 63, 87, 12, 35, 28)
t1 = ('Max', 'Carlos', 'Leclerc')
print("\nFirst element of tuple t: ", t[0])
print("\nLast three elements if tuple t: ", t[-3:])
print("\nLength of tuple: ", len(t))
print("\nAdding to tuples :" , t+t1)
print("\nIterating tuple elements:")
for rd in t1: print(rd, end = "\n ")
print()
s = {12, 35, 31, 15, 37, 28}
s.add(33)
print("\nAdding an element: ", s)
s.remove(12)
print("\nSet s after removing element 12:", s)

s1 = {78, 89, 65, 32, 45, 75}
s2 = {75, 98 ,56 ,23 ,45 ,12}

print("\nUnion of s1 and s2: ", s1.union(s2))
print("\nIntersection of s1 and s2: ", s1.intersection(s2))
print("\nDifference of s1 and s2: ", s1.difference(s2))



