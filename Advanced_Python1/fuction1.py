# Built in functions
# id()
# type()
# input()
# eval()


# # user defined fuctions
# def wish():
#     print("Hello Good Morning")
# wish()
# wish()
# wish()


# # Parameters
# def wish(name):
#     print("Hello",name,"Good Morning")
# wish("Durga")
# wish("Ravi")

# #print square
# def square(number):
#     print("The square of",number,"is",number*number)
# square(4)
# square(5)

#Types of arguments
# 1.positional arguments
# 2.keyword arguments
# 3.default arguments
# 4.variable length arguments

# 1.positional arguments
# def sub(a,b):
#     print(a-b)

# sub(100,200)
# sub(200,100)

# 2.keyword arguments
# def wish(name,msg):
#     print("Hello",name,msg)
# wish(name="Durga",msg="Good Morning")
# wish(msg="Good Morning",name="Durga")

# 3.default arguments
# def wish(name="Guest"):
#     print("Hello",name,"Good Morning")
# wish("Durga")
# wish()

# 4.variable length arguments
# def sum(*n):
#     total=0
#     for n1 in n:
#         total = total+n1
#     print("The Sum=",total)

# sum()
# sum(10)
# sum(10,20)
# sum(10,20,30,40)


#mix variable length arguments with positional arguments
# def f1(n1,*s):
#     print(n1)
#     for s1 in s:
#         print(s1)
# f1(10)
# f1(10,20,30,40)
# f1(10,"A",30,"B")


#after variable length arguments any other argument then provide values as keyword
# def f1(*s,n1):
#     for s1 in s:
#         print(s1)
#     print(n1)

# f1("A","B",n1=10)

#keyword variable length arguments
# def f1(**n):

#internally they are stored in a dictionary
# def display(**kwargs):
#     for k,v in kwargs.items():
#         print(k,"=",v)
# display(n1=10,n2=20,n3=30)
# display(rno=100,name="Durga",marks=70,subject="Java")

#global variable
# a=10
# def f1():
#     print(a)

# def f2():
#     print(a)

# f1()
# f2()

#local variable
# def f1():
#     a=10
#     print(a)

# def f2():
#     print(a)

# f1()
# f2()

#global keyword
# Ex1:
# a=10
# def f1():
#     a=77
#     print(a)

# def f2():
#     print(a)

# f1()
# f2()

# Ex2:
# a=10
# def f1():
#     global a
#     a=77
#     print(a)

# def f2():
#     print(a)

# f1()
# f2()

# Ex3:
# def f1():
#     a=10
#     print(a)

# def f2():
#     print(a)   # name 'a' is not defined

# f1()
# f2()


# def f1():
#     global a
#     a=10
#     print(a)

# def f2():
#     print(a)

# f1()
# f2()


#if global and local variable have same name then
#we can access global variable inside a function as follows
# a=10
# def f1():
#     a=777
#     print(a)
#     print(globals()['a'])
# f1()