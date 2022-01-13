#class
# Example:
# class Student:
#     '''This is student class with required data'''
# print(Student.__doc__)
# help(Student)


# Example for class:
# class Student:
#     '''Developed by durga for python demo'''
#     def __init__(self): 
#         self.name='durga' 
#         self.age=40 
#         self.marks=80
    
#     def talk(self):
#         print("Hello I am :",self.name)
#         print("My Age is:",self.age)
#         print("My Marks are:",self.marks)


# Reference Variable:
# Call the method talk() to display student details
# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name=name 
#         self.rollno=rollno 
#         self.marks=marks 

#     def talk(self): 
#         print("Hello My Name is:",self.name) 
#         print("My Rollno is:",self.rollno) 
#         print("My Marks are:",self.marks)

# s1=Student("Durga",101,80) 
# s1.talk() 

# Constructor
# Example:
# def __init__(self,name,rollno,marks): 
#     self.name=name 
#     self.rollno=rollno 
#     self.marks=marks


# Program to demonistrate constructor will execute only once per object:
# class Test:
#     def __init__(self):
#         print("Constructor exeuction...")
#     def m1(self):
#         print("Method execution...")
#
# t1=Test()
# t2=Test()
# t3=Test()
# t1.m1()

# Ex:
# class Student:
#     ''' This is student class with required data''' 
#     def __init__(self,x,y,z):
#         self.name=x
#         self.rollno=y
#         self.marks=z
        
#     def display(self):
#         print("Student Name:{}\nRollno:{} \nMarks:{}".format(self.name,self.rollno,self.marks))

# s1=Student("Durga",101,80) 
# s1.display() 
# s2=Student("Sunny",102,100) 
# s2.display()