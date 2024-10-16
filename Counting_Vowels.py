statement = input("Enter a statement: ").lower()
vowels = {"a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" : 0}

for i in statement:
    if i in vowels:
        vowels[i] += 1

print(vowels) 