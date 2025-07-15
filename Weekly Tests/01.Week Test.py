#The Birthday Format Fixer (STring & Type Conversion)
# Input = A string representing a date:dd-mm-yyyy
# Output = A string formatted as yyyy/mm/dd

n = input("Enter the date of birthday as dd-mm-yyyy: ")
print(len(n))
print(f'{n[6:10]}/{n[3:5]}/{n[0:2]}')

#The even Odd Game 
#Input:an integer n 
#Output: "Even Winner" or "Odd winner"

n = int(input("Enter the Number: "))
s = n % 2
if s == 0:
    print("Even Winner")
else:
    print("Odd Winner")

#Vowel Replacer Bot 
#Input: a string msgg
#Output: Modified string with vowels replaced by *

n = input("Enter the message: ")

s = n.replace('a', '*')
s = s.replace('e', '*')
s = s.replace('i', '*')
s = s.replace('o', '*')
s = s.replace('u', '*')

print(s)


