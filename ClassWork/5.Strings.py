#String and Strings Operations

s='shanmukh' #Declaring A String
print("The String:",s) #The Output of the S is 'shanmukh'

s = 'shanmukh' #Declaring the String with single Qutations
s = "shanmukh" #Declaring the String with Double Qutations
s = '''shanmukh''' #Declaring the String with Triple Qutations
s = '' #Intailizing an empty String

#Concatenation (+) - Joining two or more strings.

fname='Shanmukh' #Declaring a string 
lname='Vutikuri' #Decalring a another string
print("Concatnating the both fname and lname:", fname+lname) #ShanmukhVutikuri

#Repetition (*) - Repeating a string multiple times.

Repeat = fname * 10
print("Repetition of the string:",Repeat) #ShanmukhShanmukhShanmukhShanmukhShanmukhShanmukhShanmukhShanmukhShanmukhShanmukh

# Indexing - Accessing individual characters using indices.

s = "Shanmukh Vutikuri"
print("5th Index element in the s is:", s[5]) #5th Index element in the s is: u
print("1st index element in the s is:", s[1]) #1st index element in the s is: h

#Slicing - Extracting a part (substring) of the string.

print("The index of the element from the reverse is :",s[-3]) #The index of the element from the reverse is : u
print("The index of the element from the reverse is :",s[-1]) #The index of the element from the reverse is : i
print("The element that which is at the index 5:",s[5]) #The element that which is at the index 5: u

RCB='kohlibhuvirajat'
print("The string which is stroed in :",RCB) #The string which is stroed in RCB: kohlibhuvirajat
print("The length of the string RCB is:",len(RCB)) #The length of the string RCB is: 15
print("The output after slicing is :",RCB[0:5]) #The output after slicing is : kohli
print("The output after slicing is :",RCB[5:10]) #The output after slicing is : bhuvi
print("The output after slicing is :",RCB[10:15]) #The output after slicing is : rajat
print("The even elements in the :",RCB[1:15:2]) #The even elements in the RCB: olbuiaa
print("The odd elements in the RCB:",RCB[0:15:2]) #The odd elements in the RCB: khihvrjt
print("The Reverse slicing of the RCB is:",RCB[-5:]) #The Reverse slicing of the RCB is: rajat
print("The Reverse slicing of the RCB is:",RCB[-10:-5]) #The Reverse slicing of the RCB is: bhuvi
print("The Reverse slicing of the RCB is:",RCB[-15:-10]) #The Reverse slicing of the RCB is: kohli
print("The Output after slicing:",RCB[-15:-10]) #The Output after slicing: kohli
print("Printing the Reversing of the:",RCB[::-1]) #Printing the Reversing of the: tajarivuhbilhok
print("Printing the Reversing of the string by skipping some part:",RCB[-1:-6:-1]) #Printing the Reversing of the string by skipping some part: tajar

#Membership (in, not in) - Checking if a substring exists within a string.

print(RCB) #kohlibhuvirajat
print("Checking whether kolhi is present in RCB or not:",'kohli' in RCB) #Checking whether kolhi is present in RCB or not: True
print("Checking whether maxi is present in RCB or not:",'maxi' in RCB) #Checking whether maxi is present in RCB or not: False
print("Checking whether Green is present in RCB or not:",'green'  not in RCB) #Checking whether Green is present in RCB or not: True
print("Checking whether siraj is present in RCB or not:",'siraj' not in RCB) #Checking whether siraj is present in RCB or not: True

#Built-in String Functions

print(RCB)  #kohlibhuvirajat
print("The length of the String that present in RCB:",len(RCB)) #The length of the String that present in RCB: 15
print("The largest element that present in the RCB:",max(RCB)) #The largest element that present in the RCB: v
print("The Smallest element that presents in the RCB:",min(RCB)) #The Smallest element that presents in the RCB: a
print("Sorting all the elements that contain in the RCB:",sorted(RCB)) #Sorting all the elements that contain in the RCB: ['a', 'a', 'b', 'h', 'h', 'i', 'i', 'j', 'k', 'l', 'o', 'r', 't', 'u', 'v']
print("The ASCII value of the element in the string that stored in the RCB:",ord('H')) #The ASCII value of the element in the string that stored in the RCB: 72


# Complete List of Python String Methods with Examples

# 1. Case Conversion Methods

print("Converting all the elements in s to the UPPER CASE:",s.upper())       #Converting all the elements in s to the UPPER CASE: SHANMUKH VUTIKURI
print("Converting all the elements in s to the lower CASE:",s.lower())        #Converting all the elements in s to the lower CASE: shanmukh vutikuri

k = 'shanmukh vutikuri'

print("Capitalizes the first character:",k.capitalize())          #Capitalizes the first character: Shanmukh vutikuri
print("Capitalizes the first letter of each word:",k.title())      #Capitalizes the first letter of each word: Shanmukh Vutikuri
print("Swaps case: upper → lower, lower → upper:",s.swapcase())     #Swaps case: upper → lower, lower → upper: sHANMUKH vUTIKURI
print("ß".casefold())           # ss

# 2. Alignment & Formatting Methods

print("Centers the String within the Width:",s.center(40,'*'))        #Centers the String within the Width: ***********Shanmukh Vutikuri************
print("Left-align the String within the Width:",s.ljust(25,"-"))       #Left-align the String within the Width: Shanmukh Vutikuri--------
print("Rignt-align the String within the Width:",s.rjust(25,"_"))       #Rignt-align the String within the Width: ________Shanmukh Vutikuri
print("Pads the string with zeros on the left:",'17/12/2003'.zfill(10))   #Pads the string with zeros on the left: 17/12/2003

# 3. Search & Find Methods

print("Returns the index of first occurrence, -1 if not found:",s.find('shan'))       #Returns the index of first occurrence, -1 if not found: -1
print("Returns the last occurrence of the substring:",s.rfind('i'))  #Returns the last occurrence of the substring: 16
print("Counts how many times 'a' appears:",s.count('a'))             #Counts how many times 'a' appears: 1
print("Counts how many times 's' appears:",k.count('s'))             #Counts how many times 's' appears: 1