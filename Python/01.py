# data types in python and variable declaration
# a = 10 # int 
# a = 10.5 # float
# a = "Hello" # string
# a = True  # boolean variable declaration 
# a = [1, 2, 3, 4] # list
# print(type(a))  # print the type of variable a

#------------

# conditions (if , else, elif)
# a = 10
# b = 20 
# c = 30
# if a > b and a > c:
#     print("a is the greatest")
# elif b > a and b > c:
#     print("b is the greatest")
# else:
#     print("c is the greatest")


#--------------

# loops (for, while)

# to print the name 5 times using for loop
# name = 'benny' 
# for i in range(5):
#     print(name)

# to print the numbers from 1 to 10 using for loop

# for i in range (1, 11): # why (1, 11) range is exclusive of the last number, so to include 10 we use 11 its index concept
#     print(i)

# to print fruits in the list using for loop
# fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# for fruit in fruits:
#     print(fruit)

# while loop  -> keeps running until the condition is true 


#to print the numbers from 1 to 5 using while loop
# count = 1

# while count <= 5:
#     print (count)
#     count += 1  # increment the count by 1 // why? to stop the loop after the condition met, if we dont loop contionues forever


# function

# def add( a, b):
#     print(a +b)


# add(5, 10)

# data structures

# list -> []
# tuple -> ()
# set {}
# dictionary {key : value}


# a = [1, 2, 3, 4]
# print(type(a)) # list
# print(a[0]) # 1
# print(a)
# a.append(5) # adding 5 to the list
# print(a)

# a = (1, 2, 3, 4)
# print(type(a)) # tuple
# print(a[0]) # 1
# print(a)
# a.append(5) # this will fail since tuple is immutable

# a = {1, 2, 3, 3, 4}
# print(type(a)) # set
# # print(a[0]) # 1 this will fail since set is unordered and does not support indexing
# print(a)
# a.add(5) # adding 5 to the set / set doesnt support append and some other methods that list supports
# print(a)

# a = {1:1, 2:2, 3:3, 4:4}
# print(type(a)) # dictionary
# print(a[1]) # for dict we use the key to access the value and not the index
# print(a)
# a[5] = 5 # adding 5 to the dictionary
# print(a)


# -----------
# index

# a = {1:1, 2:2, 3:3, 4:4, 5:5}
# print(a[1], a[2])
# print(a)
# print(a[1]) # for dict we use the key to access the value and not the index

# ----------------
# slicing
# a = [1, 2, 3, 4, 5]
# print(a[1:5:2]) # silicing with step the 3rd part define the step size like jumping 2 elements at a time
# print(a[::-1]) # slicing with negative step size to reverse the list
# print(a[1:2]) # slicing
# print(a[1]) # indexing

# reverse string

# b = 'hello benny!'
# print(b[::-1]) # reverse the string

# ------------------------
# adding changing elements in list, tuple, set, dictionary

# a = ['apple', 'banana', 'cherry']
# print(a)
# a[1] = 'blueberry'  # changing the second element / list / mutable / can change the elements
# print(a)

# ---------------


# a = ('apple', 'banana', 'cherry')
# print(a)
# a[1] = 'blueberry'  # changing the second element / tuple / immutable / cannot change the elements
# print(a)

# ----------------

# adding changing elements in list items using methods

# a = ['apple', 'banana', 'cherry']
# print(a)
# a[1] = 'blueberry' # changng using indexing  
# print(a)
# a.append('orange') # adding using append method
# print(a)
# a.insert(1, 'kiwi') # adding using insert method / in specifc position 
# print(a)
# a.remove('cherry') # removing using remove method
# print(a)
# a.pop(1) # removing using pop method / removes the last element / can also remove the element at specific index by passing the index as argument
# print(a)
# # a.clear() # removing all the elements from the list
# # print(a)
# a.sort() # sorting the list in ascending order
# print(a)

# -----------

# operators in python

# arithmetic operators

# + add a + b
# - subtract a - b  
# * multiply a * b
# / divide a / b    
# // floor division a // b
# % modulus a % b
# ** exponent a ** b

# relational operators

# a == b  # equal to
# a != b  # not equal to    
# a > b   # greater than
# a < b   # less than
# a >= b  # greater than or equal to
# a <= b  # less than or equal to

# logical operators

# and  a and b
# or   a or b
# not  not a

# assignment operators

# =   a = b
# +=  a += b  # a = a + b
# -=  a -= b  # a = a - b
# *=  a *= b  # a = a * b
# /=  a /= b  # a = a / b
# %=  a %= b  # a = a % b
# **= a **= b # a = a ** b

# bitwise operators

# &   a & b
# |   a | b  / its used to set the bits of a number to 1 if either of the bits is 1
# ^   a ^ b  / its used to set the bits of a number to 1 if either of the bits is 1 but not both
# ~   ~a     / its used to invert the bits of a number
# <<  a << b  / its used to shift the bits of a number to the left by b positions
# >>  a >> b  / its used to shift the bits of a number to the right by b positions

# membership operators

# in      a in b  / its used to check if a is present in b
# not in  a not in b  / its used to check if a is not present

# identity operators

# is      a is b  / its used to check if a and b are the same object
# is not  a is not b  / its used to check if a and b are not the same object

# ---------
# inputs() - built in function to take input from user

# name = input("Enter your name: ")
# print("Hello, " + name + "!")


# ---------
# data type conversion
# changing the one data type to another data type

# int() - converts to integer
# float() - converts to float
# str() - converts to string
# list() - converts to list
# tuple() - converts to tuple
# set() - converts to set
# dict() - converts to dictionary
# bool() - converts to boolean

# a = "10"
# print(type(a)) # string
# a = int(a)
# print(type(a)) # int

# ----------------

# string handling

# working or changing the string using methods like upper(), lower(), strip(), replace(), split(), join(), find(), index(), count(), isalpha(), isdigit(), isspace(), startswith(), endswith()

# x = "Hello, World!"
# print(x.upper()) # convert to uppercase
# print(x.lower()) # convert to lowercase
# print(x.strip()) # remove whitespace from the beginning and end
# print(x.replace("H", "J")) # replace H with J
# print(x.split(",")) # split the string into a list
# print(x.join("Python")) # join the string with another string
# print(x.find("World")) # find the index of World
# print(x.index("World")) # find the index of World
# print(x.count("l")) # count the occurrences of "l"
# print(x.isalpha()) # check if all characters are alphabetic
# print(x.isdigit()) # check if all characters are digits
# print(x.isspace()) # check if all characters are whitespace
# print(x.startswith("Hello")) # check if the string starts with "Hello"
# print(x.endswith("World!")) # check if the string ends with "World!"

# -----------------

# lambda function

# this is normal function
# def add(x, y):  # here add is the function name and x, y are the parameters
#     return x + y # return statement is used to return the value of the function
# a = add(5, 10)  # here 5 and 10 are the arguments passed to the function
# print(a) # 15

#  lambda fucntion is quick one line fucntion without using def keyword and return statement

# add = lambda x,y: x + y
# a = add(100, 500)
# print(a) # 600

# one eg using result for def, return and result for lambda function

# def square(x):
#     return x * x

# a = square(5)
# print(a) # 25

# result = lambda x: x * x
# b = result(5)
# print(b) # 25

# ----------------

# comprehension
# take the exists collection > aplly to new logic > create new collection
# used for data transformation and filtering

# types list / set / dictionary comprehension

# eg of list comprehension
# data transformation using list comprehension
# a = [1, 2, 3, 4, 5]
# squared = [x**2 for x in a]
# print(squared) # [1, 4, 9, 16, 25]

# data filtering using list comprehension
# squared_even = [x**2 for x in a if x % 2 == 0]
# print(squared_even) # [4, 16]

# set comprehension
# squared_set = {x**2 for x in a}
# print(squared_set) # {1, 4, 9, 16, 25}

# dictionary comprehension
# squared_dict = {x: x**2 for x in a}

# ---------
# exception handling
# handling the errors in the code using try, except, finally, else

# x = 10
# y = 0
# print(x/y) # this will raise a ZeroDivisionError

#  try and except

# try:                # code that might cause an error
#     x = 10
#     y = 0
#     print(x/y)
# except:              # handle the error
#     print("something went wrong!")

# try / except / else / finally

# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num

# except ValueError:
#     print("Please enter a valid number")

# except ZeroDivisionError:
#     print("You cannot divide by zero")

# else:
#     print("Result:", result)

# finally:
#     print("Program finished")

# ------------
# file handling
# open() - open a file 
# read() - read from file 
# write() - write form file 
# close() - close the file 
# with - create a block where py automatically close the file 

# modes
# r - read 
# w - write 
# a - add / append 
# x - crearte a  new file 

# =-------------
# modules and packages 

# import module name 
# eg import math 
#    print(math.sqrt(25))

# from ... import ... 
# eg  from math import sqrt 
#     print(sqrt(25))

# to install packages 
# pip install requests 

# to access those packages
# import requests

# --------------------
# csv commma seprate values

# import csv 
# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# -------------
# # json - javascript object notation

# import json
# with open('data.json', 'r') as file:
#     data = json.load(file)
#     print(data["name"])

# ---------------

# json parsing / converting json data into something py can work with
# imporartant functions
# json.loads() - json str > py obj
# json.load() - json file > py obj
# json.dumps() - py obj > json str
# json.dump() - py obj > json file

# --------------

# iterator / something we use to take values one by one
# a = [1, 2, 3]
# it = iter(a)
# print(next(it))
# print(next(it))
# print(next(it))

# -------------------

# generator / easy way to create iterator

# def num():
#     yield 10
#     yield 20
#     yield 30 
#     yield 40
#     yield 50
# g = num()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# --------------------
# processing tools collections

# processing tools collections

# # lmabda / smalll one line function / 
# # eg 
# square = lambda X: X ** 2

# print(square(5))


# # map() / apply something to every item
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x ** 2, numbers))
# print(squared)

# # filter() / keeps the item that statisfy the conditions
# numbers = [1, 2, 3, 4, 5]
# even = list(filter(lambda x: x % 2 == 0, numbers))
# print(even)

# ----------------
# api / json 
# api / a way for application to communicate to another 
# json / common format to send or recive data
# request / asking for something 
# response / something we get!


# -------------------
# indexing in numpy 
# import numpy as np
# x = np.array([1, 2, 3, 4])
# print(x[1]) # output is 2 

# # shape 
# import numpy as np
# x = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]])
# print(x.shape) # output is (2, 4)

# # ndim / tells how many dimension
# import numpy as np
# x = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]])
# print(x.ndim) # output is 2 

# # dtpye / tells what type of data array contains 
# import numpy as np
# x = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8]])
# print(x.dtype)

# # np.where / filtering concept / find the value based on the condition
# import numpy as np
# x = np.array([10, 20, 30, 40, 50])
# np.where(x > 20)
# indices = np.where(x > 20)
# print(x[indices])  # output is [30 40 50]

# # random / generate random numbers 
# import numpy as np
# x = np.array([10, 20, 30, 40, 50])
# np.random.randint(5 , 15, size = 5) # output is array([ 7,  8, 14,  5,  9])

