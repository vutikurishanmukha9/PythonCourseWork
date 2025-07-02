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


