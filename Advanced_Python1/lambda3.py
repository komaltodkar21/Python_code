#recursive function
# factorial(3)=3*factorial(2)
#             =3*2*factorial(1)
#             =3*2*1*factorial(0)
#             =3*2*1*1
#             =6
# factorial(n)=n*factorial(n-1)


#factorial with recursion
# def factorial(n):
#     if n==0:
#         result=1
#     else:
#         result=n*factorial(n-1)
#     return result

# print("Factorial of 4 is:",factorial(4))
# print("Factorial of 5 is:",factorial(5))


#Normal Function
# def squarelt(n):
#     return n*n

# print(square(4))

#Lambda function/Anonymous Function/One line function/nameless function
#(we define it using lambda keyword)
# s=lambda n:n*n
# print("The Square of 4 is :",s(4))
# print("The Square of 5 is :",s(5))

#sum of 2 given numbers
# s=lambda a,b:a+b
# print("The Sum of 10,20 is:",s(10,20))
# print("The Sum of 100,200 is:",s(100,200))

#find biggest of given values
# s=lambda a,b:a if a>b else b
# print("The Biggest of 10,20 is:",s(10,20))
# print("The Biggest of 100,200 is:",s(100,200))

# filter() function
# def isEven(x):
#     if x%2==0:
#         return True
#     else:
#         return False

# l=[0,5,10,15,20,25,30]
# l1=list(filter(isEven,l))
# print(l1)


#with lambda function
# l=[0,5,10,15,20,25,30]
# l1=list(filter(lambda x:x%2==0,l))
# print(l1)  #[0,10,20,30]
# l2=list(filter(lambda x:x%2!=0,l))
# print(l2) #[5,15,25]


#map() function
#without lambda
# l=[1,2,3,4,5]
# def doublelt(x):
#     return 2*x
# l1=list(map(doublelt,l))
# print(l1)  #[2,4,6,8,10]


# l=[1,2,3,4,5]
# l1=list(map(lambda x:2*x,l))
# print(l1) #[2,4,6,8,10]

# l=[1,2,3,4,5]
# l1=list(map(lambda x:x*x,l))
# print(l1)  #[1,4,9,16,25]

# l1=[1,2,3,4]
# l2=[2,3,4,5]
# l3=list(map(lambda x,y:x*y,l1,l2))
# print(l3)  #[2,6,12,20]

# reduce() function
# from functools import *
# l=[10,20,30,40,50]
# result=reduce(lambda x,y:x+y,l)
# print(result)  #150
# result=reduce(lambda x,y:x*y,l)
# print(result)  #12000000
# result=reduce(lambda x,y:x+y,range(1,10))
# print(result)


# def f1():
#     print("Hello")
# print(f1)
# print(id(f1))

#function aliasing
# def wish(name):
#     print("Good Morning:",name)

# greeting=wish
# print(id(wish))
# print(id(greeting))

# greeting('Durga')
# wish('Durga')

#if we delete one name still we can access that function using alias name
# def wish(name):
#     print("Good Morning:",name)

# greeting=wish

# greeting('Durga')
# wish('Durga')

# del wish
# # wish('Durga')  #name wish is not defined
# greeting('Pavan')

#nested function
# def outer():
#     print("Outer function started")
#     def inner():
#         print("inner function execution")
#     print("outer function calling inner function")
#     inner()
# outer()
# #inner() #name inner is not defined


#inner function is local to outer function
#it is not possible to call directly from outside of outer() function
# def outer():
#     print("outer function started")
#     def inner():
#         print("inner function execution")
#     print("outer function returning inner function")
#     return inner
# f1=outer()
# f1()
# f1()
# f1()


#  difference between 
# f1=outer   #function aliasing
# f1=outer() #calling outer function