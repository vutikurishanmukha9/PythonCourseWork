# Input Formatting
# Python's input() function is used to take input from the user during program execution. By
# default, it returns a string. We often convert the input into int, float, list, tuple, set,
# or dict as needed.

# 1. String Input
# Use case: Entering a name, email, city, etc.

name = input("Enter your full name: ") #Output:-Enter your full name: shanmukh
print(name)  #Output:-shanmukh

# 2. Integer Input
# Use case: Age, quantity, mobile number, number of items in cart.

quantity = int(input("Enter the number of items: ")) #OUtput:-Enter the number of items: 12 #It takes only integer as a input
print(quantity) #Output:-12

# 3. Float Input
# Use case: Price, temperature, discount, rating.

price = float(input("Enter the product price: ")) #Output:- Enter the product price: 12.25 #It takes only floast value as a input
print(price) #Output:- 12.25

# 4. Input as List (Space-separated)
# Use case: List of names, marks, or product IDs.

names = input("Enter employee names (space-separated):").split() #Enter employee names (space-separated):kohli rajat bhuvi
print(names) #['kohli', 'rajat', 'bhuvi']

# 5. Input as List (Comma-separated)
# Use case: Tags, emails, product categories.

tags = input("Enter tags (comma-separated): ").split(',') #nter tags (comma-separated): kohli rajat bhuvi
print(tags) #['kohli rajat bhuvi']

# 6. List of Integers
# Use case: Marks, product prices, IDs.

marks = list(map(int, input("Enter marks: ").split())) #Enter marks: 89 76 94 82
print(marks) #Output: [89, 76, 94, 82]


# 7. List of Floats
# Use case: Sensor readings, weights, product prices.

weights = list(map(float, input("Enter weights: ").split())) #Enter weights: 55.6 62.1 70.3
print(weights) #Output: [55.6, 62.1, 70.3]

# 8. Tuple Input
# Use case: Coordinates, dimensions (length, width, height).

dimensions = tuple(map(int, input("Enter length, width,height: ").split())) #Enter length, width, height: 10 20 15
print(dimensions) #Output: (10, 20, 15)


# 9. Set Input
# Use case: Selected image IDs where duplicates must be removed (e.g., in a photo-sharing app).

selected_ids = set(map(int, input("Enter selected image IDs:").split())) #Enter selected image IDs: 101 102 103 101 104
print(selected_ids) #Output: {101, 102, 103, 104}


# 10. Dictionary Input using eval()
# Use case: When entering structured data like configuration settings or user profiles.

profile = eval(input("Enter user profile as a dictionary: ")) #Enter user profile as a dictionary: {'name': 'Shanmukh', 'age': 21, 'role': 'admin'}
print(profile) #Output: {'name': 'Shanmukh', 'age': 21, 'role': 'admin'}

# Note: Only use eval() when input is trusted.

# 11. Multiple Inputs with Unpacking
# Use case: Login form or payment details.

username, password = input("Enter username and password:").split()
print("Username:", username) #Enter username and password: user01 mypassword123
print("Password:", password) #Username: user01 
#Password: mypassword123