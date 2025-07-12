'''Print multiplication table of a given number'''
n = int(input("Enter the number: "))
for i in range (1,21):
    print(f'{n} X {i} = {n*i}')