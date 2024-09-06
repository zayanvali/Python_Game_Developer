### Dictionaries ##
# Dictionaries is a kind of data type in python just like integers, strings and floats
# Dictionaries are represented using curly or second brackets, where the items are stored as key:value pair
# All keys in the dictionary are supposed to be unique
# Multiple values in dictionary can be same
# Values in a dictionary can be accessed only through the keys



sample = {"Name" : "Zayan", "Age" : 12, "Country" : "UK", "Count" : 12, "Name" : "Zayan Vali"}

print(sample)

# Adding items in dictionary
sample["Profession"] = "Student"
print("\n") # \n is used to create a line gap in the output statement
print(sample)

# Accessing all keys
print(sample.keys())

# Accessing all values
print(sample.values())

# Accessing all items
print(sample.items())