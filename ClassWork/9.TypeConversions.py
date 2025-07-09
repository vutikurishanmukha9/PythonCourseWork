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
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
list(b)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable

#complex to another data types

c = 2+18j

int(c)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
str(c)
'(2+18j)'
bool(c)
True
float(c)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
tuple(c)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
list(c)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
