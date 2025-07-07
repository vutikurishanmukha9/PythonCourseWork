## 1. Introduction to Dictionaries
# A dictionary is an ordered and mutable collection of key-value pairs.
# It is defined using curly braces {}.
# Keys must be unique and immutable (e.g., strings, numbers, tuples).
# Values can be of any data type.

# Syntax:
# dictionary_name = {key1: value1, key2: value2, key3: value3}

student = {"name": "Alice","age": 21,"course": "Computer Science"}

print(student) # Output: {'name': 'Alice', 'age': 21, 'course': 'Computer Science'}

# 2. Dictionary Operations
# 2.1 Accessing Values
# Accessing values using keys

print(student["name"])           # Output: Alice
print(student.get("age"))        # Output: 21

# Difference:
# student["key"] raises KeyError if key is missing
# student.get("key", default) returns default if key is missing

print(student.get("city", "Not Available"))  # Output: Not Available


# 2.2 Adding and Updating Items
# Updating an existing key
student["age"] = 22

# Adding a new key-value pair
student["city"] = "New York"

print(student) # Output: {'name': 'Alice', 'age': 22, 'course': 'Computer Science', 'city': 'New York'}

# 2.3 Removing Items

# Using pop() to remove a key and return its value
age = student.pop("age")
print(age)       # Output: 22

# Using del to delete a key-value pair
del student["course"]
print(student)

# Using popitem() to remove and return the last inserted item
student.popitem()
print(student)

# Using clear() to remove all items
student.clear()
print(student)   # Output: {}

# 3. Dictionary Methods
# 3.1 Methods for Accessing Data

d = {"name": "Alice", "age": 22, "course": "CS"}

print(d.get("name"))         # Output: Alice
print(d.keys())              # Output: dict_keys(['name', 'age', 'course'])
print(d.values())            # Output: dict_values(['Alice', 22, 'CS'])
print(d.items())             # Output: dict_items([('name', 'Alice'), ('age', 22), ('course', 'CS')])

# 3.2 Methods for Adding and Updating Data
# update() merges another dictionary into the current one
d.update({"city": "New York"})

# setdefault() returns value if key exists; otherwise adds the key with default value
print(d.setdefault("city", "Unknown"))   # Already exists → New York
print(d.setdefault("country", "USA"))    # Not exists → adds key with value "USA"
print(d)

# 3.3 Methods for Removing Data
# pop() removes a key and returns its value
d.pop("age")

# popitem() removes the last inserted item
d.popitem()

# clear() removes all items
d.clear()

# del removes a key
del d["name"]

# 4. Built-in Functions for Dictionaries
student = {"name": "Alice", "age": 22, "marks": 90}

# len() returns number of key-value pairs
print(len(student))       # Output: 3

# max() returns the maximum key
print(max({1: "a", 3: "b", 2: "c"}))   # Output: 3

# min() returns the minimum key
print(min({1: "a", 3: "b", 2: "c"}))   # Output: 1

# sorted() returns sorted list of keys
print(sorted({3: "x", 1: "z", 2: "y"}))  # Output: [1, 2, 3]

# 5. Nested Dictionaries
# Dictionary containing other dictionaries as values
students = {
    "Alice": {"age": 21, "course": "CS"},
    "Bob": {"age": 22, "course": "Math"}
}

print(students["Alice"]["course"])  # Output: CS







