### Lists ###
# List is another kind of datatype in python
# Lists are represented using square brackets
# Lists can contain different kinds of data like integers, strings, floats, dictionaries, tuples, boolean and lists as well
# Lists created within list are known as Nested-List
# Lists have the property of indexing and slicing
# Indexes give you the positional value of the items within the list
# Slicing extracts a portion of the list based on the indexes

x = [13, 11.26, "Test Value", True, [248, False, "another List", 9.76]]
print(x)

# Index concept in lists
# indexes are of two types : positive and negative index
# positive index are in the direction from left to right and start from 0, 1, 2...
# negative index start from right to left and they start from -1, -2, -3, ...

print(x[1])
print(x[4])
print(x[-3])
print(x[2][-5])

# Slicing means extracting a portion of the list
# Slicing needs a range of indexes where values would be extracted in between
# slicing eg : abc[1 : 6], here 1 is the starting index and 6 is the destination index
# For slicing we start counting from the starting index and will go upto 1 less than the destination index

x = [13, 11.26, "Test Value", True, [248, False, "another List", 9.76]]

print(x[1 : 4])
print(x[-4 : -1])
print(x[2 : ])
print(x[ : ])
print(x[4][2][5])
