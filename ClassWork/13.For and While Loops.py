#For loop
'''For Loop Examples'''
'''How to print a table using For loop'''

n = int(input("Enter a number: "))
for i in range(1,21):
    print(f'{n} * {i} = {n*i}')


'''Output'''
# Enter a number: 5

# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50
# 5 * 11 = 55
# 5 * 12 = 60
# 5 * 13 = 65
# 5 * 14 = 70
# 5 * 15 = 75
# 5 * 16 = 80
# 5 * 17 = 85
# 5 * 18 = 90
# 5 * 19 = 95
# 5 * 20 = 100

'''Another example'''
#To find the index of a character in the given string when ever the charcter apears 
s = input("Enter the names: ")
c = s.lower()
n = len(s)
ch = input("Enter the Character: ")

for i in range(n):
    if s[i] == ch:
        print(ch,i)

'''Output'''
# Enter the names: kohli bhuvi rajat jithesh
# Enter the Character: h
# h 2
# h 7
# h 21
# h 24

'''another example'''
#We have to take the user input and based on the user input we have to check at what index the user input is present

products = ['bat','ball','wickets','bails','pads']

l = input("Enter the items: ").split()

for i in l:
    if i in products:
        print(products.index(i),i)
    else:
        print(f"{i} is not available")

# Enter the items: bat ball

# 0 bat
# 1 ball

#While Loop

'''No. of bullets left in the mag'''

bullets = 10
while bullets > 0:
    bullets -= 1
    if bullets > 0:
        print(f"{bullets} are left")
    else:
        print("No bullets are there change the mag")

'''Output'''
# 9 are left
# 8 are left
# 7 are left
# 6 are left
# 5 are left
# 4 are left
# 3 are left
# 2 are left
# 1 are left
# No bullets are there change the mag

'''Login Attempts example for the While loop'''

email,pwd = 'abc@gmail.com','abcdefg'

max_attempts = 5

while max_attempts > 0:
    user_email = input("Enter the Gmail: ")
    password = input("Enter the Password: ")
    if user_email == email and password == pwd:
        print("Login Succesfull")
        break
    else:
        print("Invalid Password")
        max_attempts -= 1
else:
    print("Try again after Some time")

'''output'''

#For valid login
# Enter the Gmail: abc@gmail.com
# Enter the Password: abcdefg
# Login Succesfull

#For invalid login




