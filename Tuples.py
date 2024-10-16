# Tuples
# Tuples are another kind of data type in python
# Tuples are represented using round brackets
# Tuples are immutable, once a tuple is created we cannot add, modify, alter, delete any item
# Tuples follow the concept of indexing and slicing
# Tuples within a tuple are known as nested tuples


tup1 = 13, 93.19, "Zayan", "UK", "Central London"
print(tup1, type(tup1))
# When no brackets are there for multiple values of a variable, round bracket is by default applicable

# Unpacking concept
# Through unpacking we can decongest multiple values of a tuple into individual variable items
Age, Score, Name, Country, Region = tup1

print("Your name is : ", Name)
print("Your age is : ", Age)
print("You scored : ", Score)
print("You reside in : ", Country)

tup2 = 13, 93.19, "Central London", True, ["Hello World", 666, 13.48, False], (369, 741.864, "Test Value", True)
print(tup2)
print(tup2[2][9 : 12]) # ond
print(tup2[4][1])
print(tup2[5][2][7 : 10])