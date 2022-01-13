# Tuple
# >>> t1=(4,)
# >>> print(type(t1))
# <class 'tuple'>

# >>> t2=(5)
# >>> print(type(t2))
# <class 'int'>

# >>> t3=(5,4,3,6)
# or
# >>> t3=5,4,3,6



# >>> t
# ()
# >>> t1=(3,)
# >>> type(t1)
# <class 'tuple'>
# >>> t2=(4)
# >>> type(t2)
# <class 'int'>
# >>> t=(2,4,5,6)
# >>> t=[0]=40
# SyntaxError: cannot assign to literal
# >>>



# Program: 
# from operator import attrgetter
# from typing import Set
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#      def __str__(self):
#             return "Roll.No:- {} and Name:- {}".format(self.rollno,self.name)


# s1=student(1,"abc")
# s2=student(2,"pqr")
# s3=student(3,"xyz")
# t=(s1,s2,s3)

# l=sorted(t,key=attrgetter('name'))
# print(type(l))
# for stu in l:
#     print(stu)



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



# s={6,8,9,5}
# s.remove(8)
# print(s)


# Set
# >>> s={6,8,4,5}
# >>> s.remove(8)
# >>> s
# {4, 5, 6}
# >>> s.remove(40)
# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
#     s.remove(40)
# KeyError: 40
# >>>



# Program:
# s1={6,8,5,4}
# s1.discard(70)  #no error
# print(s1)
# s1.discard(8)
# print(s1)
# s1.discard(40)  #no error
# print(s1)

# s1.clear()
# print(s1)

# s2={7,8,5,3}
# print(s2)
# s2.pop()        #set doesnot support pop
# print(s2)       #it pops last element




# Program:
# s1={3,4,5,6}
# s2={5,6,7,8}
# print(s1.union(s2))   #all unique elements
# print(s1|s2)          #alternative for union

# print(s1.intersection(s2))  #comman elements
# print(s1&s2)                #alternative for intersection

# print(s1.difference(s2))
# print(s1-s2)
# print(s2.difference(s1))
# print(s2-s1)

# print(s1^s2)     #selected difference/all uncommans



# Dictionary
# >>> d={}
# >>> d
# {}
# >>> d1=dict()
# >>> d1
# {}
# >>> d={5:"java", 10:"python"}
# >>> d[15]="django"
# >>> d
# {5: 'java', 10: 'python', 15: 'django'}
# >>> d[3]="flask"
# >>> d
# {5: 'java', 10: 'python', 15: 'django', 3: 'flask'}
# >>> 



# Program:
# d={5:'java',10:'python'}
# d[15]='django'
# print(d)

# d={"a":50,"b":60,"c":500}
# for key in d.items():
#     print(key)

# for value in d.items():
#     print(value)

# for value in d.items():
#     print(value)



# Program:
# mh=['mumbai','pune']
# jh=['ranchi','lohardaga']
# india={'Maharashtra':mh, 'Jharkhand':jh}
# for key,value in india.items():
#     print(key)
#     for city in value:
#         print(city)



# Program:
# mh=['mumbai','pune']
# jh=['ranchi','lohardaga']
# india={'Maharashtra':mh, 'Jharkhand':jh}
# for k,v in india.items():
#     print(k)
#     print(v)



