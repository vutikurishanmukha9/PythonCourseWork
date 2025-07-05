# 1. Basic Features of Lists
# ● Ordered: Lists maintain the order of elements.
# ● Mutable: Elements can be modified after creation.
# ● Indexed: Elements can be accessed using an index (starting from 0).
# ● Allow Duplicates: Lists can contain duplicate values.
# ● Heterogeneous: Lists can contain different data types (e.g., int, str, float, etc.).
# ● Dynamic: Size is not fixed; elements can be added or removed dynamically.

#2.1 Empty List

my_list = [] # Empty list
my_list2 = list() # Using list() constructor
print("Printing the Empty list:",my_list)
print("Printing the list using the constructor:",my_list2)

# 2.2 List with Elements

l = [0,1,2,3,4,5,6,] #Instialzing the list with the integers
print("Printing the list:",l) #Printing the list: [0, 1, 2, 3, 4, 5, 6]

fruits = ["apple", "banana", "cherry"] # List of strings
print("Printing the list of the strings:",fruits)

mixed = [10, "Python", 3.14, True] # Mixed data types
print("Printing the list of the mixed data types:",mixed)

# 2.3 List with Nested Lists

nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print("Printing the list with nested list:",nested_list)

# 2.4 List using list() Constructor

list_from_tuple = list((1, 2, 3)) # Converting tuple to list
print("coverting tuple to list:",list_from_tuple)

string_to_list = list("Python") # ['P', 'y', 't', 'h', 'o','n']
print("converting the string to list:",string_to_list) #converting the string to list

#3. Accessing Elements in a List

# 3.1 Using Indexing (Positive & Negative)

my_list = ["Python", "Java", "C++"]
print(my_list[0]) # Python
print(my_list[1]) # Java
print(my_list[-1]) # C++ (Negative Indexing)

# 3.2 Using Slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4]) # [20, 30, 40]
print(numbers[:3]) # [10, 20, 30] (from start)
print(numbers[2:]) # [30, 40, 50] (to end)
print(numbers[-3:-1]) # [30, 40]
print(numbers[::-1]) # [50, 40, 30, 20, 10] (Reverse list)

# 4. Modifying Lists

# 4.1 Changing Elements

numbers = [10, 20, 30, 40]
numbers[2] = 100 
print(numbers) # [10, 20, 100, 40]

# 4.2 Adding Elements

# Append (adds to the end)
numbers.append(50)

# Insert (adds at a specific position)
numbers.insert(1, 15)

# Extend (adds multiple elements)
numbers.extend([60, 70, 80])

print(numbers) # [10, 15, 20, 100, 40, 50, 60, 70, 80]

# 4.3 Removing Elements

numbers.remove(100) # Removes first occurrence of 100
numbers.pop(2) # Removes element at index 2
numbers.pop() # Removes last element
del numbers[1] # Deletes element at index 1
numbers.clear() # Clears the entire list

# 5. List Methods

numbers = [3, 1, 4, 1, 5, 9]
print(numbers.count(1)) # 2 #Counting how many times does the 1 is present in the list
print(numbers.index(4)) # 2
numbers.sort()
print(numbers) # [1, 1, 3, 4, 5, 9]
numbers.reverse()
print(numbers) # [9, 5, 4, 3, 1, 1]