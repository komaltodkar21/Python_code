# import math
# print(math.log10(100))    #2.0


# from math import pi
# print(pi)                #3.141592653589793


# from math import *
# print(log10(100))
# print(pi)
# 2.0
# 3.141592653589793

# import math as m
# print(m.log10(100))
# print(m.pi)
# 2.0
# 3.141592653589793

# import durgamath
# print(durgamath.x)
# durgamath.add(10,20)
# durgamath.product(10,20)   #no module named durgamath

#Ex:
# import durgamath as m
# print(m.x)
# m.add(10,20)
# m.product(10,20)      #no module named durgamath

# Ex:
# from durgamath import x,add
# print(x)
# add(10,20)
# product(10,20)   #name product is not defined

# Ex:
# from durgamath import *
# print(x)
# add(10,20)
# product(10,20)

#member aliasing
# from durgamath import x as y, add as sum
# print(y)
# sum(10,20)

# Ex:
# from durgamath import x as y
# print(x)        #name x is not defined

# Ex:
# import time
# from imp import reload
# import module1
# time.sleep(30)
# reload(module1)
# time.sleep(30)
# reload(module1)
# print("This is test file")

# Ex:
# import module1
# import module1
# import module1
# import module1
# print("This is test module")

# Ex:
# import module1
# import module1
# from imp import reload
# reload(module1)
# reload(module1)
# reload(module1)
# print("This is test module")


#finding members of module by using dir() function
# x=10
# y=20
# def f1():
#     print("Hello")
# print(dir())    #To print all members of current module


#To display members of particular module
# import durgamath
# print(dir(durgamath))


#can access these properties also
# print(__builtins__)
# print(__cached__)
# print(__doc__)
# print(__file__)
# print(__loader__)
# print(__name__)
# print(__package__)
# print(__spec__)


#The special variable __name__
# import module1
# module1.f1()


#working with math module
# from math import *
# print(sqrt(4))
# print(ceil(10.1))
# print(floor(10.1))
# print(fabs(-10.6))
# print(fabs(10.6))

#can find help for any module
# import math
# help(math)

#working with random module
#random() function
# from random import *
# for i in range(10):
#     print(random())

#randint() function
# from random import *
# for i in range(10):
#     print(randint(1,100))  #generate random integer value between 1 and 100


#uniform() function
# from random import *
# for i in range(10):
#     print(uniform(1,10))


#randrange([start],stop,[step])
# from random import *
# for i in range(10):
#     print(randrange(10))

# Ex:
# from random import *
# for i in range(10):
#     print(randrange(1,11))

# Ex:
# from random import *
# for i in range(10):
#     print(randrange(1,11,2))


#choice() function
# from random import *
# list=["Sunny","Bunny","Chinny","Vinny","pinny"]
# for i in range(10):
#     print(choice(list))


#packages
#Ex:
# import pack1.module1
# pack1.module1.f1()

#Ex:
# from pack1.module1 import f1
# f1()

#Ex:
# from com.module1 import f1
# from com.durgasoft.module2 import f2
# f1()
# f2()