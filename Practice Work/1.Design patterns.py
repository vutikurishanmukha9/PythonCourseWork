'''To print the following pattern'''
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

n = int(input("Enter a number: "))
for i in range (1,n+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print() 


# *
# * *
# * * *
# * * * *
# * * * * *

    
print("\nStar Pattern:")

for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()