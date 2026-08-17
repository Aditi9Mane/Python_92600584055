#Mutable and Immutable Objects
"""Mutables are those which can be changed after being created,
While immutables can't be changed after creation."""

#List is an mutable object
m = [ ]
for i in range(40, 1,  -3):
    m.append(i) #adding elements after creating a empty list 

print(m)

m1 = ["Carlos", "Max", "Oscar", "Charles", "Lando"]
print("\nUpdating values in list m from list m1")
m[0] = m1[-1]
print(m)
print()
#Tuple does'nt have append method
i =tuple(range(40, 1, -2)) # creating tuple
print(i)
#i[0] = "Max"
#print(i) this throws an error bc once created tuples can't be assigned new item


