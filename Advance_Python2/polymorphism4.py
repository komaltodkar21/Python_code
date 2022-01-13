# Related to polymorphism the following 4 topics are important
# 1. Duck Typing Philosophy of Python
# 2. Overloading
#  1. Operator Overloading
#  2. Method Overloading
#  3. Constructor Overloading
# 3. Overriding
#  1. Method overriding
#  2. constructor overriding


# 1. Duck Typing Philosophy of Python:
# class Duck: 
#     def talk(self): 
#         print('Quack.. Quack..') 

# class Dog:
#     def talk(self): 
#         print('Bow Bow..') 

# class Cat: 
#     def talk(self): 
#         print('Moew Moew ..') 

# class Goat: 
#     def talk(self): 
#         print('Myaah Myaah ..') 

# def f1(obj): 
#     obj.talk() 

# l=[Duck(),Cat(),Dog(),Goat()] 
# for obj in l:
#     f1(obj) 



# Eg:
# class Duck: 
#     def talk(self): 
#         print('Quack.. Quack..') 

# class Dog: 
#     def bark(self): 
#         print('Bow Bow..')

# def f1(obj): 
#     obj.talk() 

# d=Duck() 
# f1(d) 

# d=Dog() 
# f1(d) 



# Demo Program with hasattr() function:
# class Duck: 
#     def talk(self): 
#         print('Quack.. Quack..') 

# class Human: 
#     def talk(self): 
#         print('Hello Hi...') 

# class Dog: 
#     def bark(self): 
#         print('Bow Bow..') 

# def f1(obj): 
#     if hasattr(obj,'talk'): 
#         obj.talk() 
#     elif hasattr(obj,'bark'): 
#         obj.bark() 

# d=Duck() 
# f1(d) 

# h=Human() 
# f1(h) 

# d=Dog() 
# f1(d) 
# Quack.. Quack..
# Hello hii...
# Bow.. Bow..


# 1. Operator Overloading:
# Demo program to use + operator for our class objects:
# class Book: 
#     def __init__(self,pages): 
#         self.pages=pages 

# b1=Book(100) 
# b2=Book(200) 
# print(b1+b2)


# Demo program to overload + operator for our Book class objects:
# class Book: 
#     def __init__(self,pages): 
#         self.pages=pages 

#     def __add__(self,other): 
#         return self.pages+other.pages 

# b1=Book(100) 
# b2=Book(200) 
# print('The Total Number of Pages:',b1+b2)


# The following is the list of operators and corresponding magic methods.
# + ---> object.__add__(self,other)
# - ---> object.__sub__(self,other)
# * ---> object.__mul__(self,other)
# / ---> object.__div__(self,other)
# // ---> object.__floordiv__(self,other)
# % ---> object.__mod__(self,other)
# ** ---> object.__pow__(self,other)
# += ---> object.__iadd__(self,other)
# -= ---> object.__isub__(self,other)
# *= ---> object.__imul__(self,other)
# /= ---> object.__idiv__(self,other)
# //= ---> object.__ifloordiv__(self,other)
# %= ---> object.__imod__(self,other)
# **= ---> object.__ipow__(self,other)
# < ---> object.__lt__(self,other)
# <= ---> object.__le__(self,other)
# > ---> object.__gt__(self,other)
# >= ---> object.__ge__(self,other)
# == ---> object.__eq__(self,other)
# != ---> object.__ne__(self,other)



# Overloading > and <= operators for Student class objects:
# class Student: 
#     def __init__(self,name,marks): 
#         self.name=name 
#         self.marks=marks 
#     def __gt__(self,other): 
#         return self.marks>other.marks 
#     def __le__(self,other): 
#         return self.marks<=other.marks 
 
# print("10>20 =",10>20) 
# s1=Student("Durga",100) 
# s2=Student("Ravi",200) 
# print("s1>s2=",s1>s2) 
# print("s1<s2=",s1<s2) 
# print("s1<=s2=",s1<=s2) 
# print("s1>=s2=",s1>=s2) 


# Program to overload multiplication operator to work on Employee objects:
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __mul__(self,other):
#         return self.salary*other.days
#
# class TimeSheet:
#     def __init__(self,name,days):
#         self.name=name
#         self.days=days
#
# e=Employee('Durga',500)
# t=TimeSheet('Durga',25)
# print('This Month Salary:',e*t)


# 2. Method Overloading:
# Demo Program:
# class Test: 
#     def m1(self): 
#         print('no-arg method') 
#     def m1(self,a): 
#         print('one-arg method') 
#     def m1(self,a,b): 
#         print('two-arg method') 

# t=Test() 
# #t.m1() 
# #t.m1(10) 
# t.m1(10,20)


# Demo Program with Default Arguments:
# class Test: 
#     def sum(self,a=None,b=None,c=None): 
#         if a!=None and b!= None and c!= None: 
#             print('The Sum of 3 Numbers:',a+b+c) 
#         elif a!=None and b!= None: 
#             print('The Sum of 2 Numbers:',a+b) 
#         else: 
#             print('Please provide 2 or 3 arguments') 

# t=Test() 
# t.sum(10,20) 
# t.sum(10,20,30) 
# t.sum(10)


# Demo Program with Variable Number of Arguments:
# class Test: 
#     def sum(self,*a): 
#         total=0 
#         for x in a: 
#             total=total+x 
#         print('The Sum:',total) 

# t=Test() 
# t.sum(10,20) 
# t.sum(10,20,30) 
# t.sum(10) 
# t.sum() 


# 3. Constructor Overloading:
# Constructor overloading is not possible in Python.
# If we define multiple constructors then the last constructor will be considered.
# class Test: 
#     def __init__(self): 
#         print('No-Arg Constructor') 

#     def __init__(self,a): 
#         print('One-Arg constructor') 

#     def __init__(self,a,b): 
#         print('Two-Arg constructor') 

# #t1=Test() 
# #t1=Test(10) 
# t1=Test(10,20)


# Constructor with Default Arguments:
# class Test: 
#     def __init__(self,a=None,b=None,c=None): 
#         print('Constructor with 0|1|2|3 number of arguments') 

# t1=Test() 
# t2=Test(10) 
# t3=Test(10,20) 
# t4=Test(10,20,30)


# Constructor with Variable Number of Arguments:
# class Test: 
#     def __init__(self,*a): 
#         print('Constructor with variable number of arguments') 

# t1=Test() 
# t2=Test(10) 
# t3=Test(10,20) 
# t4=Test(10,20,30) 
# t5=Test(10,20,30,40,50,60) 


# Method overriding:
# Demo Program for Method overriding:
# class P: 
#     def property(self): 
#         print('Gold+Land+Cash+Power') 
#     def marry(self): 
#         print('Appalamma') 
# class C(P): 
#     def marry(self): 
#         print('Katrina Kaif') 

# c=C() 
# c.property() 
# c.marry() 


# From Overriding method of child class,we can call parent class method also by using super() 
# method.
# class P: 
#     def property(self): 
#         print('Gold+Land+Cash+Power') 
#     def marry(self): 
#         print('Appalamma') 
# class C(P): 
#     def marry(self): 
#         super().marry() 
#         print('Katrina Kaif') 

# c=C() 
# c.property() 
# c.marry() 


# Demo Program for Constructor overriding:
# class P: 
#     def __init__(self): 
#         print('Parent Constructor') 

# class C(P): 
#     def __init__(self): 
#         print('Child Constructor') 

# c=C() 


# Demo Program to call Parent class constructor by using super():
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
# class Employee(Person):
#     def __init__(self,name,age,eno,esal):
#         super().__init__(name,age)
#         self.eno=eno
#         self.esal=esal
#
#     def display(self):
#         print('Employee Name:',self.name)
#         print('Employee Age:',self.age)
#         print('Employee Number:',self.eno)
#         print('Employee Salary:',self.esal)
#
# e1=Employee('Durga',48,872425,26000)
# e1.display()
# e2=Employee('Sunny',39,872426,36000)
# e2.display()