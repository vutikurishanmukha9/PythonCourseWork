# Output Formatting

# Understanding the print() Function in Python

# Before diving into output formatting, it's important to understand the basics of the print() function,# which is used to
#  display information on the screen.

# What is print()?
# The print() function in Python outputs text, numbers, or any other data type to the  console. It's one of the first functions 
# every Python programmer learns.

# Basic Syntax:

# print(object, ..., sep=' ', end='\n', file=sys.stdout,flush=False)

# ● object: The data you want to display (can be text, numbers, variables, etc.).
# ● sep (optional): Defines the separator between multiple items.Default is a space(‘').
# ● end (optional): Specifies what to print at the end of the output. Default is a new line ('\n').
# ● file (optional): Where the output is sent. By default, it goes to the console.
# ● flush (optional): Forces the output to be written immediately.

# Basic Examples of print()

# a) Printing Text

print("Hello, World!") #Output: Hello, World!

# b) Printing Multiple Items
name = "Shanmukha"
age = 21
print("Name:", name, "Age:", age) #Output: Name: Shanmukha Age: 21

# c) Using sep to Change the Separator
print("2025", "07", "09", sep="-") #Output: 2025-07-09

# d) Using end to Control Line Endings
print("Hello,", end=" ")
print("World!") #Output: Hello, World!

# Printing Special Characters
# ● New Line (\n):

print("Shanmukha \nvutikuri") 

'''Output:Shanmukha 
vutikuri'''

# ● Tab (\t):

print("Name:\tShanmukh") # ● Output:Name:   Shanmukh

# Output Formatting
# 1️ Using Commas (Simple Print Method)
# This is the most basic way to print multiple items. When you separate items with commas in the print() function, Python adds 
# a space between them automatically.

name = "Shanmukh"
age = 21
score = 95.5
# Using Commas
print("Name:", name, "Age:", age, "Score:", score) #Output: Name: Shanmukh Age: 21 Score: 95.5

# Pros: Simple and easy for beginners.
# Cons: Limited control over formatting (like decimal places or alignment).

# 2️ Using Modulo Operator (% Formatting)
# This is an older method, similar to C-style formatting.
# You use % followed by format specifiers like %s (string), %d (integer), %f (float), etc.

name = "Shanmukha"
age = 21
score = 88.75
# Using Modulo Operator
print("Name: %s | Age: %d | Score: %.2f" % (name, age, score)) #Output: Name: Shanmukha | Age: 21 | Score: 88.75

# ● %s → String
# ● %d → Integer
# ● %.2f → Float with 2 decimal places

# Pros: Good control over formatting.
# Cons: Outdated; not recommended for new projects.

# 3️ Using f-strings (Formatted String Literals) — Python 3.6+
# This is the most modern and recommended method.
# Add an f before the string and use curly braces {} to insert variables directly.

name = "Shanmukha"
age = 21
score = 92.389
# Using f-strings
print(f"Name: {name} | Age: {age} | Score: {score:.2f}") # Output: Name: Shanmukha | Age: 21 | Score: 92.39

# {score:.2f} → Displays the score with 2 decimal places.

# Pros: Clean, concise, and easy to read.
# Cons: Only works in Python 3.6 and above.

# 4️ Using str.format() Method
# This method works in both Python 2 and 3.
# You use {} as placeholders and call .format() with the variables you want to insert.

name = "Shanmukha"
age = 22
score = 89.456
# Using str.format()
print("Name: {} | Age: {} | Score: {:.1f}".format(name, age,score)) # Output: Name: Shanmukha | Age: 22 | Score: 89.5

# ● {} → Placeholder for variables.
# ● {:.1f} → Formats the score with 1 decimal place.


# Pros: Flexible and supports complex formatting.
# Cons: Slightly more verbose compared to f-strings.



## Comparison Table: Output Formatting Methods in Python

# | Method              | Python Version | Pros                                | Cons                                   |
# |---------------------|----------------|-------------------------------------|----------------------------------------|
# | Commas in print()   | All Versions   | Simple, beginner-friendly           | Limited formatting options             |
# | Modulo Operator (%) | All Versions   | Good for basic formatting           | Outdated, less readable                |
# | f-Strings           | 3.6+           | Clean, fast, readable               | Not available in Python versions < 3.6 |
# | str.format()        | 2.7+, 3+       | Flexible, works in Python 2 and 3   | Slightly verbose                       |
