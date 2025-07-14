#4.PythonOperators

#Arithmetic Operators
a = 20
b = 10
c = 30

print("a:", a)  # Output: 20
print("b:", b)  # Output: 10
print("c:", c)  # Output 30
print("Addition(+) of a,b:",a+b) #30 //Addition
print("Subtraction(-) of a,b:",a-b) #10 //Subtraction
print("Multiplication(*) of a,b:",a*b) #200 //Multiplication
print("Floor Division(//) of a,b:",a//b) #2 //Floor divison to get the output in Integer
print("Divison(/) of a,b:",a/b) #2.0 //Division to print the remainder 
print("Modulos Divison(%) of a,b:",a%b) #0 //Modulos Divison to print remainder
print("Exponentional(**)of a,b:",a**b) #10240000000000 //Raises the first number to the power of the second


# Comparison Operators

print("a:", a)  # Output: 20
print("b:", b)  # Output: 10
print("Equals to (==):", a == b)               # False
print("Not Equals to (!=):", a != b)           # True
print("Greater than (>):", a > b)              # True
print("Greater than or Equal to (>=):", a >= b)  # True
print("Less than (<):", a < b)                 # False
print("Less than or Equal to (<=):", a <= b)   # False

#Assignment Operators

print("Assiging a value to a:", a)  #a is assigned to 20
a += b
print("Add & Assign to a:",a)  # a is Added & Assigned to b
a -= b
print("Subtract & Assign to a:",a) #a Subtracted & Assigned to b
a *= b
print("Multiply & Assign to a:",a) #a is Multipled & Assigned to a b
a /= b
print("Divide & Assign to a:",a) #b is Divided & Assigned to a
a //= b
print("Floor Divide & Assign to a:",a) #b is Floor Divison & Assigned to a
a %= b
print("Modulus & Assign to a:",a) # b is Modulus & Assign to a
a **= b
print("Exponentiate & Assign to a:",a) #b is Exponentiate & Assign to a

# Logical Operators

print("AND logic for a,b,c:",2000 > a and 2000 > b and 2000 > c) #Returns True if both conditions are true
print("OR Logic for a,b,c:", 1000 > a or 1000 > b or 1000 > c) #Returns True if at least one condition is true
print("NOT logic for b,c:", not(b > c)) #Reverses the condition (True becomes False)

#Membership Operators

fruits = ["apple", "banana", "cherry"]
print("in operators check if a value exists within a sequence:", "apple" in fruits) # Returns True if the value exists in the sequence
print("not in operators check if a value exists within a sequence:","grape" not in fruits) # Returns True if the value does NOT exist in the sequence

numbers = [10, 20, 30, 40, 50]
print(20 in numbers)       # True → 20 is present in the list
print(100 not in numbers)  # True → 100 is not in the list

message = "Hello, world!"
print("Hello" in message)     # True → "Hello" is a substring
print("bye" not in message)   # True → "bye" is not in the string

vowels = {'a', 'e', 'i', 'o', 'u'}
print('e' in vowels)        # True → 'e' is a member of the set
print('z' not in vowels)    # True → 'z' is not in the set

student = {"name": "Shanmukha", "age": 21,"course": "Data Analytics"}
print("name" in student)        # True → "name" is a key in the dictionary
print("marks" not in student)   # True → "marks" is not a key

matrix = [[1, 2], [3, 4], [5, 6]]
print([3, 4] in matrix)         # True → the sublist [3, 4] exists in matrix
print([7, 8] not in matrix)     # True → [7, 8] is not in matrix


# Identity Operators Example

X = [1, 2, 3, 4, 5]
Y = [6, 7, 8, 9, 10]
Z = X  # Z now refers to the same object in memory as X
print(X)  # Output: [1, 2, 3, 4, 5]
print(Y)  # Output: [6, 7, 8, 9, 10]
print(Z)  # Output: [1, 2, 3, 4, 5], same as X

# Check if X and Z refer to the same object (True because Z = X)
print(X is Z)  # Output: True

# Check if Y and Z refer to the same object (False because Y is a different list)
print(Y is Z)  # Output: False
print(id(X))  # Same as id(Z), because X and Z refer to the same object
print(id(Y))  # Different ID, because Y is a different object
print(id(Z))  # Same as id(X)


#Bitwise operator
# 1-0001
# 2-0010
# 3-0011
# 4-0100
# 5-0101
# 6-0110
# 7-0111
# 8-1000
# 9-1001
# 10-1010

x = 5 # Binary: 0101
y = 3 # Binary: 0011
print("AND Operation for the x and y is :",x & y) # Output: 1 (Binary: 0001 → AND operation)
print("OR Operation for the x and y is :",x | y) # Output: 7 (Binary: 0111 → OR operation)
print("XOR Operation for the x and y is :",x ^ y) # Output: 6 (Binary: 0110 → XOR operation)
print("NOT Operation for the x and y is :",~x) # Output: -6 (Binary: Inverts bits of 5)
print("LEFT SHIFT Operation for the x and y is :",x << 1) # Output: 10 (Binary: 1010 → Shifts left by 1)
print("RIGHT SHIFT Operation for the x and y is :",x >> 1) # Output: 2 (Binary: 0010 → Shifts right by 1)

# Declare two integers
a = 12  # Binary: 1100
b = 5   # Binary: 0101

# Bitwise AND (&)
print(a & b)  # Output: 4
# 1100 (12)
# 0101 (5)
# ----
# 0100 (4)

# Bitwise OR (|)
print(a | b)  # Output: 13
# 1100 (12)
# 0101 (5)
# ----
# 1101 (13)

# Bitwise XOR (^)
print(a ^ b)  # Output: 9
# 1100 (12)
# 0101 (5)
# ----
# 1001 (9)

# Bitwise NOT (~)
print(~a)  # Output: -13
# Inverts all bits of a → -(a+1)
# ~12 = -13

# Left Shift (<<)
print(a << 2)  # Output: 48
# 1100 << 2 becomes 110000 → binary for 48

# Right Shift (>>)
print(a >> 2)  # Output: 3
# 1100 >> 2 becomes 0011 → binary for 3
