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
print("Returns the last occurrence of the substring:",s.rfind('i'))                   #Returns the last occurrence of the substring: 16
print("Counts how many times 'a' appears:",s.count('a'))                              #Counts how many times 'a' appears: 1
print("Counts how many times 's' appears:",k.count('s'))                              #Counts how many times 's' appears: 1

#4. String Testing Methods (Boolean Results)

### 1. startswith(sub) – Checks if a string starts with a given substring
print("Checking whether the String starts with py or not:","python".startswith("py"))  # True → "python" starts with "py"

# 2. endswith(sub) – Checks if a string ends with a given substring
print("Checking whether the String ends with py or not:","python".endswith("on"))  # True → "python" ends with "on"

# 3. isalpha() – Returns True if all characters are alphabetic (no numbers or symbols)
print("Checking whether the String contains all charcters or not:","Hello".isalpha())  # True → All characters are alphabets
print("Checking whether the String contains all charcters or not:","Hello123".isalpha())  # False → Contains digits

# 4. isalnum() – Returns True if all characters are alphanumeric (letters and numbers)
print("Checking whether the string contains alphanumeric (letters and numbers) or not:","abc123".isalnum())  # True → Letters + digits only
print("Checking whether the string contains alphanumeric (letters and numbers) or not:","abc_123".isalnum())  # False → Contains underscore (_)

# 5. islower() – Returns True if all alphabetic characters are lowercase
print("Checking whether all alphabetic characters in string are lowercase:","hello".islower())  # True → All characters are lowercase
print("Checking whether all alphabetic characters in string are lowercase:","Hello".islower())  # False → Contains uppercase 'H'

# 6. isupper() – Returns True if all alphabetic characters are uppercase
print("Checking whether all alphabetic characters in string are UPPERcase:","HELLO".isupper())  # True → All characters are uppercase
print("Checking whether all alphabetic characters in string are UPPERcase:","Hello".isupper())  # False → Contains lowercase 'e', 'l', 'l', 'o'

# 7. isspace() – Returns True if the string contains only whitespace characters
print("Checking whether the string contains only whitespace characters:","   ".isspace())  # True → Only spaces
print("Checking whether the string contains only whitespace characters:"," \n\t".isspace())  # True → Whitespace characters (space, newline, tab)
print("Checking whether the string contains only whitespace characters:","a b".isspace())  # False → Contains non-whitespace characters

# 8. istitle() – Returns True if string is in title case (each word starts with uppercase letter)
print("Checking whether the string is in title case:","Hello World".istitle())  # True → Each word starts with uppercase
print("Checking whether the string is in title case:","hello world".istitle())  # False → Words not capitalized

# 9. isidentifier() – Returns True if string is a valid Python identifier
print("Checking whether the string is a valid Python identifier:","variable1".isidentifier())  # True → Valid Python variable name
print("Checking whether the string is a valid Python identifier:","1variable".isidentifier())  # False → Cannot start with a digit
print("Checking whether the string is a valid Python identifier:","for".isidentifier())  # True → Valid identifier but a Python keyword

# 10. isdecimal() – Returns True if all characters are decimal digits (0–9)
print("12345".isdecimal())  # True → All decimal digits
print("²".isdecimal())  # False → Superscript 2 is not a decimal digit

# 11. isdigit() – Returns True if all characters are digits (includes superscripts, etc.)
print("12345".isdigit())  # True → All digits
print("²".isdigit())  # True → Superscript 2 is considered a digit

# 12. isnumeric() – Returns True if characters are numeric (includes digits, fractions, etc.)
print("12345".isnumeric())  # True → Digits
print("½".isnumeric())  # True → Fraction
print("Verifing whether the number is numeric or not:","Ⅷ".isnumeric())  # True → Roman numeral 8

#5. Replace & Modify Methods

# 1. replace function

# Replaces all occurrences of the substring `old` with the substring `new`.

text = "apple"
print(text.replace("p", "b"))  # Output: "abble" # Explanation: All 'p' characters are replaced with 'b'

# 2. Function - str.maketrans(from_str, to_str)
# Creates a translation table that maps each character in from_str to the corresponding character in to_str.
# Used together with the translate() method.

# Example: Replacing 'a' with '%', 'o' with '#', and 'n' with '5'

trans_table = str.maketrans("aon", "%#5")
print(trans_table)        # Output: {97: 37, 111: 35, 110: 53}

# Explanation:
# ASCII of 'a' (97) → '%' (37)
# ASCII of 'o' (111) → '#' (35)
# ASCII of 'n' (110) → '5' (53)

# 3. function - translate(table)

# Applies the translation table created by str.maketrans() to the string.

text = "python"
table = str.maketrans("aon", "%#5")
translated = text.translate(table)
print("Translated text is:",translated)  # Output: "pyth#5"

# Explanation:
# 'o' → '#' and 'n' → '5'
# So, 'python' becomes 'pyth#5'

#6.Splitting & Joining Methods

# 1. split(sep)
# Splits the string into a list of substrings using the specified separator.
data = "a,b,c"
print(data.split(","))  # Output: ['a', 'b', 'c']
# Explanation: The comma ',' is used as the separator to split the string into parts.

# 2. rsplit(sep, maxsplit)
# Same as split(), but starts splitting from the right.
data = "a,b,c"
print(data.rsplit(",", 1))  # Output: ['a,b', 'c']
# Explanation: Only 1 split is done from the rightmost separator.


# 3. splitlines()
# Splits the string at line breaks (\n or \r\n) into a list of lines.
text = "Hello\nWorld"
print(text.splitlines())  # Output: ['Hello', 'World']
# Explanation: It separates the string wherever a newline character appears.

# 4. join(iterable)
# Joins the elements of an iterable (like a list or tuple) into a single string using the string as the separator.
words = ["Hello", "World"]
print(" ".join(words))  # Output: "Hello World"
# Explanation: A space character " " is used to join the words into one string.

# 5. partition(sep)
# Splits the string into a 3-part tuple: (before_sep, sep, after_sep)
text = "apple-pie"
print(text.partition("-"))  # Output: ('apple', '-', 'pie')
# Explanation: It splits at the first occurrence of '-' and keeps the separator in the result.

# 6. rpartition(sep)
# Similar to partition(), but splits at the **last** occurrence of the separator.
text = "apple-pie"
print(text.rpartition("-"))  # Output: ('apple', '-', 'pie')
# In this example, the result is the same as partition() since there's only one separator.
# But if multiple separators exist, rpartition() uses the **last** one.

#7. Whitespace & Trimming Methods

# 1. strip([chars])
# Removes leading (left) and trailing (right) characters from the string.
# By default, it removes whitespace characters like space, tab, newline.

text = "   hello   "
print(text.strip())  # Output: "hello"
# Explanation: Removes spaces from both ends (not in the middle)

# You can also remove specific characters by passing them as an argument.
text = "---hello---"
print(text.strip("-"))  # Output: "hello"
# Explanation: Removes '-' characters from both the beginning and end

# 2. lstrip([chars])
# Removes characters from the left (start) of the string.
text = "---hello"
print(text.lstrip("-"))  # Output: "hello"
# Explanation: Strips only the left side of '-' characters

# 3. rstrip([chars])
# Removes characters from the right (end) of the string.
text = "hello---"
print(text.rstrip("-"))  # Output: "hello"
# Explanation: Strips only the right side of '-' characters

#8. Encoding & Decoding Methods

# 1. encode(encoding)
# Converts a string into a bytes object using the specified encoding.
# Common encoding: "utf-8" (most widely used for text data)

text = "hello"
encoded_bytes = text.encode("utf-8")
print(encoded_bytes)  # Output: b'hello'
# Explanation: The string "hello" is encoded into a bytes object.
# The prefix `b` indicates that it's a byte string (not regular string).

# 2. decode(encoding)
# Converts a bytes object back to a regular string using the specified encoding.
# This is the reverse of encode().

byte_data = b'hello'
decoded_text = byte_data.decode("utf-8")
print(decoded_text)  # Output: "hello"
# Explanation: The byte object is decoded back into a normal string using UTF-8 encoding.