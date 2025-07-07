# *Dictionary*
# A dictionary in Python is an ordered, mutable collection that stores key-value pairs.
# Unlike lists or tuples, which are indexed by position, dictionaries are indexed by unique keys.

# 1. Introduction to Dictionary
# A dictionary is defined using curly braces {}, where each key is followed by a colon :, and the key-value pairs are separated by commas.
# -------------------------------
# 🧠 PYTHON DICTIONARY - COMPLETE NOTES WITH EXPLANATIONS
# -------------------------------

# 🔹 1. Introduction to Dictionary
# Dictionaries are used to store data in key-value pairs. Very useful when data is logically mapped (like a student's details).
# Keys are unique and immutable (e.g., strings, numbers, tuples).
# Values can be any type – int, list, dict, etc.

# ✅ Syntax:
# dictionary_name = {key1: value1, key2: value2, key3: value3}

# ✅ Example:
student = {
    "name": "Alice",
    "age": 21,
    "course": "Computer Science"
}
print(student)  # Displays the full dictionary

# -------------------------------
# 🔹 2. Dictionary Operations
# -------------------------------

# 📌 2.1 Accessing Values
# Why? To retrieve values by their associated keys.

print(student["name"])           # Direct access → Output: Alice
print(student.get("age"))        # Safer access using get() → Output: 21

# Why use get()?
# get() avoids KeyError if key doesn't exist. Use when you're unsure if key is present.

print(student.get("city", "Not Available"))  # Provides a default value if key not found

# 📌 2.2 Adding and Updating Items
# Why? Dictionaries are mutable — can add or update any time.

student["age"] = 22             # Updates existing value
student["city"] = "New York"    # Adds new key-value pair
print(student)

# Output:
# {'name': 'Alice', 'age': 22, 'course': 'Computer Science', 'city': 'New York'}

# 📌 2.3 Removing Items

# 👉 Using pop(key)
# Why? Removes a specific key and also gives its value back.
age = student.pop("age")
print(age)      # Output: 22
print(student)  # 'age' key removed

# 👉 Using del
# Why? Deletes a key-value pair permanently. Use when value is not needed.
del student["course"]
print(student)

# 👉 Using popitem()
# Why? Removes the most recently added key-value pair. Useful in LIFO scenarios.
student.popitem()
print(student)

# 👉 Using clear()
# Why? Completely clears all data from the dictionary.
student.clear()
print(student)  # Output: {}

# -------------------------------
# 🔹 3. Dictionary Built-in Methods
# -------------------------------

# Let's reset the dictionary
student = {
    "name": "Alice",
    "age": 21,
    "course": "CS"
}

# 📌 3.1 Accessing Data
# Why? To retrieve structure or contents of the dictionary.

print(student.get("name"))       # Safe way to fetch value
print(student.keys())            # Returns all keys → use in loops or to check for existence
print(student.values())          # Returns all values → for stats, checks, etc.
print(student.items())           # Returns all key-value pairs → useful for iteration

# 📌 3.2 Adding and Updating Data

# 👉 Using update()
# Why? Merges another dictionary into this one. Cleaner than multiple assignments.
student.update({"city": "New York"})
print(student)

# 👉 Using setdefault()
# Why? Returns value if key exists, else inserts key with default. Useful for default initialization.
student.setdefault("email", "alice@example.com")
print(student)

# 📌 3.3 Removing Data (again, summarized)

student.pop("age")               # Removes 'age'
student.popitem()                # Removes last inserted item
student.clear()                  # Empties the dictionary

# -------------------------------
# 🔹 4. Built-in Functions for Dictionaries
# -------------------------------

# Why? These help analyze or process the dictionary contents.

sample_dict = {1: "a", 3: "b", 2: "c"}

print(len(sample_dict))          # Number of key-value pairs → Output: 3
print(max(sample_dict))          # Max key (works if keys are comparable) → Output: 3
print(min(sample_dict))          # Min key → Output: 1
print(sorted(sample_dict))       # Sorted list of keys → Output: [1, 2, 3]

# -------------------------------
# 🔹 5. Nested Dictionaries
# -------------------------------
# Why? Helps in representing complex data (e.g., records of multiple users)

students = {
    "Alice": {"age": 21, "course": "CS"},
    "Bob": {"age": 22, "course": "Math"}
}

print(students["Alice"]["course"])  # Accessing inner dict → Output: CS

# -------------------------------
# 🔹 6. Dictionary Comprehension
# -------------------------------
# Why? Creates dictionary in a single line with logic.

squares = {x: x*x for x in range(1, 6)}  # Dictionary of squares
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# -------------------------------
# ✅ END OF NOTES
# -------------------------------
