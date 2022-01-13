# Types of Variables:
# 1. Instance Variables (Object Level Variables)
# 2. Static Variables (Class Level Variables)
# 3. Local variables (Method Level Variables)


# Inside Constructor by using self variable:
# class Employee:
#     def __init__(self): 
#         self.eno=100 
#         self.ename='Durga'
#         self.esal=10000
# e=Employee()
# print(e.__dict__)


# Inside Instance Method by using self variable:
# class Test:
#     def __init__(self): 
#         self.a=10 
#         self.b=20 

#     def m1(self): 
#         self.c=30 

# t=Test() 
# t.m1() 
# print(t.__dict__) 


# Outside of the class by using object reference variable:
# class Test:
#     def __init__(self): 
#         self.a=10 
#         self.b=20 

#     def m1(self): 
#         self.c=30 

# t=Test() 
# t.m1() 
# t.d=40 
# print(t.__dict__) 

# How to access Instance variables:
# class Test:
#     def __init__(self): 
#         self.a=10 
#         self.b=20 

#     def display(self): 
#         print(self.a) 
#         print(self.b) 

# t=Test()
# t.display() 
# print(t.a,t.b)


# How to delete instance variable from the object:
# 1. Within a class we can delete instance variable as follows
#  del self.variableName
# 2. From outside of class we can delete instance variables as follows
#  del objectreference.variableName


# Example:
# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#         self.d=40
#     def m1(self):
#         del self.d 

# t=Test() 
# print(t.__dict__)
# t.m1() 
# print(t.__dict__) 
# del t.c 
# print(t.__dict__)


# Example:
# class Test: 
#     def __init__(self): 
#         self.a=10 
#         self.b=20 
#         self.c=30 
#         self.d=40 

# t1=Test() 
# t2=Test() 
# del t1.a 
# print(t1.__dict__) 
# print(t2.__dict__)


# Example:
# class Test:
#     def __init__(self): 
#         self.a=10 
#         self.b=20 

# t1=Test() 
# t1.a=888 
# t1.b=999 
# t2=Test() 
# print('t1:',t1.a,t1.b)
# print('t2:',t2.a,t2.b) 


# Static variables:
# Instance Variable vs Static Variable:
# class Test:
#     x=10 
#     def __init__(self): 
#         self.y=20 

# t1=Test() 
# t2=Test() 
# print('t1:',t1.x,t1.y) 
# print('t2:',t2.x,t2.y) 
# Test.x=888 
# t1.y=999 
# print('t1:',t1.x,t1.y) 
# print('t2:',t2.x,t2.y) 


# Various places to declare static variables:
# class Test: 
#     a=10 
#     def __init__(self):
#         Test.b=20 
#     def m1(self): 
#         Test.c=30 
#     @classmethod 
#     def m2(cls): 
#         cls.d1=40 
#         Test.d2=400 
#     @staticmethod 
#     def m3(): 
#         Test.e=50 
# print(Test.__dict__) 
# t=Test() 
# print(Test.__dict__) 
# t.m1() 
# print(Test.__dict__) 
# Test.m2() 
# print(Test.__dict__)
# Test.m3() 
# print(Test.__dict__) 
# Test.f=60 
# print(Test.__dict__)



# How to access static variables:
# class Test: 
#     a=10 
#     def __init__(self): 
#         print(self.a) 
#         print(Test.a) 
#     def m1(self): 
#         print(self.a)
#         print(Test.a)
#     @classmethod 
#     def m2(cls): 
#         print(cls.a) 
#         print(Test.a) 
#     @staticmethod 
#     def m3(): 
#         print(Test.a) 
# t=Test() 
# print(Test.a) 
# print(t.a) 
# t.m1() 
# t.m2() 
# t.m3()


# Where we can modify the value of static variable:
# class Test: 
#     a=777 
#     @classmethod 
#     def m1(cls): 
#         cls.a=888 
#     @staticmethod 
#     def m2():
#         Test.a=999 
# print(Test.a) 
# Test.m1() 
# print(Test.a) 
# Test.m2() 
# print(Test.a) 


# If we change the value of static variable by using either self 
# or object reference variable:
# class Test: 
#     a=10
#     def m1(self): 
#         self.a=888 
# t1=Test() 
# t1.m1() 
# print(Test.a)
# print(t1.a) 


# Example:
# class Test: 
#     x=10 
#     def __init__(self): 
#         self.y=20 

# t1=Test() 
# t2=Test() 
# print('t1:',t1.x,t1.y) 
# print('t2:',t2.x,t2.y) 
# t1.x=888 
# t1.y=999 
# print('t1:',t1.x,t1.y)
# print('t2:',t2.x,t2.y)


# Example:
# class Test: 
#     a=10 
#     def __init__(self): 
#         self.b=20
# t1=Test() 
# t2=Test() 
# Test.a=888 
# t1.b=999 
# print(t1.a,t1.b) 
# print(t2.a,t2.b) 


# Ex:
# class Test: 
#     a=10 
#     def __init__(self): 
#         self.b=20 
#     def m1(self): 
#         self.a=888 
#         self.b=999 
# t1=Test() 
# t2=Test() 
# t1.m1() 
# print(t1.a,t1.b) 
# print(t2.a,t2.b)


# Example:
# class Test:
#     a=10
#     def __init__(self):
#         self.b=20
#     @classmethod
#     def m1(cls):
#         cls.a=888
#         cls.b=999
#
# t1=Test()
# t2=Test()
# t1.m1()
# print(t1.a,t1.b)
# print(t2.a,t2.b)
# print(Test.a,Test.b)


# How to delete static variables of a class:
# We can delete static variables from anywhere by using the following syntax
# del classname.variablename
# But inside classmethod we can also use cls variable
# del cls.variablename

# class Test: 
#     a=10 
#     @classmethod 
#     def m1(cls): 
#         del cls.a 
# Test.m1() 
# print(Test.__dict__)


# Example:
# class Test: 
#     a=10 
#     def __init__(self): 
#         Test.b=20 
#         del Test.a 
#     def m1(self): 
#         Test.c=30 
#         del Test.b 
#     @classmethod 
#     def m2(cls): 
#         cls.d=40 
#         del Test.c 
#     @staticmethod 
#     def m3(): 
#         Test.e=50 
#         del Test.d 
# print(Test.__dict__) 
# t=Test()
# print(Test.__dict__) 
# t.m1() 
# print(Test.__dict__) 
# Test.m2() 
# print(Test.__dict__) 
# Test.m3() 
# print(Test.__dict__) 
# Test.f=60 
# print(Test.__dict__) 
# del Test.e 
# print(Test.__dict__) 


# Example:
# class Test: 
#     a=10 

# t1=Test() 
# del t1.a        #AttributeError: a 


# We can modify or delete static variables only by using classname or cls variable.
# import sys 
# class Customer:
#     ''' Customer class with bank operations.. ''' 
#     bankname='DURGABANK' 
#     def __init__(self,name,balance=0.0): 
#         self.name=name 
#         self.balance=balance 
#     def deposit(self,amt): 
#         self.balance=self.balance+amt 
#         print('Balance after deposit:',self.balance) 
#     def withdraw(self,amt): 
#         if amt>self.balance: 
#             print('Insufficient Funds..cannot perform this operation') 
#             sys.exit() 
#         self.balance=self.balance-amt 
#         print('Balance after withdraw:',self.balance) 

# print('Welcome to',Customer.bankname) 
# name=input('Enter Your Name:') 
# c=Customer(name) 
# while True: 
#     print('d-Deposit \nw-Withdraw \ne-exit') 
#     option=input('Choose your option:') 
#     if option=='d' or option=='D': 
#         amt=float(input('Enter amount:')) 
#         c.deposit(amt) 
#     elif option=='w' or option=='W': 
#         amt=float(input('Enter amount:')) 
#         c.withdraw(amt) 
#     elif option=='e' or option=='E': 
#         print('Thanks for Banking') 
#         sys.exit() 
#     else: 
#         print('Invalid option..Plz choose valid option')



# Local variables:
# Example:
# class Test: 
#     def m1(self): 
#         a=1000 
#         print(a) 
#     def m2(self): 
#         b=2000 
#         print(b) 
# t=Test() 
# t.m1()
# t.m2()


# Example 2: 
# class Test: 
#     def m1(self): 
#         a=1000 
#         print(a) 
#     def m2(self): 
#         b=2000 
#         # print(a)    #NameError: name 'a' is not defined 
#         print(b) 
# t=Test() 
# t.m1() 
# t.m2() 