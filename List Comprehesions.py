#List Comprehesions:-

"""it offers you the smaller line of code that you can create a new list from the existing list"""
import array

"""list_fruits = ["Apple","Banana","pineapple","mango","kiwi"]
#print the fruits with letter "A" in it and store it in new list
list = []
for x in  list_fruits:
    if "A" in x:
        list.append(x)
print(list)

"""

"""list_fruits = ["Apple","Banana","pineapple","mango","kiwi"]
#new_list = [items(i) for items(i) in "collection_name"]
new_list =[x for x in list_fruits if "e" in x]
print(new_list)"""

# #print the new_list without "Banana" from the existing list_fruits.
# list_fruits = ["Apple","Banana","pineapple","mango","kiwi"]
# new_list = [x for x in list_fruits if x != "Banana"]
# print(new_list)


# create list of numbers from 0 to 20?
"""num = []
for x in range(21):
    num.append(x)
print(num)
"""

"""n = [x for x in range(21)]
print(n)"""

# even numbers
'''num = [x for x in range(21) if x%2 == 0]
print(num)'''

# odd numbers

'''num = [x for x in range(21) if x%2 != 0]
print(num)'''

# Note : so LC can offer shorter syntax and also it is time efficient

# create a new_list of numbers in range of 20 the output must be in multiple of 2 by using Lc?
# Note Syntax : new_list = [items(i) for items(i) in "collection name"
'''num = [x * 2 for x in range(21)]
print(num)'''

# lambda, filter, Map

# lambda()
# what is lamda()?
# lambda is a anonymous function
# "anonymous function" means this function doesn't have name.
'''def f1(X):
    return X
print(10)'''

# syntax for lambda function():- "lamda arguments:expression"
#so lambda is an anonymous function it can have many arguments and single expression.
#what is an expression?
#expression is some kind of statement/calculation/step using that values to give single value
#lambda is an anonymous function how can you call it.
#we generally use this function  where it has some name.
#means we can create a variable to call this function.

"""x = lambda a: a+10
#where your calling the lamda function use the variable name
print(x(5))"""
"""
x = lambda a,b,c : a + b + c
print(x(5,6,7))"""

#when we use lambda function?
#create function that can give square of every number?

"""def square(x):
    return x ** 2
def cube(x):
    return  x ** 3
def four(x):
    return  x ** 4
def sqrt(x):
    return x ** 0.5
print(square(4))
print(cube(4))
print(four(4))
print(sqrt(4))"""

"""def power(n):
    return lambda a: a ** n
square = power(2)
cube = power(3)
print(square(6))
print(cube(3))"""

#similarly try the lambda function for the multiplication.
#global and local variable
#global variable is a variable thet can create outside the function
#you can access the global variable and it is a permanent

"""x = "amazing"
def f():
    return x
print(x)"""


#what is local variable?
#creating variable inside the function is known as local variable.
"""
def f():
    x = "fantastic"
    return x
print(f())
print(x)"""

""":- even the variables names are same the local variables never affect the global varaibles """

#Map():
#what map does?
#it uses a function on iterabes.
#what is iterables?
#list,tuple,dict,set,array.
# map will take an function and run it over the iterables.
"""Functions are the 1st class objects which means one function can act as an argument for another function"""
#syntax :- Map = (function,iterables)

#a = ['apples','bananas','cherries','pineapple']
"""length =[]
for i in a :
    length.append(len(i))
print(length)"""

# do same thing using LC
'''l = [len(i) for i in a]
print(l)'''

# a = ['apples','bananas','cherries','pineapple']
"""if you want to display the output by using the map function we need to decide in which iterables(list,tuple,set) the output has tober"""
"""length = tuple(map(len,a))
print(length)"""

# def f1(x):
#     return "Hello " + x
#print(f1("apples"))

#apply the function for each item in the collection.
# l = list(map(f1,a))
# print(l)
# #when we have to use the map function?
#when we are having multiple user input collection then we can use the map function
'''user = input().split()
print(user)
print(type(user))'''

"""31-07-2024"""
#take a set of numbers being seprated with the spaces
'''user = input().split()
print(user)
print(type(user))
'''
#how to convert this string of elements in list to integers?
'''user = input().split()
print(user)
print(type(user))
number = []
for x in user:
    number.append(int(x))
print(number)
print(type(number))'''

#user = input().split()
'''number = set(map(int,input().split()))
print(number)'''

#note:- before executing the map() we need to decide in what type of solution,do we need
#how can we print the following 10 20 30 40 50 in double that to in tuple?
#lambda:- you can have many arguments but single expression

'''double = tuple(map(lambda a : a * 2, number))
print(double)
'''
'''double = tuple(map(lambda a : a * 2, map(int,input().split())))
print(double)'''

"""map(int,input().split())---> map storing entire thing/data, if we want it to be in a 
readable need to add "tuple","list","set"."""
# =======================================================================

"""filter() ---> collection_name(filter(function,iterable))
filter gives output of the collection if the condition is true"""
# age = [18,48,31,24,16,56,35,45,12,14,10,20]
"""def adult(x):
    if x >= 18:
        return x
f1 = list(filter(adult,age))
print(f1)
"""
"""f1 =list(filter(lambda a: a >= 18 and a <= 30 ,age))
print(f1)

f1 =list(filter(lambda a: 18<=a<=30,age))
print(f1)"""
"""so filter basically filters your original collections that returns
 true or false, any value that comes out to be true that original value can be stored
 as a collection(list,tuple,set) of items"""
#regular expressions: it is a build in pacakage which is known as "re"
#A RegEx, or regular expressions is a sequance of characters that forms a search patterns
# import re
# txt = "hello world"
# #search weather world is present or not
# x = re.search("world$",txt)
# print(x)
#regular expression function
#findall()--->returns a list containing all matches
#search--->returns match object
#split---> return a list
#sub---> replace one or many objects with the string













