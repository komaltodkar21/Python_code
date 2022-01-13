#tuple is immutable
#it is order sequence
# in terms of execution tuple is faster than list 
# (tuple only contains static memory list both dynamic and static memory)

#functions of tuple
# t1=(1,2,3,4,5,5)
# print(len(t1))
# print(max(t1))
# print(min(t1))
# print(sum(t1))
# print(sorted(t1))
# print(tuple(t1))
# print(any(t1))
# print(all(t1))

#cmp() -available only in python 2 not python 3

#methods of tuple
# print(t1.count(5))
# print(t1.index(5))


# primes=(2,3,5,7)
# pos=primes.index(5)
# print("position of 5 is",pos)

# country=('i','n','d','i','a')
# x=country.count('i')
# print("i occurs",x,"times in",country)

#packing unpacking tuple
# a,b=(5,2)
# print(a)
# print(b)

# a,*b=(1,2,3,4,5,6,7)
# print(a)
# print(b)


# a=10
# b=20
# c=30
# d=40
# t=a,b,c,d
# print(t)     #(10,20,30,40)


# a=1,2,3
# x,y,z=a
# print(x,y,z)    # 1 2 3


# t=(10,20,30,40)
# a,b,c,d=t
# print("a=",a," b=",b," c=",c," d=",d)

#swapping
# a=10
# b=20
# b,a=a,b

#returning multiple values from function
# def calculate(a,b):
#     c=a+b
#     d=a-b
#     return c,d
# x,y=calculate(5,3)
# print("Sum is",x,"and difference is",y)
# z=calculate(15,23)
# print("Sum is",z[0],"and difference is",z[1])

# def add(a,b,c,d):
#     print("Sum is",a+b+c+d)
# mytuple=(10,20,30,40)
# add(*mytuple)


#accessing elements of tuple
# t=(10,20,30,40)
# print(t[0])
# print(t[-1])
# print(t[100])

#by using slice operator
# t=[10,20,30,40,50,60]
# print(t[2:5])
# print(t[2:100])
# print(t[::-2])
#print(t[1:4:2])


#print entire tuple
# a=(10,20,30,40)
# print(a)

#accessing individual elements
# mynums=(10,20,30,40,50)
# print(mynums[0])
# print(mynums[1])
# print(mynums[-3])
# print(mynums[-2])

#accessing tuple using for loop
# n=[10,20,30,40,50]
# for x in n:
#     print(x)

#accessing tuple using while loop
# n=(10,20,30,40,50)
# x=len(n)
# i=0
# while i<x:
#     print(n[i])
#     i=i+1

#concatination
# t1=(10,20,30)
# t2=(40,50,60)
# t3=t1+t2
# print(t3)

#multiplication
# t1=(10,20,30)
# t2=t1*3
# print(t2)