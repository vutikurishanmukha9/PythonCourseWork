#The Birthday Format Fixer (STring & Type Conversion)
# Input = A string representing a date:dd-mm-yyyy
# Output = A string formatted as yyyy/mm/dd

n = input("Enter the date of birthday as dd-mm-yyyy: ")
print(len(n))
print(f'{n[6:10]}/{n[3:5]}/{n[0:2]}')

