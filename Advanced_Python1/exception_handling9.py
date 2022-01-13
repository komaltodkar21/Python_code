#Syntax Error
#ex1:
# x=10
# if x==10
# print("Hello")

#ex2:
# print "Hello"


#Runtime error
# print(10/0)   #ZeroDivisionError
# print(10/"ten")   #TypeError

# x=int(input("Enter Number:"))
# print(x)


#Default exception handling in python
# print("Hello") 
# print(10/0) 
# print("Hi")


# without try-except:
# print("stmt-1")
# print(10/0)
# print("stmt-3")


# with try-except:
# print("stmt-1") 
# try:
#     print(10/0) 
# except ZeroDivisionError:
#     print(10/2) 
# print("stmt-3")

# stmt-1
# 5.0
# stmt-3


# How to print exception information:
# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print("exception raised and its description is:",msg)


# Eg:
# try: 
#     x=int(input("Enter First Number: ")) 
#     y=int(input("Enter Second Number: ")) 
#     print(x/y) 
# except ZeroDivisionError : 
#     print("Can't Divide with Zero") 
# except ValueError: 
#     print("please provide int value only")


# Eg:
# try: 
#     x=int(input("Enter First Number: ")) 
#     y=int(input("Enter Second Number: ")) 
#     print(x/y) 
# except ArithmeticError : 
#     print("ArithmeticError")       #preference to first error
# except ZeroDivisionError: 
#     print("ZeroDivisionError")


# Single except block that can handle multiple exceptions:
# Eg:
# try: 
#     x=int(input("Enter First Number: ")) 
#     y=int(input("Enter Second Number: ")) 
#     print(x/y) 
# except (ZeroDivisionError,ValueError) as msg: 
#     print("Plz Provide valid numbers only and problem is: ",msg) 


#Default Except Block:
# Eg:
# try:
#     print(10/0)
# except:
#     print("Default Except")      #dilog box error
# except ZeroDivisionError:
#     print("ZeroDivisionError")


# Case-1: If there is no exception
# try: 
# print("try") 
# except: 
# print("except") 
# finally: 
# print("finally") 


# Case-2: If there is an exception raised but handled:
# try: 
#     print("try") 
#     print(10/0) 
# except ZeroDivisionError: 
#     print("except") 
# finally: 
#     print("finally") 


# Case-3: If there is an exception raised but not handled:
# try: 
#     print("try") 
#     print(10/0) 
# except NameError: 
#     print("except") 
# finally: 
#     print("finally")


# Nested try-except-finally blocks:
# Eg:
# try:
#     print("outer try block")
#     try:
#         print("Inner try block")
#         print(10/0)
#     except ZeroDivisionError:
#         print("Inner except block")
#     finally:
#         print("Inner finally block")
# except:
#     print("outer except block")
# finally:
#     print("outer finally block")

# outer try block
# Inner try block
# Inner except block
# Inner finally block
# Outer finally block


# How to Define and Raise Customized Exceptions:
# Eg:
# class TooYoungException(Exception): 
# def __init__(self,arg):
#     self.msg=arg 


# Eg:
# class TooYoungException(Exception):
#     def __init__(self,arg):
#         self.msg=arg 

# class TooOldException(Exception):
#     def __init__(self,arg):
#         self.msg=arg 

# age=int(input("Enter Age:")) 
# if age<18:
#     raise TooYoungException("Plz wait some more time you will get best match soon!!!") 
# elif age>60:
#     raise TooOldException("Your age already crossed marriage age...no chance of getting marriage") 
# else:
#     print("You will get match details soon by email!!!")

# Enter Age:26
# You will get match details soon by email!!