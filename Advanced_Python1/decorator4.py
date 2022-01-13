# def wish(name):
#     print("Hello",name,"Good Morning")
# wish("komal")

# Ex:
# def decor(func):
#     def inner(name):
#         if name=="Sunny":
#             print("Hello Sunny Bad Morning")
#         else:
#             func(name)
#     return inner

# @decor
# def wish(name):
#     print("Hello",name,"Good Morning")

# wish("Durga")
# wish("Ravi")
# wish("Sunny")


#call same function with decorator and without decorator
# def decor(func):
#     def inner(name):
#         if name=="Sunny":
#             print("Hello Sunny Bad Morning")
#         else:
#             func(name)
#     return inner

# def wish(name):
#     print("Hello",name,"Good Morning")

# decorfunction=decor(wish)

# wish("Durga") #decorator wont be executed
# wish("Sunny") #decorator wont br executed

# decorfunction("Durga")  #decorator will be executed
# decorfunction("Sunny")  #decorator will be executed


# Ex:
# def smart_division(func):
#     def inner(a,b):
#         print("We are dividing",a,"with",b)
#         if b==0:
#             print("OOPS... cannot divide")
#         else:
#             return func(a,b)
#     return inner
# @smart_division
# def division(a,b):
#     return a/b
# print(division(20,2))
# print(division(20,0))


# Decorator channing
# define multiple decorators for same function
# @decor1
# @decor
# def num():

#Ex:
# def decor1(func):
#     def inner():
#         x=func()
#         return x*x
#     return inner

# def decor(func):
#     def inner():
#         x=func()
#         return 2*x
#     return inner

# @decor1
# @decor
# def num():
#     return 10

# print(num())


# Ex:
# def decor(func):
#     def inner(name):
#         print("First Decor(decor) Function Execution")
#         func(name)
#     return inner

def decor1(func):
    def inner(name):
        print("Second Decor(decor1) Execution")
        func(name)
    return inner

# @decor1
# @decor
# def wish(name):
#     print("Hello",name,"Good Morning")

# wish("Durga")