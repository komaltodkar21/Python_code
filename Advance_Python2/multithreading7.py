# Multi Tasking:
# Executing several tasks simultaneously is the concept of multitasking.
# There are 2 types of Multi Tasking
#  1. Process based Multi Tasking
#  2. Thread based Multi Tasking

# Program to print name of current executing thread:
# import threading 
# print("Current Executing Thread:",threading.current_thread().getName())


# The ways of Creating Thread in Python:
# We can create a thread in Python by using 3 ways
# 1. Creating a Thread without using any class
# 2. Creating a Thread by extending Thread class
# 3. Creating a Thread without extending Thread class


# 1. Creating a Thread without using any class
# from threading import * 
# def display(): 
#     for i in range(1,11): 
#         print("Child Thread") 
# t=Thread(target=display) #creating Thread object 
# t.start() #starting of Thread 
# for i in range(1,11): 
#     print("Main Thread") 


# 2. Creating a Thread by extending Thread class
# from threading import * 
# class MyThread(Thread): 
#     def run(self): 
#         for i in range(10): 
#             print("Child Thread-1") 
# t=MyThread() 
# t.start() 
# for i in range(10):
#     print("Main Thread-1")



# 3. Creating a Thread without extending Thread class:
# from threading import * 
# class Test: 
#     def display(self): 
#         for i in range(10): 
#             print("Child Thread-2") 
#             obj=Test() 
#             t=Thread(target=obj.display) 
#             t.start() 
# for i in range(10):
#     print("Main Thread-2")


# Without multi threading:
# from threading import * 
# import time 
# def doubles(numbers): 
#     for n in numbers: 
#         time.sleep(1) 
#         print("Double:",2*n) 
# def squares(numbers): 
#     for n in numbers: 
#         time.sleep(1) 
#         print("Square:",n*n) 
# numbers=[1,2,3,4,5,6] 
# begintime=time.time() 
# doubles(numbers) 
# squares(numbers) 
# print("The total time taken:",time.time()-begintime) 


# With multithreading:
# from threading import * 
# import time 
# def doubles(numbers): 
#     for n in numbers: 
#         time.sleep(1) 
#         print("Double:",2*n) 
# def squares(numbers): 
#         for n in numbers: 
#             time.sleep(1) 
#             print("Square:",n*n) 

# numbers=[1,2,3,4,5,6] 
# begintime=time.time() 
# t1=Thread(target=doubles,args=(numbers,)) 
# t2=Thread(target=squares,args=(numbers,)) 
# t1.start() 
# t2.start() 
# t1.join() 
# t2.join() 
# print("The total time taken:",time.time()-begintime) 


# Setting and Getting Name of a Thread:
# t.getName()  Returns Name of Thread
# t.setName(newName)  To set our own name

# Eg:
# from threading import * 
# print(current_thread().getName()) 
# current_thread().setName("Pawan Kalyan") 
# print(current_thread().getName()) 
# print(current_thread().name) 


# Thread Identification Number (ident):
# from threading import * 
# def test(): 
#     print("Child Thread") 
# t=Thread(target=test) 
# t.start() 
# print("Main Thread Identification Number:",current_thread().ident) 
# print("Child Thread Identification Number:",t.ident) 


# active_count():
# This function returns the number of active threads currently running.
# Eg:
# from threading import * 
# import time 
# def display(): 
#     print(current_thread().getName(),"...started") 
#     time.sleep(3) 
#     print(current_thread().getName(),"...ended") 
#     print("The Number of active Threads:",active_count()) 
# t1=Thread(target=display,name="ChildThread1") 
# t2=Thread(target=display,name="ChildThread2") 
# t3=Thread(target=display,name="ChildThread3") 
# t1.start() 
# t2.start() 
# t3.start() 
# print("The Number of active Threads:",active_count()) 
# time.sleep(5) 
# print("The Number of active Threads:",active_count()) 



# enumerate() function:
# This function returns a list of all active threads currently running.
# Eg:
# from threading import * 
# import time 
# def display(): 
#     print(current_thread().getName(),"...started") 
#     time.sleep(3) 
#     print(current_thread().getName(),"...ended") 
# t1=Thread(target=display,name="ChildThread1") 
# t2=Thread(target=display,name="ChildThread2") 
# t3=Thread(target=display,name="ChildThread3") 
# t1.start() 
# t2.start() 
# t3.start() 
# l=enumerate() 
# for t in l: 
#     print("Thread Name:",t.name) 
# time.sleep(5) 
# l=enumerate() 
# for t in l: 
#     print("Thread Name:",t.name)



# isAlive():
# isAlive() method checks whether a thread is still executing or not.
# Eg:
# from threading import * 
# import time 
# def display(): 
#     print(current_thread().getName(),"...started") 
#     time.sleep(3) 
#     print(current_thread().getName(),"...ended") 
# t1=Thread(target=display,name="ChildThread1") 
# t2=Thread(target=display,name="ChildThread2") 
# t1.start() 
# t2.start() 

# print(t1.name,"is Alive :",t1.isAlive()) 
# print(t2.name,"is Alive :",t2.isAlive()) 
# time.sleep(5) 
# print(t1.name,"is Alive :",t1.isAlive()) 
# print(t2.name,"is Alive :",t2.isAlive()) 


# join() method:
# If a thread wants to wait until completing some other thread then we should go for join() method. 
# Eg:
# from threading import * 
# import time 
# def display(): 
#     for i in range(10): 
#         print("Seetha Thread") 
#         time.sleep(2) 

# t=Thread(target=display) 
# t.start() 
# t.join()#This Line executed by Main Thread 
# for i in range(10): 
#     print("Rama Thread") 


# join() method:
# If a thread wants to wait until completing some other thread then we should go for join() method. 
# Eg:
# from threading import * 
# import time 
# def display(): 
#     for i in range(10): 
#         print("Seetha Thread") 
#         time.sleep(2)

# t=Thread(target=display) 
# t.start() 
# t.join()#This Line executed by Main Thread 
# for i in range(10): 
#     print("Rama Thread") 



# Daemon Threads:
# Eg:
# from threading import * 
# print(current_thread().isDaemon()) #False 
# print(current_thread().daemon) #False 


# Eg:
# from threading import * 
# print(current_thread().isDaemon()) 
# current_thread().setDaemon(True)  #RuntimeError


# Default Nature:
# Eg:
# from threading import * 
# def job(): 
#     print("Child Thread") 
# t=Thread(target=job) 
# print(t.isDaemon())#False 
# t.setDaemon(True) 
# print(t.isDaemon()) #True 


# Eg:
# from threading import * 
# import time 
# def job(): 
#     for i in range(10): 
#         print("Lazy Thread") 
#         time.sleep(2) 

# t=Thread(target=job) 
# #t.setDaemon(True)===>Line-1 
# t.start() 
# time.sleep(5) 
# print("End Of Main Thread") 


# Synchronization:
# If multiple threads are executing simultaneously then there may be a chance of data inconsistency 
# problems.
# Eg:
# from threading import * 
# import time 
# def wish(name): 
#     for i in range(10): 
#         print("Good Evening:",end='') 
#         time.sleep(2) 
#         print(name) 
# t1=Thread(target=wish,args=("Dhoni",)) 
# t2=Thread(target=wish,args=("Yuvraj",)) 
# t1.start() 
# t2.start() 


# In Python, we can implement synchronization by using the following 
# 1. Lock
# 2. RLock
# 3. Semaphore


# Eg:
# from threading import * 
# l=Lock() 
# #l.acquire() ==>1 
# l.release()    #RuntimeError

# Eg:
# from threading import *
# import time 
# l=Lock() 
# def wish(name): 
#     l.acquire() 
#     for i in range(10): 
#         print("Good Evening:",end='') 
#         time.sleep(2) 
#         print(name) 
#     l.release() 

# t1=Thread(target=wish,args=("Dhoni",))
# t2=Thread(target=wish,args=("Yuvraj",)) 
# t3=Thread(target=wish,args=("Kohli",)) 
# t1.start() 
# t2.start() 
# t3.start() 


# Problem with Simple Lock:
# Eg:
# from threading import * 
# l=Lock() 
# print("Main Thread trying to acquire Lock") 
# l.acquire() 
# print("Main Thread trying to acquire Lock Again") 
# l.acquire() 


# Eg:
# from threading import * 
# l=RLock() 
# print("Main Thread trying to acquire Lock") 
# l.acquire() 
# print("Main Thread trying to acquire Lock Again") 
# l.acquire()


# Eg:
# l=RLock()
# l.acquire()
# l.acquire()
# l.release()
# l.release()

# After 2 release() calls only the Lock will be released.


# Demo Program for synchronization by using RLock:
# from threading import * 
# import time 
# l=RLock() 
# def factorial(n): 
#     l.acquire() 
#     if n==0: 
#         result=1 
#     else: 
#         result=n*factorial(n-1) 
#     l.release() 
#     return result

# def results(n): 
#     print("The Factorial of",n,"is:",factorial(n)) 

# t1=Thread(target=results,args=(5,)) 
# t2=Thread(target=results,args=(9,)) 
# t1.start() 
# t2.start() 


# Case-1: s=Semaphore()
# In this case counter value is 1 and at a time only one thread is allowed to access. It is exactly same 
# as Lock concept.
# Case-2: s=Semaphore(3)
# In this case Semaphore object can be accessed by 3 threads at a time.The remaining threads have 
# to wait until releasing the semaphore.
# Eg:
# from threading import * 
# import time 
# s=Semaphore(2) 
# def wish(name): 
#     s.acquire() 
#     for i in range(10): 
#         print("Good Evening:",end='') 
#         time.sleep(2) 
#         print(name) 
#     s.release() 

# t1=Thread(target=wish,args=("Dhoni",)) 
# t2=Thread(target=wish,args=("Yuvraj",)) 
# t3=Thread(target=wish,args=("Kohli",)) 
# t4=Thread(target=wish,args=("Rohit",)) 
# t5=Thread(target=wish,args=("Pandya",)) 
# t1.start() 
# t2.start() 
# t3.start() 
# t4.start() 
# t5.start() 


# BoundedSemaphore:
# from threading import * 
# s=Semaphore(2) 
# s.acquire() 
# s.acquire() 
# s.release() 
# s.release() 
# s.release() 
# s.release() 
# print("End")


# Eg:
# from threading import * 
# s=BoundedSemaphore(2) 
# s.acquire() 
# s.acquire() 
# s.release() 
# s.release() 
# s.release() 
# s.release() 
# print("End") 