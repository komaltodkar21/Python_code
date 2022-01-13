# Program:
# class A:
#     def __init__(self):
#         print("constructor--A")

# a=A()
# a1=A()
# a2=A()



# Ex:
# class A:
#     pass

# a=A()
# a.x=100



# Ex:
# class A:
#     def __init__(self,y):
#         self.x=y

# a=A(100)    #x=100



# Program:
# class A:
#     def __init__(self):
#         print("constructor--A")

# a=A()
# a.x=100
# a1=A()
# a1.x=200
# print(a.x)
# print(a1.x)



# Program:
# class A:
#     def __init__(self,y):
#         self.x=y

# a=A(100)
# a1=A(200)

# print(a.x)
# print(a1.x)



# Program:
# class A:
#     def __init__(self,x):
#         self.x=x

# a=A(100)
# a1=A(200)

# print(a.x)
# print(a1.x)



# # Self.x - instance variable
# # x - local variable


# Program:
# class student:
#     pass

# s1=student()
# s1.rollno=1
# s1.name="xyz"

# s2=student()
# s2.rollno=2
# s2.name="abc"

# print(s1.rollno)
# print(s1.name)
# print(s2.rollno)
# print(s2.name)


# Program:
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

# s1=student(1,"xyz")
# s2=student(2,"abc")

# print(s1.rollno)
# print(s1.name)
# print(s2.rollno)
# print(s2.name)


# Program:
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#     def display(self):
#         print(self.rollno)
#         print(self.name)

# s1=student(1,"xyz")
# s2=student(2,"abc")

# s1.display()
# s2.display()



# Program:
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#     def display(self):
#         return "Hello"

# s1=student(1,"xyz")
# s2=student(2,"abc")

# print(s1.display())
# x=s2.display()
# print(x)



# Program:
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#     def __str__(self):
#         return "Hello"

# s1=student(1,"xyz")
# s2=student(2,"abc")

# print(s1)
# print(s2)



# Program:
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#     def __str__(self):
#         return "Roll.No:-{} and Name:-{}".format(self.rollno,self.name)

# s1=student(1,"xyz")
# s2=student(2,"abc")

# print(s1)
# print(s2)


# Ex:
# class A:
#     def m1():
#         pass

# a=A()
# a.m1


