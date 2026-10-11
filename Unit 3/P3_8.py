import re

s = input("Enter a statement: ")

pattern = r"\d+"

if re.fullmatch(pattern, s):
    print("Statement contains only digits.")
else:
    print("Statement does not contain only digits.")
