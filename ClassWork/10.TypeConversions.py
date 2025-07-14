# Type Conversion (Type Casting) in Python
# Python provides several built-in functions for converting one data type to another:
# int(), float(), str(), bool(), list(), tuple(), set(), dict(), complex()

# Integer to Other Types

a = 18
float(a)      # 18.0
str(a)        # '18'
complex(a)    # (18+0j)
bool(a)       # True

# Invalid conversions - int is not iterable
list(a)       #TypeError
tuple(a)      #TypeError
dict(a)       #TypeError
set(a)        #TypeError

#Float to Other Types

b = 1.8
int(b)        # 1
complex(b)    # (1.8+0j)
bool(b)       # True

# Invalid conversions - float is not iterable
list(b)       #TypeError
tuple(b)      #TypeError
set(b)        #TypeError
dict(b)       #TypeError

# Complex to Other Types

c = 2 + 18j
str(c)        #'(2+18j)'
bool(c)       #True

#Invalid conversions - cannot convert complex to real types or iterables
int(c)        #TypeError
float(c)      #TypeError
list(c)       #TypeError
tuple(c)      #TypeError
set(c)        #TypeError
dict(c)       #TypeError


# String to Other Types

s = "kohli"

list(s)       #['k', 'o', 'h', 'l', 'i']
tuple(s)      #('k', 'o', 'h', 'l', 'i')
set(s)        #{'k', 'o', 'h', 'l', 'i'} (unordered, unique chars)
bool(s)       #True (non-empty string)

#Invalid conversions - string must be numeric for number types
int(s)        #ValueError
float(s)      #ValueError
complex(s)    #ValueError
dict(s)       #ValueError

# List to Other Types

l = [1, 2, 3, 4, 5]
str(l)        #'[1, 2, 3, 4, 5]'
tuple(l)      #(1, 2, 3, 4, 5)
set(l)        #{1, 2, 3, 4, 5}
bool(l)       #True (non-empty list)

#Invalid conversions
int(l)        #TypeError
float(l)      #TypeError
dict(l)       #TypeError unless elements are pairs

# Tuple to Other Types

t = (1, 2, 3, 4, 5)
list(t)       #[1, 2, 3, 4, 5]
set(t)        #{1, 2, 3, 4, 5}
bool(t)       #True

#Invalid conversions
int(t)        #TypeError
float(t)      #TypeError
complex(t)    #TypeError
dict(t)       #TypeError unless elements are key-value pairs

# Set to Other Types

s = {1, 2, 3, 4, 5}
list(s)       #[1, 2, 3, 4, 5]
tuple(s)      #(1, 2, 3, 4, 5)
bool(s)       #True

#Invalid conversions
int(s)        #TypeError
float(s)      #TypeError
complex(s)    #TypeError
dict(s)       #TypeError

#  Dictionary to Other Types

d = {'a': 1, 'b': 2}
list(d)       #['a', 'b']
tuple(d)      #('a', 'b')
set(d)        #{'a', 'b'}
bool(d)       #True

#Invalid conversions
int(d)        #TypeError
float(d)      #TypeError
complex(d)    #TypeError
str(d)        #"{'a': 1, 'b': 2}" (optional)
