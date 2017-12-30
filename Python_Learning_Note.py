"""
# I installed local python and anaconda. After add "python.exe" and "anaconda/Script" path to the system,both can be
# interpreter for the project
# (For Windows, right click My Computer->Properties, Go to Advanced System setting -> Environment Variables and
# add append path to the "PATH" in system variables)
"""
"""
# know the preserved keyword
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except'
# , 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise'
# , 'return', 'try', 'while', 'with', 'yield']
"""
import keyword

print(keyword.kwlist)

# we use back slash to do a line break
a = 1 + 1 + \
    2 + 2 + \
    3 + 3
print("\na equals to ", a)
del a;

"""
# double quotation mark and single quotation mark serves as equal in Python
# triple quotes can contain line break and is usually used as document express
# escape character is '\'
"""

word = 'word'
sentence = "sentence"
paragraph = """triple quotes can contain 
line break"""


def foo():
    """This function is a foo"""
    pass


help(foo)
print(paragraph)

# input syntax: input("prompt")
temp = input("press enter to show something")
if temp == "":
    print('You press the right key')
else:
    print('You pressed something else before hit enter')
del temp

"""
# print() in default will move to next line, by using 'end = "" ' as second parameter can solve this
# 'end = ' means you can decide what character as a delimiter
"""
print("print with new line")
print("print without new line", end='')
print("print something")

"""
# a useful Python print characteristics
"""
print('.' * 10)

"""
# import & from ... import:
# import whole module
# from ... import import several particular methods. Using wildcard character, it import all methods
"""

import sys

for i in sys.argv:
    print(i)
print('the path of python is ', sys.path)

from sys import path

print('the path of python is', path)

from sys import *

"""
# several command line syntax
# $ python -h
# usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
# Options and arguments (and corresponding environment variables):
# -c cmd : program passed in as string (terminates option list)
# -d     : debug output from parser (also PYTHONDEBUG=x)
# -E     : ignore environment variables (such as PYTHONPATH)
# -h     : print this help message and exit
#
# [ etc. ]
"""

"""
# In Python, Variables can be used without clarification. And variables can be assign value in one line
"""
a = b = c = 1
d, e, f = 1, 2.0, '3'

"""
# There are 6 build in types: numerics, sequences, mappings, classes, instances and exceptions
# Numeric Types: int, float , complex
"""
a = 1
print(isinstance(a, int))

"""
# Comparing isinstance & type
# isinstance function in the same as instanceof in JAVA, it treats the subclass as a kind of superclass
# type, on the other hand, does not use polymorphism. It returns true only when variable is exactly a certain type
"""


class ATestOnly():
    pass


class BTestOnly(ATestOnly):
    pass


print("isinstance test result: ", isinstance(BTestOnly(), ATestOnly))
print("type test result: ", type(BTestOnly()) == ATestOnly)

"""
# now introduce sequence types: string, list, tuple
# Python String
"""

string_for_test = 'Michael Pan'
print(string_for_test[0:-1])  # print from the first string to the second-to-last character
print(string_for_test[3:])  # print all chars started from the 4th char
print(string_for_test * 2)  # print a string in several times
print(string_for_test + " concatenate strings")  # concatenate string by using + operand, just as in Java
del string_for_test

"""
# Python escape character '\'
# another alternative is 'r'
"""
print(r'Michael\pan')
print('Michael\\pan')

"""
# Python List data structure is very interesting and powerful.
# I see it as ArrayList<Object>, but more flexible
"""
list_for_test = [1, 2.0, 'Michael Pan', 1 + 2j]
list_for_test2 = [123, '123']
print('', list_for_test[1:3])  # !!!!!!!!!!!!!notice. it will return 2nd char to the 3rd. [start,end), end exclusive
print('list_for_test[2:-2] ', list_for_test[2:-2])  # same as String

list_for_test[2:-2] = []  # eye-catching feature, you can control the list in almost anyway!
print('eye-catching feature: set part of the list as null', list_for_test)
del list_for_test, list_for_test2

"""
# Python Tuple is used exactly like ArrayList<Object>. It has more rigid constrains (immutable)
# String can be seen as a subset instance of tuple
"""
list_for_test = [2, 3.0]
tuple_for_test = (1, 2.0, 'string', list_for_test)  # tuple can contain list which is mutable
print('tuple test: ', tuple_for_test[3:])
del list_for_test, tuple_for_test

"""
# Python set stores the unique value of objects with no order. Just as the Set in JAVA
# create a set using such syntax: reference = set(...) or reference = {...}
# Notice! empty set must be created by using set(). Because {} is used for create empty dictionary
student = {'Mike', 'Zed', 'Lucas', "Zoe", 'Mike', 'mike'}  # duplicate value will be automatically removed
"""

print('set print: ', student)
if 'Rose' in student:
    print('Rose is in the set')
else:
    print('Rose is not in the set')
del student

a = set('abracadabra')
b = set('alacazam')
print('a ', a, '\nb', b)
print('a-b ', a - b)  # return 'a' set after deduct common elements in 'b' set
print('a | b ', a | b)  # return a∪b
print('a & b ', a & b)  # return a∩b
print('a^b ', a ^ b)  # return all elements that are not exist in both sets
del a, b

"""
# Python dictionary stores key-value sets. Just like the map in JAVA
# Empty dictionary should be represented as  {}
"""

dict_for_test = {}
dict_for_test['one'] = "The value pairs with key 'one'"
dict_for_test[2] = "The value pairs with key '2'"
dict_for_test2 = {'key1': 'value1', 'key2': 'value2', 3: 'value3', 4: 4}
print('dict_for_test[\'one\'] ', dict_for_test['one'])
print('dict_for_test[2] ', dict_for_test[2])
print('dict_for_test2 ', dict_for_test2)
print(dict_for_test2.keys())
print(dict_for_test2.values())

# dictionary constructor also take sequence as construction parameters
dict_for_test3 = dict([('Key1', 1), ('key2', 2)])
print(dict_for_test3)
del dict_for_test, dict_for_test2, dict_for_test3

""" casting in Python
int(x [,base])
float(x)
complex(real [,imag])
str(x)
repr(x)
eval(str)
tuple(seq)
list(seq)
set(seq)
dict(d)
frozenset(iterable)
chr(x) x is a number
ord(x) x is a char
hex(x) x is an integer based on 10, convert num based on 10 to base of 16
oct(x) X is an integer based on 10, convert num based on 10 to base of 8
"""

print(int('0x12', 0))  # we tell the int function to read the prefix by enter base = 0
print(int('12', 16))  # or we directly assign particular base in the function
print(int(1.2))
print(int('12'))  # By default, the base is 10

print(float('123'))  # similar to int(x,base)
print(float(123))

print(complex(1))
print(complex(1, 2))

print(str([1, 2, 3]))  # str(Object) can transfer any object to string
print(repr([1, 2, 3]))  # repr(Object) can also transfer any object to string
# What's the difference between str() and repr?
# str() is used to make object readable for end users!
# repr() is used to reproduce object for developer!
# the result from repr() can be interpreted by eval(str) while str() can't

print("str(\"srt() String Test\")", str("srt() String Test"))
print("repr(\"repr() String Test\")", repr("repr() String Test"))
print("eval(repr(\"repr() String Test\"))", eval(repr("repr() String Test")))

print('eval(str) result: ', eval("1+1"))  # eval(str) can evaluate expression expressed in String

print(tuple(['Google', "Taobao", "Ali", "Baidu"]))  # convert any sequence in tuple
# for the dictionary, it will convert it to 2 arrays
# {1: 'Google', 2: "Taobao", 3: "Ali", 4: "Baidu"} -> ('Google', 'Taobao', 'Ali', 'Baidu') & (1, 2, 3, 4)
print("tuple(Dictionary) result: ", tuple({1: 'Google', 2: "Taobao", 3: "Ali", 4: "Baidu"}))

# list performs slightly different from tuple, it will only take keys from the dictionary and dump all values
print("list(Dictionary) result: ", list({1: 'Google', 2: "Taobao", 3: "Ali", 4: "Baidu"}))

# set will automatically remove duplicate chars and return a set with random order
# as the list, set will take Key only and ignore the Values
print('normal set() usage', set('ruuuuuuuumor'))
print('set(Dictionary) result: ', {1: '1', 2: '2'})

# three different ways of using dictionary()
print("dict(a='a',b='b',c='c') ", dict(a='a', b='b', c='c'))
print("dict(ZIP(['one','two','three'],[1,2,3]))", dict(zip(['one', 'two', 'three'], [1, 2, 3])))
print("dict([('one', 1), ('two', 2), ('three', 3)])", dict([('one', 1), ('two', 2), ('three', 3)]))

# frozenset([iterable]) returns a immutable set (as immutable as tuple ⚆_⚆!)
print('frozenset(range(10)) result: ', frozenset(range(10)))

# all other casting
print("chr(0x30) ", chr(0x30))
print("chr(48) ", chr(48))
print("ord('a')", ord('a'))
print("chr(ord('b'))", chr(ord('b')))
print("hex(10)", hex(10))
print("oct(10)", oct(10))
