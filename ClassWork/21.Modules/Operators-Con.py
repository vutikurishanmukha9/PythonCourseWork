import Operators as OP

a = int(input("Enter the input 1: "))
b = int(input("Enter the input 2: "))

op = input("+  -  *  //  /  **  % ")
if op == '+':
    OP.add(a,b)
elif op == '-':
    OP.sub(a,b)
elif op == '*':
    OP.mul(a,b)
elif op == '/':
    OP.div(a.b)
elif op == '//':
    OP.floor(a,b)
elif op == '%':
    OP.mod(a,b)