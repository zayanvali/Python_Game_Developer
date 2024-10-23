## Sets##
# Sets is a collection of well defined objects.
# All objects in a set are meant to be unique
# If duplicate values are defined in a set mistakenly then they get discarded
# Sets are represented using curly brackets

set1 = {1, 2, 3, 4, 3, 6, 4, 8}
print(set1)

list1 = [1, 3, 5, 7, 9, 3, 5]
print(list1)

set2 = set(list1)
print(set2)

if 5 in set2:
    print("\nYes it Exists!")
else:
    print("\nNo it does not exist!")

set3 = set([])
set3.add(24)
set3.add(66)
set3.add(-32)
set3.add(99)
set3.add(48)
print(set3)

# Deletion from set can be done using multiple options

# Remove operation
set3.remove(66)
print(set3)

# set3.remove(999)
# print(set3)

# Discard operation
set3.discard(999)
set3.add(96)
set3.discard(99)
print(set3)

# Sets have 4 major operations : Union, Intersection, Difference and Symmetric Difference

# Union
s1 = {1, 3, 5, 7, 9}
s2 = {2, 4, 6, 7, 8, 9, 10}

# Union is a combined operation of both the sets, and it brings all the items in a new set

union_result1 = s1.union(s2)
union_result2 = s2 | s1

print(union_result1, union_result2)

# Intersection gives us the common items of both the sets

intersection_result1 = s1.intersection(s2)
intersection_result2 = s2.intersection(s1)
print("\n")
print(intersection_result1, intersection_result2)

# Difference of sets

difference1 = s1.difference(s2)
difference2 = s2 - s1
print(difference1, difference2)

# Symmetric Difference - it is similar to union of both the sets, but here we will totally discard the common items
sym1 = s1.symmetric_difference(s2)
sym2 = s2 ^ s1
print(sym1, sym2)