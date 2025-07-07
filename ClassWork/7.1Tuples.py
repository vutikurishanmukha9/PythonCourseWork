# 1. Introduction to Tuples
# ● A tuple is an immutable, ordered collection of elements.
# ● Tuples are similar to lists, but once a tuple is created, its contents cannot be changed.
# ● Tuples can store any type of data (int, float, string, list, etc.).
# ● Tuples are faster than lists because they are immutable.

t = () #Decalring the tuple
t = tuple() #Declaring the tuple using the constructor
t = (1,2.3,4+3j,'string',[1,2,3,4,5,6],(1,2,3,4,5,6),True, {1,2,3,4,5,6},{'name': 'xyz'}) #storing the elememts in the tuple\
print(t)   #Output: (1, 2.3, (4+3j), 'string', [1, 2, 3, 4, 5, 6], (1, 2, 3, 4, 5, 6), True, {1, 2, 3, 4, 5, 6}, {'name': 'xyz'})

# 2. Accessing Tuple Elements

# a. Indexing
# ● Access elements using zero-based indexing.
# ● Syntax: tuple[index]

t = (1,2,3,4,5)
print("the Tuple:",t)   #Output the Tuple: (1, 2, 3, 4, 5)
print(t[0]) #Indexing output is 1

# b. Negative Indexing
# ● Access elements from the end of the tuple using negative indices.

t = (10,20,30,40,50,60)
print(t[-1]) #Output 60
print("reverse of the Tuple:",t[::-1]) #reverse of the Tuple (60, 50, 40, 30, 20, 10)

# c. Slicing
# ● Extract a portion of the tuple using slicing ([start:end:step]).
# ● Syntax: tuple[start:end]

t = (10,20,30,40,50)
print(t[1:3:1]) #Output (20, 30)

# 3. Operations on Tuples
# a. Concatenation
# ● Combine two or more tuples using the + operator.

t1 = (10,20,30,40,50)
t2 = (60,70,80,90,100)
print("The Concatenated tuple is:",t1 + t2) #The Concatenated tuple is: (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# b. Repetition
# ● Repeat the elements of a tuple using the * operator.

t1 = (1,2,3,4,5)
print("The Repeated string is:",t1*3) #The Repeated string is: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# C.Membership Testing
# ● Check if an element is present in the tuple using the in or not in keywords.

RCB = ('kohli','Bhuvi','Rajat','salt')
print("The output is:",'Maxi' in RCB)   #The output is: False
print("The Output is:",'salt' in RCB)  #The Output is: True

# d. Tuple Unpacking
# ● Assign tuple elements to multiple variables.

IPL = ('Viart Kohli','Rohit sharma','MS Dhoni','shreyas iyer') #packing of the items
rcb,MI,CSK,PK = IPL #unpacking of the items
print(rcb,MI,CSK,PK) ##unpacking of the items

# 4. Tuple Methods
# count(x) -- Counts the number of occurrences of x in the tuple

t = (1,1,2,3,2,4,5,6,7,8,9,4,2,3,5,1,2,4,5,2,5,2,5,5,7,8,9,4,1,2,2)
print("The number of times the value occured is:",t.count(1)) #The number of times the value occured is: 4

# index(x) --Returns the first index of x in the tuple
print("The index of the element of the value is :",t.index(9)) #The index of the element of the value is : 10

# 5. Built-in Functions for Tuples
# len(tuple) ---Returns the length (number of elements) of the tuple

t = (1,2,3,4,5,6,7,8,9,1,2,3,6,5,4,7,8,9,6,3,2,5,8,7,4,1)
print("The length of the tuple is:",len(t)) #The length of the tuple is: 26

# max(tuple) Returns the maximum element in the tuple (for comparable types)
print("The biggest element in the tuple is:",max(t)) #The biggest element in the tuple is: 9

# min(tuple) -- Returns the minimum element in the tuple
print("The samllest element in the tuple is the:",min(t)) #The samllest element in the tuple is the: 1

# sum(tuple) -- Returns the sum of elements (if all are numbers)
print("The total sum of the tuple is:",sum(t)) #The total sum of the tuple is: 126

# tuple(iterable) -- Converts an iterable (like a list or string) to a tuple
print("Coverting of the tuple into into list:",list(t))  #Coverting of the tuple into into list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 6, 5, 4, 7, 8, 9, 6, 3, 2, 5, 8, 7, 4, 1]
