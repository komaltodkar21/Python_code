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

# for stu in l:
#     print(stu.rollno)
#     print(stu.name)
   
# o/p:
# 1
# abc
# 2
# pqr
# 3
# xyz

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

# for stu in l:
#     print(stu)
    
# o/p:
# Roll.No:- 1 and Name:- abc
# Roll.No:- 2 and Name:- pqr
# Roll.No:- 3 and Name:- xyz

# Progarm:
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#     def __str__(self):
#         return "Roll.No:- {} and Name:- {}".format(self.rollno,self.name)

# l=[]
# s1=student(1,"abc")
# s2=student(2,"pqr")
# s3=student(3,"xyz")

# l.append(s1)
# l.append(s2)
# l.append(s3)

# for stu in l:
#     print(stu)
   
# o/p:
# Roll.No:- 1 and Name:- abc
# Roll.No:- 2 and Name:- pqr
# Roll.No:- 3 and Name:- xyz

# Program:
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#     def __str__(self):
#         return "Roll.No:- {} and Name:- {}".format(self.rollno,self.name)

# l=[]
# s1=student(1,"abc")
# s2=student(2,"pqr")
# s3=student(3,"xyz")

# l.append(s1)
# l.append(s1)
# l.append(s1)

# for stu in l:
#     print(stu)

# o/p:
# Roll.No:- 1 and Name:- abc
# Roll.No:- 1 and Name:- abc
# Roll.No:- 1 and Name:- abc
   
# Program:
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#     def __str__(self):
#         return "Roll.No:- {} and Name:- {}".format(self.rollno,self.name)

# l=[]
# s1=student(1,"abc")
# s1=student(2,"pqr")
# s1=student(3,"xyz")

# l.append(s1)
# l.append(s1)
# l.append(s1)

# for stu in l:
#     print(stu)

# o/p:
# Roll.No:- 3 and Name:- xyz
# Roll.No:- 3 and Name:- xyz
# Roll.No:- 3 and Name:- xyz

# Program:
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#     def __str__(self):
#         return "Roll.No:- {} and Name:- {}".format(self.rollno,self.name)

# l=[]
# s1=student(1,"abc")
# l.append(s1)
# s1=student(2,"pqr")
# l.append(s1)
# s1=student(3,"xyz")
# l.append(s1)

# for stu in l:
#     print(stu)
    
# o/p:
# Roll.No:- 1 and Name:- abc
# Roll.No:- 2 and Name:- pqr
# Roll.No:- 3 and Name:- xyz

# List in List
# (using inner for loop)

# Ex:
# MH=["Pune", "Mumbai", "Nagpur"]
# JH=["Ranchi","Lohardaga"]
# India=[MH, JH]

# for l in India:
#     for city in l:
#         print(city)

# o/p:
# Pune
# Mumbai
# Nagpur
# Ranchi
# Lohardaga

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
# mca1=[s1,s2,s3]

# s4=student(1,"bbb")
# s5=student(1,"ccc")
# mca2=[s4,s5]

# mca=[mca1,mca2]

# for l in mca:
#     for stu in l:
#         print(stu)
    
# o/p:
# Roll.No:- 1 and Name:- abc
# Roll.No:- 2 and Name:- pqr
# Roll.No:- 3 and Name:- xyz
# Roll.No:- 1 and Name:- bbb
# Roll.No:- 1 and Name:- ccc
