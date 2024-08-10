# Classes and Objects
#why we are creating classes and objects?

#how to create a class?
# to create a class we are using keyword called "Class"

"""class customer:
    pass
#object creation
c1 = customer()
print(c1)"""
#pass will used to define the class


#what is __main__?
#main is nothing but a file where the class is comes from

"""Attributes:- these are two types
1.class attribute:- come from class and there attributes accessible by every object(common attributes)
2.object attribute :- means unique attributes that can be applicable to particular object"""

# class customer():
# #create class attributes:  creating varibles inside the class
#     Bank_Name = "HDFC Bank"
#     Branch = "Mumbai"
#     State = "Maharastra"
#     IFSC = "HDFC000023"
# c1 = customer()
# c2 = customer()
# #how can an object access the  class attribute?
# print(c1.Bank_Name,c1.IFSC)
# print(c2.State)

#create methods for class customer
#what is methods?
#methods can be created inside the class
#methods are nothing but creating functions inside the class


class customer():
    #create class attributes:  creating varibles inside the class
    Bank_Name = "HDFC Bank"
    Branch = "Mumbai"
    State = "Maharastra"
    IFSC = "HDFC000023"
    #before creating the object attributes we need to initiate object attributes inside the class
    def __init__(self,name,age,intial_amount,acc_No):
        #what is __init__?
        """when you creating an object by default it runs with init
            method-----> initialisation method"""
        self.name = name
        self.age = age
        self.intial_amount = intial_amount
        self.acc_No = acc_No

    #creating methods
    def welcome(self):
        print(f"Hello {self.name} and welcome to {self.Bank_Name},{self.Branch}")
    def check_balance(self):
        print(f"your current balance is {self.intial_amount}")
    def deposit(self,amount):
        self.intial_amount += amount #- --> initial_amount + amount
        print(f"Transaction is completed." 
              f'{amount} has been credited to your {self.acc_No}.'
              f'The updated balance is {self.intial_amount}')
    def withdraw(self,amount):
        if amount <= self.intial_amount:
        # self.intial_amount += amount  # - --> initial_amount + amount
            print(f"Transaction is completed." 
              f'{amount} has been deduct from your {self.acc_No}.'
              f'The updated balance is {self.acc_No}')
        else:
            print("insuffient balance")
            self.check_balance()

#create a object
c1 = customer("python",28,10000,123456789)
c2 = customer("python",28,10000,123456789)

#how to access the particlar methods
# c1.welcome()
# c1.check_balance()
c1.deposit(100000)
c2.withdraw(1000)
# c2.welcome()
#class.method(object)
#how can an object access the  c'lass attribute?
# print(c1.Bank_Name,c1.IFSC)
# print(c2.State)

#how can an object access object attributes
# print(c1.intial_amount)

# self --> self is an extra parameter in the method defination
#self act as  a pointer/reference to access the object

x = "hello"
x.upper()


#step 1 ---> create  a class ---> customer --->bank
#step 2 ----> created a object by using varaibles for ex --> c1 = customer()
#step 3 ----> creating class attribute inside the class ----> these are common attributes
#step 4 ----> how to access class attributes by particular object ---->print(c1.Bank_Name)
#step 5 ----> created methods inside the class which are nothing but functions inside class
"""ex:- welcome(),check_balance(),deposit(),withdraw()"""
#step 6----> how to access particular method by particular object ---> c1.welcome(),c1.deposit()



#class
#object
#method
#inheritence :- The childs object can acquire all the properties and behaviour of parent object
#polymorphism :- one task can be performed in many ways.
#data abstraction:- data abstraction and encapsulation both are like  synonyms
#encapsulation:-