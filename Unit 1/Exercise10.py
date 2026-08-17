def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n - 1)  #calling the function again until we get our ans

num = int(input("Enter num: "))
result = factorial(num)

print(f"Factorial of {num}: ", result)
