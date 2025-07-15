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

#Shopping cart Analyzer
#input- list of floats seperated by space 
#Output - Two lines

n = list(map(float, input("Enter the Numbers: ").split()))
print("Sum:", sum(n))
print("Max:", max(n))


#Secure login system (Tuple and Conditional)

#input - Two strings: username and password
#Output - Login Successful / Acess Denied

credentials = {"admin" , "python123"}

n = input("Enter the username: ")
s = input("Enter the Password: ")

if n and s in credentials:
    print("Login Successful")
else:
    print("Acess Denied")


#Clean my list (List and Type Conversions)
#Input - String of numbers of names seperated by commas
#Output - Print a sorted list (alphabetical) of unique
n = input("Enter names or numbers separated by commas: ").split(",")
unique_items = set(n)              
sorted_list = sorted(unique_items) 
print(list(sorted_list))         

#Student Marks Record (Dictonary Operations)
#input - First line:integer n 
#Next n lines:namesand marks (sepearted by spaces)
#Output - Name of the student with highest marks

n = int(input("Enter number of students: "))
student_marks = {}
for _ in range(n):
    name, marks = input("Enter name and marks: ").split()
    student_marks[name] = int(marks)
topper = max(student_marks, key=student_marks.get)
print("Topper:", topper)

#Reverse My Words
#Input - a string sentence
# output - Each word reversed, seperated by space

sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_word_list = []
for word in words:
    reversed_word = word[::-1]    
    reversed_word_list.append(reversed_word)  
result = ' '.join(reversed_word_list)
print("Reversed sentence word by word:", result)

#Clean My List (List and Type Conversions)
#Input - String of numbers 
#Output - List of Non-Zeros

n = list(map(int,input("Enter the list of the numbers: ").split(" ")))
non_zero_list = []
for num in n:
    if num != 0:
        non_zero_list.append(num)
print("List of Non-Zeros:", non_zero_list)


#The Frequncy Counter (Dictonary + String)
#Input - A single-line string
#Output - Q dictionary with charcters as keys and their counts as values
n = input("Enter a string: ")
frequency_counter = {}
for char in n:
    if char in frequency_counter:
        frequency_counter[char] += 1
    else:
        frequency_counter[char] = 1
print("Character Frequency:", frequency_counter)
