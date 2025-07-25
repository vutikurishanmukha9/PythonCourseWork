'''Functions

Definition of Functions

A function in Python is a reusable block of code that performs a specific task. It helps in breaking 
down large programs into smaller, manageable parts. Functions improve code reusability, readability, and modularity.

Features of Functions in Python
1. Code Reusability - Write once, use multiple times.
2. Modularity - Divide code into logical sections.
3. Maintainability - Easier to debug and modify.
4. Scalability - Helps in handling complex applications.
5. Encapsulation - Hides implementation details from users.
6. Parameterization - Functions accept arguments to perform operations dynamically.
7. Return Values - Functions can return values for further use.'''

data = {'current_balance':12345,'history':[]}

def check_balance():
    print(f'Current Balance: {data['current_balance']}')

def deposit():
    amount = int(input("Enter the amount: "))
    data['current_balance'] += amount
    data['history'].append(f'Deposited - Rs{amount}')
    print(f'Deposited - Rs{amount}')
def withdraw():
    amount = int(input("Enter the amount: "))
    if data['current_balance'] >=amount:
        data['current_balance']-= amount
        data['history'].append(f'Withdrawed - Rs{'amount'}')
def check_history():
    print("Transactions")
    for i in data['history']:
        print(i)
while True:
    print("======Welcome to ATM======")
    print('1.Check Balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.History')
    print('0.Exit')

    choice = int(input("Enter your choice:  "))
    if choice == 0:
        print('Thanks Visit Again'.center(50,'*'))
        break
    elif choice == 1:
        check_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        check_history()
    else:
        print("Invalid coice. Try Again")



def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def div(a, b):
    return a // b  

def mod(a, b):
    return a % b

value = input("Enter the Value (e.g., 12+5): ")
op = ""
for i in value:
    if not i.isdigit():
        op = i
        break

if op:
    a, b = value.split(op)
    a, b = int(a), int(b)
    if op == '+':
        print(add(a, b))
    elif op == '-':
        print(sub(a, b))
    elif op == '*':
        print(multiplication(a, b))
    elif op == '/':
        print(div(a, b))
    elif op == '%':
        print(mod(a, b))
    else:
        print("Unsupported operator.")
else:
    print("No operator found in input.")
