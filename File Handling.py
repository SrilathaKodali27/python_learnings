# what is file handling?
# handling certain file which is not python
# pdf,xcel,json--etc
# to handle the file in python we require a inbuilt function which is "open function"
# while your handling the file we will be having 4 modes.
# Modes:- r, a, w, x
# x-mode---> it is used to create a new file.
# f = open('trail.txt','x')
#w-mode--> over write mode
'''f = open('trail.txt','w')
f.write("i am applying write mode to my file,"
        "if i write one more time my content can be overwritten")
f.close()'''
# import xlrd

#r---> read mode ---> to read the content in file
#by default when you use the open function it is in read mode

# f = open('trail.txt','r')
# print(f.read())
# f.close()

#write mode:-
"""f = open('trail.txt','w')
f.write("i am over writing my content in the file "
        "so the previous content can be over written ")
f.close()"""

# a-mode--->append mode
"""f = open('trail.txt','a')
f.write("i am adding extra content at the end of the existing content")
f.close()"""
#read the file
"""f = open("trail.txt")
print(f.read())
f.close()"""


#========================================================================================================
#05-08-2024
#to read excel file use "xlrd" library
#what is xlrd?
"""xlrd is a library for reading data and formatting information from Excel file.
it supports .xls format only"""

"""loc = "C:\\Users\\srila\\OneDrive\\Desktop\\Python\\Financial Sample (1).xls"
# use xlrd.open_workbook to read the xls file
wb = xlrd.open_workbook(loc)
#how to acess the particular sheet data?
sheet = wb.sheet_by_index(0)

#read data sell wise
# i want to know how many rows and columns in given file?
print(sheet.nrows)
print(sheet.ncols)

#reed the particular cell
#cell_value(row,co)
#indexing can be starts from zero
print(sheet.cell_value(7,2)) # 7th row second column
#print entire rows
print(sheet.row_values(0))
print(sheet.col_values((1)))
#extract all the data in console

for x in range(sheet.nrows):
        print(sheet.row_values(x))"""

#ITERATORS:
#what is iterators?
#iterators help you to take large bunch of data in limited memory space.
# means it breaks the large data in to tiny chunks.
# in iterators we are having 2 protocols
#1. __iter__()
#2.__next__()
l = ['apple','banana','watermelom','kiwi','orange']
'''for x in l:
        #x is iter over each and every element in collection.
        print(x)'''
"""x = iter(l)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))"""

"""class Number:
    def __iter__(self):
        self.intial = 0
        return self
    def __next__(self):
        if self.intial <= 5:
            x = self.intial
            self.intial += 1 #self.intial + 1  increasing loops with 1
            return  x
        else:
            StopIteration("are you stupid")

n = Number()
# for x in n:
#     print(x)
x = iter(n)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))"""
#generators
#pip package
#pickling
#connecting with you mysql by using python
#python json

#generators:

"""A generators is a function that returns an iterator that produce a sequence of values when iterated over."""
#when we have to use those generators?
"""generators are use when we want to produce large sequence of values,we don't want to store all
of them in the memory at once"""
# use "def",instead of "return" use "yield"
"""def my_generator(n):
    value = 0
    #loop until counter is less than n
    while value < n:
        yield value
        value += 1
    #iterate over your generator to generate sequence
for value in my_generator(9):
        print(value)"""

"""Note: when your using integer directly in to for loop it throws an error use it with range function
when your using generators then use yield,it supports int object in for loop"""

#picking:
"""the process of converting any type of object in python
for example (list,tuple,set etc ) on to bytes is known as pickling"""
"""when it comes to python these pickling conversion is known as "serialisation","deserialisation"."""

#what is bytes?
#0's and 1's is known as bytes
#to do the pickling use package called "pickle"
# import pickle
#conversion of 2D data format to 1D data and store it - serialisation
#and in same time conversion 1D data in to 2D is known as pickling - deserialisation
"""
#open a pickle file.txt
pickle_file = open("pickle2.txt","wb")     #wb =work byte
#usage pickle.dump to dump the file
my_dict = "C:\\Pycham Projects\\pickle2.txt"
pickle.dump(my_dict,pickle_file)
#pickle.dump(collection_name,pickle_file(where you want to store the data)
#in the above step you dump the data into serialisation
pickle_file = open("pickle2.txt",'rb')
#load the data that you have stored
new_dict = pickle.load(pickle_file)
print(new_dict)
"""

# step1 - import pickle library
# step 2  - creating a pickle file in "wb"
# step 3 - use "pickle.dump" to convert the data
# step 4 - read the actual data by using "open(pickle filename","rb")
# step 5 - after that load the data load into new_file
# step 6 - print the file

#======================================07-08-2034
#python pip :- is basically a package manager for python package or  module
#what is package?
#package is basically something that contains all the files you needed.
#so packages contains all the files you need for certain modules.
#what is module?
#modules are code libraries which you can include in your project
#Numpy
#pandas
#matplotlib and seaborn
#pendulum
#python image processing
#movie py
#tkinter
#pygt
#py32
#py test

#how to install this packages?
"""py -m pip install "package name" when you use CMD"""
"""!pip install "package name"--> colab notebook and jupyter notebook"""
#what is global package and what is local package?
import camelcase
x = camelcase.CamelCase()
a = "hi there!this is the message to check each word of letter are capitalisation"
print(x.hump(a))
#how to uninstall package in cmd?
#py -m uninstall "package name"
#how to check how many packages are there in your system.
#py -m pip list
#how to upgrade your pip?
#pip -m pip install---ugrade pip
#how to check the version of your pip?
#py -m pip --version
#========Json===
#java script object notation
#it is basically a syntax that storing and exchanging the data.

"""{"first_name":"srilatha,
    "last_name":"kodali",
    address :{street: ramp center,
                "city":"eluru"}"""

import json
#what is parse?
"""it is a method where one string of data is converting in to another form of data"""
person = {'name':"andrew",
          'language':['english','french']}
print(type(person))
#convert this in to json format

person_dict = json.dumps(person)
print(person_dict)
print(type(person_dict))

#lets open json file by using "with open"
loc = "C:\\Users\\srila\\Downloads\\example_1.json"
with open(loc) as f:
    data = json.load(f)
print(data)
print(type(data))