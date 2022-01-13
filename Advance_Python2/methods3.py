# Types of Methods:
# 1. Instance Methods
# 2. Class Methods
# 3. Static Methods


# 1. Instance Methods
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print('Hi',self.name)
#         print('Your Marks are:',self.marks)
#     def grade(self):
#         if self.marks>=60:
#             print('You got First Grade')
#         elif self.marks>=50:
#             print('You got Second Grade')
#         elif self.marks>=35:
#             print('You got Third Grade')
#         else:
#             print('You are Failed')
# n=int(input('Enter number of students:'))
# for i in range(n):
#     name=input('Enter Name:')
#     marks=int(input('Enter Marks:'))
#     s= Student(name,marks)
#     s.display()
#     s.grade()
#     print()


# Setter and Getter Methods:
# Setter Method:
# syntax:
# def setVariable(self,variable):
#  self.variable=variable
# Example:
# def setName(self,name):
#  self.name=name


# Getter Method:
# syntax:
# def getVariable(self):
#  return self.variable
 
# Example:
# def getName(self):
#  return self.name


#  Demo Program:
# class Student: 
#     def setName(self,name):
#         self.name=name 

#     def getName(self): 
#         return self.name 

#     def setMarks(self,marks): 
#         self.marks=marks 

#     def getMarks(self): 
#         return self.marks 

# n=int(input('Enter number of students:')) 
# for i in range(n): 
#     s=Student() 
#     name=input('Enter Name:') 
#     s.setName(name) 
#     marks=int(input('Enter Marks:')) 
#     s.setMarks(marks)

#     print('Hi',s.getName()) 
#     print('Your Marks are:',s.getMarks()) 
#     print() 


# Demo Program:
# class Animal: 
#     legs=4 
#     @classmethod 
#     def walk(cls,name): 
#         print('{} walks with {} legs...'.format(name,cls.legs)) 
# Animal.walk('Dog') 
# Animal.walk('Cat') 


# Program to track the number of objects created for a class:
# class Test: 
#     count=0 
#     def __init__(self): 
#         Test.count =Test.count+1 
#     @classmethod 
#     def noOfObjects(cls): 
#         print('The number of objects created for test class:',cls.count)

# t1=Test() 
# t2=Test() 
# Test.noOfObjects() 
# t3=Test() 
# t4=Test() 
# t5=Test() 
# Test.noOfObjects()



# 3. Static Methods:
# class DurgaMath: 

#     @staticmethod 
#     def add(x,y): 
#         print('The Sum:',x+y) 

#     @staticmethod 
#     def product(x,y): 
#         print('The Product:',x*y) 

#     @staticmethod 
#     def average(x,y): 
#         print('The average:',(x+y)/2) 

# DurgaMath.add(10,20) 
# DurgaMath.product(10,20) 
# DurgaMath.average(10,20)


# Passing members of one class to another class:
# We can access members of one class inside another class.
# class Employee:
#     def __init__(self,eno,ename,esal):
#         self.eno=eno
#         self.ename=ename
#         self.esal=esal
#     def display(self):
#         print('Employee Number:',self.eno)
#         print('Employee Name:',self.ename)
#         print('Employee Salary:',self.esal)
# class Test:
#     def modify(emp):
#         emp.esal=emp.esal+10000
#         emp.display()
# e=Employee(100,'Durga',10000)
# Test.modify(e)


# Inner classes:
# class Outer: 
#     def __init__(self): 
#         print("outer class object creation") 
#     class Inner: 
#         def __init__(self): 
#             print("inner class object creation") 
#         def m1(self): 
#             print("inner class method") 
# o=Outer() 
# i=o.Inner() 
# i.m1()


# syntaxes for calling inner class method
# 1.
# o=Outer()
# i=o.Inner()
# i.m1()
# 2. 
# i=Outer().Inner()
# i.m1()
# 3. 
# Outer().Inner().m1()


# Demo Program-2:
# class Person:
#     def __init__(self):
#         self.name='durga'
#         self.db=self.Dob()
#     def display(self):
#         print('Name:',self.name)
#     class Dob:
#         def __init__(self):
#             self.dd=10
#             self.mm=5
#             self.yy=1947
#         def display(self):
#             print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))
# p=Person()
# p.display()
# x=p.db
# x.display()


# Demo Program-3:
# Inside a class we can declare any number of inner classes.
# class Human:
#
#     def __init__(self):
#         self.name = 'Sunny'
#         self.head = self.Head()
#         self.brain = self.Brain()
#     def display(self):
#         print("Hello..",self.name)
#
#     class Head:
#         def talk(self):
#             print('Talking...')
#
#     class Brain:
#         def think(self):
#             print('Thinking...')
#
# h=Human()
# h.display()
# h.head.talk()
# h.brain.think()


# Garbage Collection:
# 1. gc.isenabled()
#  Returns True if GC enabled
# 2. gc.disable()
#  To disable GC explicitly
# 3. gc.enable()
#  To enable GC explicitly

# Example:
# import gc
# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())
# gc.enable()
# print(gc.isenabled())


# Destructors:
# Destructor is a special method and the name should be __del__

# Example:
# import time 
# class Test: 
#     def __init__(self): 
#         print("Object Initialization...") 
#     def __del__(self): 
#         print("Fulfilling Last Wish and performing clean up activities...") 

# t1=Test() 
# t1=None 
# time.sleep(5) 
# print("End of application") 



# Example:
# import time 
# class Test: 
#     def __init__(self): 
#         print("Constructor Execution...") 
#     def __del__(self): 
#         print("Destructor Execution...") 

# t1=Test() 
# t2=t1 
# t3=t2 
# del t1 
# time.sleep(5) 
# print("object not yet destroyed after deleting t1") 
# del t2 
# time.sleep(5) 
# print("object not yet destroyed even after deleting t2") 
# print("I am trying to delete last reference variable...") 
# del t3 


# Example:
# import time
# class Test:
#     def __init__(self):
#         print("Constructor Execution...")
#     def __del__(self):
#         print("Destructor Execution...")
#
# list=[Test(),Test(),Test()]
# del list
# time.sleep(5)
# print("End of application")



# How to find the number of references of an object:
# sys.getrefcount(objectreference)
# Example:
# import sys 
# class Test: 
#     pass 
# t1=Test() 
# t2=t1 
# t3=t1 
# t4=t1 
# print(sys.getrefcount(t1)) 