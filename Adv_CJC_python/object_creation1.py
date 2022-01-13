# Syntax of class:
# class A:      #A is child
#     pass      #pass is used for empty class or empty method.

# class B():
#     pass

# class C(object):  #object is a readymade class of python
#     pass          #Every python class is child class



# Syntax of class:
# class ClassName:
#     #statement suite
# Ex:
# class B:          #class variable
#     x=10

# class A:           #class variable
#     x=20
#     def m1(self):  #instant method
#         pass




# Program:
# class A:
#     pass
# class B():
#     pass
# class C(object):
#     pass

# print(issubclass(A,object))   #True
# print(issubclass(B,object))   #True
# print(issubclass(C,object))   #True
# print(issubclass(B,A))        #False



# Ex: object creation
# a=A()          #a object is created
# a.x=100      #x=100 at 678902
# a.y=400      #y=400 at 678902

# a1=A()        #x=500 at 543289
# a1.x=500

# print(a.x)           #100
# print(a.y)           #400
# print(a1.x)         #500
# print(id(a))        #678902
# print(id(a1))      #543289




# Ex:
# a=A()          #x=100
# a.x=100

# a1=A()       #x=500
# a1.x=500

# print(a.x)        #100
# print(a1.x)      #500



# Program:
# class A():
#     pass
    
# a=A()
# a.x=100
# a.y=300

# a1=A()
# a1.x=600

# print(a.x)
# print(a.y)
# print(a1.x)
# print(id(a))
# print(id(a1))
# print(id(a.x))
# print(id(a.y))
# print(id(a1.x))


# Program:
# class A:
#     x=10

# a=A()
# a.x=100
# a1=A()
# a1.x=200
# print(a.x)
# print(a1.x)
# print(A.x)



# class Student:
#     pass

# s1=student()                     
# s1.rollno=1                      #rollno=1
# s1.name="xyz"                #name=xyz	
# s2=student()
# s2.rollno=2                      #rollno=2
# s2.name="pqr"          #name=pqr

# print(s1.rollno)
# print(s1.name)
# print(s2.rollno)
# print(s2.name)


