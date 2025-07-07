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

