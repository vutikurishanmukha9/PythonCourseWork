'''Calculate sum of all numbers from 1 to a given number'''

n = int(input("Enter a number: "))
count = 0
for i in range(1,n+1):
    count += i
    print(f'Number = {i} : sum = {count}')
print(f'The sum of N natural numbers is:{count}')