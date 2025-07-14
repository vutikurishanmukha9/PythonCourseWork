# Sets
# 1. Introduction to Sets
# ● A set is an unordered, mutable collection of unique elements.
# ● Sets automatically remove duplicate elements.
# ● Sets are similar to mathematical sets and support operations like union, intersection,and difference.
# ● They are useful for storing unique elements and performing fast membership tests.

# Creating a set with unique elements
my_set = {1, 2, 3, 4}
# Creating an empty set (use set() function, not {})
empty_set = set()
# Set with duplicate elements (duplicates are removed automatically)
set_with_duplicates = {1, 2, 2, 3, 4}
print(set_with_duplicates) # Output: {1, 2, 3, 4}

# 2. Set Properties
# ● Unordered: Sets do not maintain the insertion order.
# ● Unique Elements: Duplicate elements are not allowed.
# ● Mutable: Sets can be modified (elements can be added or removed).
# ● Immutable Elements Only: Elements must be hashable (mutable types like lists cannot be elements).

# This will raise a TypeError
# invalid_set = {[1, 2], 3} # Lists are mutable and cannot be added to a set

# 3. Operations on Sets
# Python provides several set operations that mimic mathematical set theory.
# a. Membership Testing
# ● Check if an element is present using the in or not in keywords.

my_set = {1, 2, 3, 4}
print(3 in my_set) # Output: True
print(5 not in my_set) # Output: True

# b. Union (| or union() method)
# ● Combines elements from two sets (removes duplicates).
# ● Syntax: set1 | set2 or set1.union(set2)


set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 | set2 # Output: {1, 2, 3, 4, 5}
print(result)

# c. Intersection (& or intersection() method)
# ● Returns common elements between two sets.
# ● Syntax: set1 & set2 or set1.intersection(set2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 & set2 # Output: {3}
print(result)

# d. Difference (- or difference() method)
# ● Returns elements in the first set but not in the second set.
# ● Syntax: set1 - set2 or set1.difference(set2)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 - set2 # Output: {1, 2}
print(result)

# Symmetric Difference (^ or symmetric_difference() method)
# ● Returns elements in either set1 or set2 but not both.
# ● Syntax: set1 ^ set2 or set1.symmetric_difference(set2)


set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1 ^ set2 # Output: {1, 2, 4, 5}
print(result)

# f. Subset (<= or issubset() method)
# ● Checks if all elements of one set are present in another.
# ● Syntax: set1 <= set2 or set1.issubset(set2)


set1 = {1, 2}
set2 = {1, 2, 3}
print(set1 <= set2) # Output: True

# g. Superset (>= or issuperset() method)
# ● Checks if one set contains all elements of another.
# ● Syntax: set1 >= set2 or set1.issuperset(set2)


set1 = {1, 2, 3}
set2 = {1, 2}
print(set1 >= set2) # Output: True

# h. Disjoint Sets (isdisjoint() method)
# ● Returns True if two sets have no common elements.

set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2)) # Output: True


# 4. Built-in Methods for Sets
# add(element) -- Adds an element to the set
# remove(element) -- Removes an element; raises an error if the element doesn’t exist
# discard(element) -- Removes an element; does not raise an error if the element doesn’t exist
# pop() -- Removes and returns an arbitrary element
# clear() -- Removes all elements from the set
# union(other_set) Returns the union of two sets
# intersection(other_set) -- Returns the intersection of two sets
# difference(other_set) -- Returns the difference between two sets
# symmetric_difference(other_set) -- Returns the symmetric difference between two sets
# update(other_set) Adds elements from another set to the current set
# intersection_update(other_set) -- pdates the set with the intersection of itself and another set
# difference_update(other_set) -- Updates the set by removing elements found in another set
# symmetric_difference_update(other_set) -- Updates the set with the symmetric difference
# copy() -- Returns a shallow copy of the set
# isdisjoint(other_set) -- Returns True if two sets have no elements in common
# issubset(other_set) -- Returns True if the set is a subset of another set
# issuperset(other_set) -- Returns True if the set is a superset of another set
s = {1, 2, 3}
s.add(4)     
print(s)   # {1, 2, 3, 4}
s.remove(2)  
print(s)   # {1, 3, 4}
s.discard(10) 
print(s)  # No error
item = s.pop() 
print(s) # Removes some item (random)
s.clear()    
print(s)   # Now s = set()

# 5. Built-in Functions for Sets

# len(set) -- Returns the number of elements in the set
# max(set) -- Returns the maximum element in the set
# min(set) -- Returns the minimum element in the set
# sum(set) -- Returns the sum of all elements in the set
# sorted(set) -- Returns a sorted list of the set elements
# set(iterable) -- Converts an iterable (e.g., list, string) to a set
s = {1, 2, 3}

print(len(s))     # 3
print(max(s))     # 3
print(min(s))     # 1
print(sum(s))     # 6
print(sorted(s))  # [1, 2, 3]

# Converting iterable to set
print(set("hello"))  # Output: {'h', 'e', 'l', 'o'}
