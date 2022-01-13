# How to solve custom class object?
# Ex:
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#     def __str__(self):
#         return "Roll.No:- {} and Name:- {}".format(self.rollno,self.name)


# s1=student(1,"abc")
# s2=student(2,"pqr")
# s3=student(3,"xyz")
# l=[s1,s2,s3]
# l.sort(key=roll_no)

# for stu in l:
#     print(stu)

# o/p:
# Traceback (most recent call last):
#   File "C:\Users\KOMAL\Desktop\hello.py", line 14, in <module>
#     l.sort(key=roll_no)
# NameError: name 'roll_no' is not defined
# >>>



# To solve this error-
# 1.	Sort by using method.
# Program:
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name		

#     def __str__(self):
#         return "Roll.No:- {} and Name:- {}".format(self.rollno,self.name)


# def roll_no(obj):
#     return obj.rollno

# def name_sort(obj):
#     return obj.name
    

# s1=student(1,"abc")
# s2=student(2,"pqr")
# s3=student(3,"xyz")
# l=[s1,s2,s3]

# l.sort(key=name_sort)

# for stu in l:
#     print(stu)
    
# o/p:
# Roll.No:- 1 and Name:- abc
# Roll.No:- 2 and Name:- pqr
# Roll.No:- 3 and Name:- xyz



# 2.	Sort by using lambda.
# Program:
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#     def __str__(self):
#         return "Roll.No:- {} and Name:- {}".format(self.rollno,self.name)

# s1=student(1,"abc")
# s2=student(2,"pqr")
# s3=student(3,"xyz")
# l=[s1,s2,s3]

# l.sort(key=lambda x:x.rollno)

# for stu in l:
#     print(stu)
    
# o/p:
# Roll.No:- 1 and Name:- abc
# Roll.No:- 2 and Name:- pqr
# Roll.No:- 3 and Name:- xyz



# 3.	Sort by using attrgetter method.
# Program:
# from operator import attrgetter
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#     def __str__(self):
#         return "Roll.No:- {} and Name:- {}".format(self.rollno,self.name)


# s1=student(1,"abc")
# s2=student(2,"pqr")
# s3=student(3,"xyz")
# l=[s1,s2,s3]

# l.sort(key=attrgetter('name'), reverse=True)

# for stu in l:
#     print(stu)
    
# o/p:
# Roll.No:- 3 and Name:- xyz
# Roll.No:- 2 and Name:- pqr
# Roll.No:- 1 and Name:- abc



# Program: 
# from operator import attrgetter
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#         def __str__(self):
#             return "Roll.No:- {} and Name:- {}".format(self.rollno,self.name)


# s1=student(1,"abc")
# s2=student(2,"pqr")
# s3=student(3,"xyz")
# t=(s1,s2,s3)

# l=sorted(t,key=attrgetter('name'))
# print(type(l))
# for stu in l:
#     print(stu)
# o/p:
# <class 'list'>
# Roll.No:- 1 and Name:- abc
# Roll.No:- 2 and Name:- pqr
# Roll.No:- 3 and Name:- xyz

# Program:
# from operator import attrgetter
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#     def __str__(self):
#         return "Roll.No:- {} and Name:- {}".format(self.rollno,self.name)


# s1=student(1,"abc")
# s2=student(2,"pqr")
# s3=student(3,"xyz")
# t=(s1,s2,s3)

# t1=tuple(sorted(t,key=attrgetter('name')))

# print(type(t1))
# for stu in t1:
#       print(stu)
# o/p:
# <class 'tuple'>
# Roll.No:- 1 and Name:- abc
# Roll.No:- 2 and Name:- pqr
# Roll.No:- 3 and Name:- xyz

# s={6,8,9,5}
# s.remove(8)
# print(s)
