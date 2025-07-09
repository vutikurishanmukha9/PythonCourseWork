# Type Conversion (Type Casting)
# Type conversion in Python refers to converting the value of one data type to another using built-in functions such as int(), float(), str(), bool(), list(), tuple(), set(),and dict().
#Integer to another data types
a = 18
float(a)
18.0
str(a)
'18'
complex(a)
(18+0j)
bool(a)
True

list(a)

# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     list(a)
# TypeError: 'int' object is not iterable
tuple(a)
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     tuple(a)
# TypeError: 'int' object is not iterable
dict(a)
# Traceback (most recent call last):
#   File "<pyshell#7>", line 1, in <module>
#     dict(a)
# TypeError: 'int' object is not iterable
set(a)
# Traceback (most recent call last):
#   File "<pyshell#8>", line 1, in <module>
# set(a)
# TypeError: 'int' object is not iterable

#float to another data types

b = 1.8
int(b)
1
complex(b)
(1.8+0j)
bool(b)
True
tuple(b)
# Traceback (most recent call last):
#   File "<pyshell#23>", line 1, in <module>
#     tuple(b)
# TypeError: 'float' object is not iterable
list(b)
# Traceback (most recent call last):
#   File "<pyshell#24>", line 1, in <module>
#     list(b)
# TypeError: 'float' object is not iterable
set(b)
# Traceback (most recent call last):
#   File "<pyshell#25>", line 1, in <module>
#     set(b)
# TypeError: 'float' object is not iterable
dict(b)
# Traceback (most recent call last):
#   File "<pyshell#26>", line 1, in <module>
#     dict(b)
# TypeError: 'float' object is not iterable

#complex to another data types

c = 2+18j

int(c)
# Traceback (most recent call last):
#   File "<pyshell#33>", line 1, in <module>
#     int(c)
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
str(c)
'(2+18j)'
bool(c)
True
float(c)
# Traceback (most recent call last):
#   File "<pyshell#36>", line 1, in <module>
#     float(c)
# TypeError: float() argument must be a string or a real number, not 'complex'
tuple(c)
# Traceback (most recent call last):
#   File "<pyshell#37>", line 1, in <module>
#     tuple(c)
# TypeError: 'complex' object is not iterable
set(c)
# Traceback (most recent call last):
#   File "<pyshell#38>", line 1, in <module>
#     set(c)
# TypeError: 'complex' object is not iterable
list(c)
# Traceback (most recent call last):
#   File "<pyshell#39>", line 1, in <module>
#     list(c)
# TypeError: 'complex' object is not iterable
dict(c)
# Traceback (most recent call last):
#   File "<pyshell#40>", line 1, in <module>
#     dict(c)
# TypeError: 'complex' object is not iterable

#string to other data types

s = 'kohli'
int(s)
# Traceback (most recent call last):
#   File "<pyshell#42>", line 1, in <module>
#     int(s)
# ValueError: invalid literal for int() with base 10: 'kohli'
float(s)
# Traceback (most recent call last):
#   File "<pyshell#43>", line 1, in <module>
#     float(s)
# ValueError: could not convert string to float: 'kohli'
complex(s)
# Traceback (most recent call last):
#   File "<pyshell#44>", line 1, in <module>
#     complex(s)
# ValueError: complex() arg is a malformed string
list(s)
['k', 'o', 'h', 'l', 'i']
tuple(s)
('k', 'o', 'h', 'l', 'i')
dict(s)
# Traceback (most recent call last):
#   File "<pyshell#49>", line 1, in <module>
#     dict(s)
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
set(s)
{'h', 'i', 'o', 'k', 'l'}

#list to other data types
l = [1,2,3,4,5]
int(l)
# Traceback (most recent call last):
#   File "<pyshell#52>", line 1, in <module>
#     int(l)
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
# Traceback (most recent call last):
#   File "<pyshell#53>", line 1, in <module>
#     float(l)
# TypeError: float() argument must be a string or a real number, not 'list'
str(l)
'[1, 2, 3, 4, 5]'
set(l)
{1, 2, 3, 4, 5}
tuple(l)
(1, 2, 3, 4, 5)
dict(s)
# Traceback (most recent call last):
#   File "<pyshell#57>", line 1, in <module>
#     dict(s)
# ValueError: dictionary update sequence element #0 has length 1; 2 is required

#tuple to other data types
t = (1,2,3,4,5)
int(t)
# Traceback (most recent call last):
#   File "<pyshell#77>", line 1, in <module>
#     int(t)
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
# Traceback (most recent call last):
#   File "<pyshell#78>", line 1, in <module>
#     float(t)
# TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
# Traceback (most recent call last):
#   File "<pyshell#79>", line 1, in <module>
#     complex(t)
# TypeError: complex() first argument must be a string or a number, not 'tuple'
set(t)
{1, 2, 3, 4, 5}
list(t)
[1, 2, 3, 4, 5]
dict(t)
# Traceback (most recent call last):
#   File "<pyshell#82>", line 1, in <module>
#     dict(t)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True

#set to other data types

set={1,2,3,4,5}
int(set)
# Traceback (most recent call last):
#   File "<pyshell#85>", line 1, in <module>
#     int(set)
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(set)
# Traceback (most recent call last):
#   File "<pyshell#86>", line 1, in <module>
#     float(set)
# TypeError: float() argument must be a string or a real number, not 'set'
bool(set)
True
complex(set)
# Traceback (most recent call last):
#   File "<pyshell#88>", line 1, in <module>
#     complex(set)
# TypeError: complex() first argument must be a string or a number, not 'set'
list(set)
[1, 2, 3, 4, 5]
tuple(set)
(1, 2, 3, 4, 5)
dict(set)
# Traceback (most recent call last):
#   File "<pyshell#91>", line 1, in <module>
#     dict(set)
# TypeError: cannot convert dictionary update sequence element #0 to a sequence

#Dictonary to other data types


