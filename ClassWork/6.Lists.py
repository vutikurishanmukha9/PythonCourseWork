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