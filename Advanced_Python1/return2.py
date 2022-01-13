# function
# def square(n):
#     return n*n
# print(square(4))
# print(square(5))

# Program: return
# def multiply(n,m):
#     return n*m
# print(multiply(2,3))
# print(multiply(4,5))

# Ex:
# def addition(a,b):
#     c=a+b
#     print(c)

# addition(100,800)
# o/p:
# 900

# Ex:
# def addition(a,b):
#     c=a+b
#     return c

# x=addition(100,800)
# print(x)
# print(addition(300,400))
# o/p:
# 900
# 700

#return sum
# def add(x,y):
#     return x+y
# result=add(10,20)
# print("The sum is",result)
# print("The sum is",add(100,200))

#if not writing return statement default value is none
# def f1():
#     print("Hello")
# f1()
# print(f1())

# o/p:
# Hello
# Hello
# None

# Program: return_even_odd
# def num(n):
#     if n%2==0:
#         return 'even'

#     else:
#         return 'odd'

# print(num(10))
# print(num(15))

#check odd or even
# def even_odd(num):
#     if num%2==0:
#         print(num,"is Even Number")
#     else:
#         print(num,"is Odd Number")
# even_odd(10)
# even_odd(15)

# Program: return_factorial
# def fact(n):
#     k=1
#     for i in range(1,n+1):
#         x=k*i
#         k=x

#     return x

#find factorial using while loop
# def fact(num):
#     fact=1
#     while num>=1:
#         fact=fact*num
#         num=num-1
#     return fact
# for i in range(1,5):
#     print("The Factorial of",i,"is:",fact(i))


# Program: return_prime
# def prime(num):
#         for i in range(2,num):     
#             if (num % i) == 0:             
#                 print(num,"is not a prime number")    
#                 break
#         else:  
#             print(num,"is a prime number")

# prime(2)
# prime(4)
# prime(5)

# ***********
# Program: return_diff
# def diff(n):
#     x=[]
#     k=n[0]
#     for i in range(1,len(n)):
#         y=n[i]-k
#         x.append(y)
#         k=n[i]

#     return x

# print(diff(5))


#returning multiple values from a function
# def sum_sub(a,b):
#     sum=a+b
#     sub=a-b
#     return sum,sub
# x,y=sum_sub(100,50)
# print("The Sum is:",x)
# print("The Substraction is:",y)



# def calc(a,b):
#     sum=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return sum,sub,mul,div
# t=calc(100,50)
# print("The Result are")
# for i in t:
#     print(i)


# Ex:
# def addition(a,b):
#     c=a+b
#     print(c)

# x=addition(100,200)
# print(x)
# o/p:
# 300
# None

# Ex:
# def addition(a,b):
#     c=a+b
#     print(c)
#     return c

# x=addition(100,200)
# print(x)
# o/p:
# 300
# 300

# Program:
# def addition(a,b):
#     c=a+b
#     return c

# def multiply():
#     x=addition(300,100)
#     x=x*5
#     print(x)

# multiply()
# o/p:
# 2000

# Program:
# def addition(a,b):
#     c=a+b
#     print(c)
#     return c

# def multiply():
#     x=addition(300,5)
#     y=x*5
#     print(y)

# multiply()
# o/p:
# 305
# 1525

# Bank application (without return statement)
# Program:
# bal=3000

# def deposit(amt):
#     global bal
#     bal=bal+amt

# def withdraw(amt):
#     global bal
#     bal=bal-amt

# def bal_check():
#     print(bal)

# deposit(1000)
# bal_check()
# withdraw(500)
# bal_check()
# o/p:
# 4000
# 3500

# Bank application (with return statement)
# Program:
# mbal=3000

# def deposit(bal,amt):
#     bal=bal+amt
#     return bal

# def withdraw(bal,amt):
#     bal=bal-amt
#     return bal

# print(mbal)
# mbal=deposit(mbal,2000)
# print(mbal)
# mbal=withdraw(mbal,1000)
# print(mbal)
# o/p:
# 3000
# 5000
# 4000

