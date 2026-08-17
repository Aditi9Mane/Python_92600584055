Fable = []

for i in range(1, 6):
    v = input("Enter values to be appended in the list: ")
    Fable.append(v)

print(Fable)

print("Fable[0:3]- ", Fable[0:3])
print("Fable[1]- ", Fable[1])
print("Fable[::-1]- ", Fable[::-1])

NFable = [i**2 for i in range(25, 31)]
print(NFable)

