'''Display numbers from a list using a loop'''
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop

n = list(map(int,input("Enter the list of numbers: ").split()))
for i in range(len(n)):
    print(i , end = ' ')
    