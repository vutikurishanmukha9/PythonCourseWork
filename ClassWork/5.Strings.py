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


# names
# 'HarshithSowmyaKiranVarunMani'
# names[-1:-4:-1]
# 'ina'
# names[-1:-5:-1]
# 'inaM'
# names[-5:-10:-1]
# 'nuraV'
# names[-15:-10:-1]
# ''
# names[-10:-15:-1]
# 'nariK'
# names
# 'HarshithSowmyaKiranVarunMani'
# 'Kiran' in names
# True
# 'Adithya' in names
# False
# 'Hema' not in names
# True
# 'mounika' not in names
# True
# names
# 'HarshithSowmyaKiranVarunMani'
# len(names)
# 28
# max(names)
# 'y'
# min(names)
# 'H'
# sorted(names)
# ['H', 'K', 'M', 'S', 'V', 'a', 'a', 'a', 'a', 'a', 'h', 'h', 'i', 'i', 'i', 'm', 'n', 'n', 'n', 'o', 'r', 'r', 'r', 's', 't', 'u', 'w', 'y']
# ord('H')
# 72
# ord('K')
# 75
# ord('S')
# 83
# ord('a')
# 97
# chr(97)
# 'a'
# chr(1)
# '\x01'
# chr(30)
# '\x1e'
# chr(101)
# 'e'
# chr(120)
# 'x'
# chr(130)
# '\x82'
# ord('1')
# 49
# ord('9')
# 57
# ord('@')
# 64
# names
# 'HarshithSowmyaKiranVarunMani'
# names.upper()
# 'HARSHITHSOWMYAKIRANVARUNMANI'
# names.lower()
# 'harshithsowmyakiranvarunmani'
# names.capitalize()
# 'Harshithsowmyakiranvarunmani'
# d='python programming lang'
# d.title()
# 'Python Programming Lang'
# d
# 'python programming lang'
# d.captilize()
# Traceback (most recent call last):
#   File "<pyshell#94>", line 1, in <module>
#     d.captilize()
# AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
# d.capitalize()
# 'Python programming lang'
# d
# 'python programming lang'
# d
# 'python programming lang'
# names
# 'HarshithSowmyaKiranVarunMani'
# names.swapcase()
# 'hARSHITHsOWMYAkIRANvARUNmANI'
# k='नमते你好'
# k.swapcase()
# 'नमते你好'
# k.casefold()
# 'नमते你好'
# k="🙂"
# k
# '🙂'
# "ß".casefold()
# 'ss'
# "ß".lower()
# 'ß'
# d
# 'python programming lang'
# d.center(50,'-')
# '-------------python programming lang--------------'
# d.center(50,'*')
# '*************python programming lang**************'
# d.center(50,' ')
# '             python programming lang              '
# d.ljust(50,'_')
# 'python programming lang___________________________'
# d.rjust(50,'_')
# '___________________________python programming lang'
# "name".ljust(10,' ')
# 'name      '
# 'age'.ljust(10,' ')
# 'age       '
# 'dob'.ljust(10,' ')
# 'dob       '
# 'Address'.ljust(10,' ')
# 'Address   '
# "name".ljust(10,' ')+'sdfgyui'
# 'name      sdfgyui'
# '42'.zfill(5)
# '00042'
# '301'.zfill(2)
# '301'
# '301'.zfill(5)
# '00301'
# '4321'.zfill(5)
# '04321'
# names
# 'HarshithSowmyaKiranVarunMani'
# names.find("kiran")
# -1
# names.find("Kiran")
# 14
# names.find(names[:8])
# 0
# names.find(names[14:19])
# 14
# names.find('z')
# -1
# names.find('H')
# 0
# names.find('S')
# 8
# names.find('a')
# 1
# names.rfind('a')
# 25
# names.index('S')
# 8
# names.index('z')
# Traceback (most recent call last):
#   File "<pyshell#133>", line 1, in <module>
#     names.index('z')
# ValueError: substring not found
# names
# 'HarshithSowmyaKiranVarunMani'
# names.count('a')
# 5
# names.count('i')
# 3
# names.count('r')
# 3