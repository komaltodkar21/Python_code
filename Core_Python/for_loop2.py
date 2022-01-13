#for loop
#range (start, end, step): range(0,10,2)


# for n in range(1,11):
#     print(n)


# Program: To print table of 5 using for loop
# for n in range(5,51,5):
#     print(n)

# a=range(5)  #starts with 0
# print(a)
# print(a[0])
# print(a[1])
# print(a[-1])
# print(a[4])

# a=range(1,5)  #starts with 1
# print(a)
# print(a[0])
# print(a[1])
# print(a[-1])
# print(a[4])   #IndexError: range object index out of range

# a=range(1,10,2)  #starts with 1
# print(a)
# print(a[0])
# print(a[1])
# print(a[-1])
# print(a[4])

# st="komal"
# for ch in st:
#     print(ch)

# Important
# st="komal"
# n=len(st)
# for i in range(n):
#     print(i,"-->",st[i])    #use , instead of +

# Nested for loop
# for i in range(2):
#     print("Outer loop",i)
#     for j in range(3):
#         print("Inner loop",j)
# print("done!")


# break - else part is not executed after break
# for i in range(10):
#     if (i==5):
#         break
#     print(i)
# print("done!")


# for i in range(10):
#     print(i)
#     if (i==5):
#         break
# print("done!")


#continue - skip current iteration and execute next
# for i in range(10):
#     if(i==3):
#         continue
#     print(i)
# print("done!")


#pass - no operation statement
# if 5>2:          # if true else part doesnot execute
#     pass
# else:
#     print("Else Part")
# print("DONE!")

#pass
# i=1
# while i<=10:
#     if (i==5):
#         pass
#     print(i)
#     i+=1
# print("done!")


# i/p: any number
# o/p: print table for that number using for loop
# Program: table
# n=int(input("enter any number: "))
# for i in range(n,n*11,n):
#     print(i)


# range() - returns a range object (a type of iterable)
# xrange() - returns generator object used to display only by looping 
#            (particular range is displayed "lazy evaluation")
# a=range(1,11)   # range is used in python 3
# x=xrange(1,11)  # x range is used in python 2
# print(type(a))
# print(type(x))


# Program: factorial   (increment, multiply)
# n=int(input("enter any number: "))
# fact=1
# for i in range(1,n):
#     i=i+1                     #i= 1+1 =2
#     fact=fact*i                #fact= 1*2   =2
      
# print("factorial of that number is " + str(fact))


# Program: even_odd_for_loop
# for i in range(1,51):
#     if i%2==0:
#         print("even")
#     else:
#         print(i)


# Program: fizz_buzz
# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("fizzbuzz")

#     elif i%3==0 or i%5==0:
#         if i%3==0:
#             print("fizz")
#         if i%5==0:
#             print("buzz")

#     else:
#         print(i)



# Program: swapping
# x=0
# y=1
# print("Before swapping: x=" + str(x) + " y=" + str(y))
# a=x
# x=y
# y=a
# print("After swapping: x=" + str(x) + " y=" + str(y))



# Program: fabiconi_series (swapping)
# k=0
# j=1
# for i in range(1,21):
#     print(k)           #k=1
#     z=k+j              #z=1+2=3
#     k=j                #k=2
#     j=z                #j=3


# Program: fabiconi_two_variables (swapping)
# j=0
# k=1
# for i in range(1,21):
#     print(j)
#     k=j+k
#     j,k=k,j


# Program: prime_for_if_else
# for i in range(2,101):
#     if (i==2 or i==3 or i==5 or i==7):
#            print(i)
#     else:
#         if (i%2==0 or i%3==0 or i%5==0 or i%7==0):
#             pass
#         else:
#             print(i)       
# else:
#     print("done!")


# Program: prime_nested_for
# for i in range(1,101):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)