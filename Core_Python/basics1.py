# print("welcome to digital trainee")
# name=input("enter your name ")
# birth_year=int(input("enter your birth year "))
# print("Welcome "+name+" your age is "+str(2021-birth_year))

# a="apple"
# b="mango"
# c=a+b
# print(c)
# print(a+c)

# radius=float(input("radius of circle:"))
# pi=3.14
# Area_of_circle=(pi*radius*radius)
#
# print("Area of circle"+str(Area_of_circle))


# Program: algebraic_expression
# a=int(input("a="))
# b=int(input("b="))
# print("(a+b)2="+str((a+b)**2))
# print("(a+b)*(a+b)="+str((a+b)*(a+b)))
# print("a2+2ab+b2="+str(a**2+2*a*b+b**2))


#if_elif_else
# n=int(input("enter a number: "))
# if n>0:
#     print("positive")
# elif n==0:
#     print("no. is 0")
# else:
#     print("negative")


# Program: odd_even
# n=int(input("Enter a number: "))
# if n%2==0:
#     print("no. is even")
# else:
#     print("no. is odd")


# Program: largest_smallest
# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# c=int(input("enter a number: "))

# if a>b and a>c:
#     print("a is largest")

# elif b>c:
#     print("b is largest")

# else:
#     print("c is largest")

# if a<b and a<c:
#     print("a is smallest")
    
# elif b<c:
#     print("b is smallest")

# else:
#     print("c is smallest")


# Program: month_if_else
# month=str(input("enter any month: "))
# if month==("january") or month==("march") or month==("may") or month==("july") or month==("august") or month==("octomber") or month==("december"):
#     print("31 days")
    
# elif month==("april") or month==("june") or month==("septemper") or month==("november"):
#     print("30 days")

# elif month==("february"):
#     print("28 or 29 days")

# else:
#     print("invalid")


# Program: divisible by 4 or not, even or odd
# n=int(input("enter a number: "))
# if n%2==0:
#     print("number is even")
#     if n%4==0:
#         print("divisible by 4")
#     else:
#         print("not divisible by 4")
# else:
#     print("number is odd")
#     print("not divisible by 4")


# Program: swapping
# a=int(input("enter a number: "))
# b=int(input("enter another number: "))
# print("Before swapping: a=" + str(a) +" and b=" +str(b))
# c=b
# b=a
# a=c
# print("After swapping: a=" + str(a) +" and b=" +str(b))


# i/p: any year
# o/p: leap year or not
# (all centuries are not leap year except that are divisible by 400)
# Program: leap_year
# year=int(input("enter any year: "))
# if year%400==0:
#     print("It is leap year.")
# elif year%100==0:
#     print("It is not a leap year.")
# elif year%4==0:
#     print("It is a leap year.")
# else:
#     print("It is not a leap year.")


# Explanation:
# year = int(input("Enter a year: "))  
# if (year % 4) == 0: #1st True
#     if (year % 100) == 0:  #2nd (if 1st is True)
#         if (year % 400) == 0:  #3rd (if 1st and 2nd is true.)
#             print(" leap year")  # all 3 condition are true than it will print
#         else:  
#             print("not a leap year")  #if 1st and 2nd are True and 3rd is False.
#     else:  
#         print("leap year")  # if 1st is True and 2nd is False.
# else:  
#     print("not a leap year")  # if 1st False
