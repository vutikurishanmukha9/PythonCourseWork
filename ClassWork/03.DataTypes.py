a = 10
print(type(a))
# <class 'int'>
b = 10.1
print(type(b))
# <class 'float'>
c = 10+10j
print(type(c))
# <class 'complex'>
sh = 'shanmukh'
print(sh)
# shanmukh
print(type(sh))
# <class 'str'>
d = "shanmukha"
print(sh)  # shanmukh
print(type(d))
# <class 'str'>
li = [1,2,3,4,5,6]
print(li)
[1, 2, 3, 4, 5, 6]
print(type(li))
# <class 'list'>
tu = (1,2,3,4,5,6)
print(tu)
(1, 2, 3, 4, 5, 6)
print(type(tu))
# <class 'tuple'>
# list is a mutable and it is hetroginious but whereas the tuple is immutable and also non hetrogenius
s = {1,2,3,4,1,1,4,3,5}    #unordered   #mutable    #dosen't allow duplicates
s1 = set()          #constructor
print(type(s))      #set

fs = frozenset({2,5,6,6})   #immutable
print(type(fs))     #frozenset

d = {'name':'Shanmukh' , 'course' : 'DA'} # key : value #ordered #key=immutable #value:mutable
print(type(d))      #dist

lockstatus = True
print(type(lockstatus))     #boolean
bestseller = False
print(type(bestseller))     #boolean

randomvar = None
print(type(randomvar))     #Nonetype
