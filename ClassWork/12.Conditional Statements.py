# Conditional Statements
# Conditional statements allow a program to execute certain pieces of code based on whether
# a specific condition is True or False. They help in decision-making processes within the code.
# In Python, the main types of conditional statements are:
# 1. if Statement
# 2. if-else Statement
# 3. if-elif-else Statement
# 4. Nested Conditional Statements


# 1. if Statement
# The if statement is the most basic conditional statement. It checks if a condition is True. If it # is, the block of code
# under the if statement is executed. If the condition is False, the code is skipped.

#syntax
# '''simple if'''
# if condition:
#     #if-True-statements
# '''if-else'''
# if condition:
#     #if-true-statements
# else:
#     #False-statements

# '''if-elif-else'''
# if condition:
#     #if-true-statements
# elif condition:
#     #cond1 statements
# elif condition:
#     #Cond2 statements
# .
# .
# .
# .
# .
# elif condition:
#     #Cond N Statement
# else:
#     #False-statements

# '''nested if'''
# if condition-outer:
#     if condition -inner:
#         #if0True stmts
#     else:
#         #if-false stmts
# else:
#     #False stmts

'''Example Using only IF'''
s =input("Enter the status(R O G):")

if s == 'R':
    print("Stop")
if s == 'O':
    print("Ready")
if s == 'G':
    print("Gooooooooo")

'''Example Using only If and Else'''

items = ['shoes','laptop','smartwatch','phone','airpods','toycars']

print("Welcome to Amazon".center(45,'*'))
searchinput = input("Enter the item:").lower()

if searchinput in items:
    print(f'{searchinput} found. Buy now!!')
else:
    print(f'{searchinput} is not found.It is out of stock can you check me later')

'''Example for If, Elif and Else'''
'''Weekend Budget Plan'''

amount = int(input("Enter the Amount that you want to spend on weekend:"))

if amount > 20000:
    print("Go to Goa")
elif amount > 15000:
    print("Go for Shopping")
elif amount > 10000:
    print("Clubbing")
elif amount > 5000:
    print("Cafe/Dinner")
elif amount > 2000:
    print("Maintaincess")
elif amount > 500:
    print("Go for the Movie")
elif amount > 100:
    print("Go for the street food")
else:
    print("Wait for Your Time")


'''Example for If, Elif and Else'''
'''Grades Based On Your marks'''
#O grade = above 90 Marks
#A+ grade = 90 marks - 85 marks
#A grade = 84 marks - 71 marks
#B grade = 70 marks - 61 marks
#C grade = 60 marks - 51 marks
#D grade = 50 marks - 41 marks
#E grade = 40 marks - 35 marks
#F grade = Below 35 marks

data = {
    1:{'name':'kohli','attempt_status':False,'Python':0,'sql':0,'powerBI':0},
    2:{'name':'Bhuvi','attempt_status':True,'Python':100,'sql':90,'powerBI':80},
    3:{'name':'Rajat','attempt_status':True,'Python':70,'sql':90,'powerBI':50},
    4:{'name':'Jitesh','attempt_status':False,'Python':30,'sql':100,'powerBI':25},
    5:{'name':'Salt','attempt_status':True,'Python':60,'sql':40,'powerBI':35}
}

stuid = int(input("Enter the Student ID:"))
print(data[stuid])
if data[stuid]['attempt_status']:
    total = (data[stuid]['Python'] + data[stuid]['sql'] + data[stuid]['powerBI']) / 3
    if total >= 90:
        print(f"Congrats !!!!!\n{data[stuid]['name']} got 'A' grade")
        print("Feedback: Good and keep it up!")
    elif total >= 75:
        print(f"Congrats !!!!!\n{data[stuid]['name']} got 'B' grade")
        print("Feedback: Good and work more!")
    elif total >= 50:
        print(f"Congrats !!!!!\n{data[stuid]['name']} got 'C' grade")
        print("Feedback: Can work hard to achieve more!")
    else:
        print(f"Congrats !!!!!\n{data[stuid]['name']} got 'D' grade")
        print("Feedback: You have to work hard!")
else:
    print("Student has not attempted the test.")
    
# '''Ticket Booking'''
# seats = {
#     'L1':True,
#     'L2':True,
#     'U1':True,
#     'U2':False,}

# print("Bus seats:",seats.Keys())




'''Postive or Negative'''
num = int(input("Enter a number: "))

if num > 0:
    print(num,":is a Positve number")
elif num < 0:
    print(num,":is a negative number")
else:
    print(num,":is equal to Zero")

'''Even or ODD'''

num = int(input())

if num % 2 == 0:
    print(f'{num} is the even number')
else:
    print(f'{num} is the ODD number')

'''Leap Year'''

Year = int(input("Enter the year: "))
if Year % 400 == 0 or Year % 4 == 0 and Year % 100 != 0:
    print(f'{Year} is a leap year')
else:
    print(f'{Year} is not a leap year')


