# Write a Python program to create a log file and write WARNING and higher level messages?
# import logging 
# logging.basicConfig(filename='log.txt',level=logging.WARNING) 
# print("Logging Module Demo") 
# logging.debug("This is debug message") 
# logging.info("This is info message") 
# logging.warning("This is warning message") 
# logging.error("This is error message") 
# logging.critical("This is critical message") 


# log.txt file is created
# WARNING:root:This is warning message 
# ERROR:root:This is error message 
# CRITICAL:root:This is critical message


# If we set level as DEBUG then all messages will be written to log file.
# import logging 
# logging.basicConfig(filename='log.txt',level=logging.DEBUG) 
# print("Logging Module Demo") 
# logging.debug("This is debug message") 
# logging.info("This is info message") 
# logging.warning("This is warning message") 
# logging.error("This is error message") 
# logging.critical("This is critical message") 

# log.txt will append the following
# DEBUG:root:This is debug message 
# INFO:root:This is info message 
# WARNING:root:This is warning message 
# ERROR:root:This is error message 
# CRITICAL:root:This is critical message


# Python Program to write exception information to the log file
# import logging 
# logging.basicConfig(filename='mylog.txt',level=logging.INFO) 
# logging.info("A New request Came:") 
# try: 
#     x=int(input("Enter First Number: ")) 
#     y=int(input("Enter Second Number: ")) 
#     print(x/y) 
# except ZeroDivisionError as msg: 
#     print("cannot divide with zero") 
#     logging.exception(msg) 
# except ValueError as msg: 
#     print("Enter only int values") 
#     logging.exception(msg) 
# logging.info("Request Processing Completed")

# 4/2
# 3/0
# 4/f

# mylog.txt file is created
# INFO:root:A New request Came: 
# INFO:root:Request Processing Completed 
# INFO:root:A New request Came: 
# ERROR:root:division by zero 
# Traceback (most recent call last): 
# File "test.py", line 7, in <module> 
# print(x/y) 
# ZeroDivisionError: division by zero 
# INFO:root:Request Processing Completed 
# INFO:root:A New request Came: 
# ERROR:root:invalid literal for int() with base 10: 'ten' 
# Traceback (most recent call last): 
# File "test.py", line 6, in <module> 
# y=int(input("Enter Second Number: ")) 
# ValueError: invalid literal for int() with base 10: 'ten' 
# INFO:root:Request Processing Completed 


# PYTHON DEBUGGING BY USING ASSERTIONS
# Eg:
# def squareIt(x):
#     return x**x
# assert squareIt(2)==4,"The square of 2 should be 4"
# assert squareIt(3)==9,"The square of 3 should be 9"
# assert squareIt(4)==16,"The square of 4 should be 16"
# print(squareIt(2))
# print(squareIt(3))
# print(squareIt(4))


