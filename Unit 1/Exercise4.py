#String Operations

strg = input("Enter a word of choice: ")

#String Slicing, index starts from 0 to len+1 
print(strg[:], ", Printing the whole string w/o slicing")
print(strg[:3], ", Printing first 3 words")
print(strg[::-1], ", Printing in backwards")
print(strg[-4:], ", Printing last 4 words\n")
print()
#String Formatting
strig = input("Enter a word/s for formatting function: ") #calling function
print(f"I am using string {strig} functions.")
print()
#String Functions
print(strig.lower()) 
print(strig.upper()) 
print(strig.capitalize()) 
print(strig.title()) 
print("   Command  ".strip())
print("Canning".replace('a', 'u'))
print(strig.find('t'))
print(strig.count('a'))
print(strig.split())
print("_".join(["Python", "Unit", "1"]))
print(strig.startswith(""))
print(strig.endswith(""))
print(strig.isalpha())
print(strig.isdigit())
print(len(strig))

      






