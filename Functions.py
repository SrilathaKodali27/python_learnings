#Functions:
"""Create a sum()  so it can take 2 arguments to do sum """
'''def sum(d1,d2):
    print(d1+d2)
d1 = int(input("Enter your number :"))
d2 = int(input("Enter your number :"))
sum(d1,d2)
'''
#write a python function to sum all the numbers in a list
#sample list : [8,2,3,0,7]
#expected: 20
'''
def sum(numbers):
    total = 0
    for x in numbers:
        total = total + x
    print(total)
numbers = [8,2,3,0,7]
sum(numbers)'''

# write a function to multiply all the elements in the collection
# write a python function to print even numbers from given list
#sample list = [1,2,3,4,5,6,7,8,9]
#expected = [2,4,6,8]
'''
def even(numbers):
    total = 1
    for x in numbers:
        total = numbers % 2 == 0
    print(total)
numbers = [1,2,3,4,5,6,7,8,9]
even(numbers)'''


'''def multi(numbers):
    total = 1 #local variable means it is created inside the function
    for x in numbers:
        total = total*x
    print(total)
numbers=[2,3,4]
multi(numbers)'''

#write a function that converts a decimal number in to binary number

'''def dectobin(num):
    if num>1:
        dectobin(num//2)
    print(num % 2 , end= "")
num = 11
dectobin(num)'''

# sum = 10  #global variable means it will created outside of the function
# def f1(x):
#     return x + sum
# print(f1(5))


"""Return:- return is a special keyword that you can use inside  function or method to send the function results back to the caller."""
# type("hello")
# len("hello")

"""def f1(x)
    print(x)
f1(10)"""

# def f2(x):
#     return x
# print(f2(10))

#what is the purpose of return?
"""when you return the value you can decide what you gonna do with value"""
# x = len(input("enter the string: "))
# print(x ** 2)

'''def f1(x):
    return x
print(f1(10))#--> 10
#print(f1(10)) #None
#why we getting none?'''
"""when i use print(x) and given the argument f1(10) the 10 will gets to the f(x) place an first prints the 10"""

"""sum = 10
def fun_sum(x):
     a = x + sum
     return a
print(fun_sum(100))"""

#write a program to print sum of range of numbers.
#samole input :- 7
#sample output :- 28

"""Num = int(input("Enter your number : "))
sum = 0
for i in range(0,Num+1):
     sum = sum + i
print(sum)"""




