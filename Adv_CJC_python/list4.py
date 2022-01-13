# How to create empty list?
# >>> l=[]
# >>> l



# >>> l1=list()
# >>> l1
# []


# >>> l=[2,3,'abc',3]
# >>> l
# [2, 3, 'abc', 3]
# >>> l[0]
# 2
# >>> l[-2]
# 'abc'
# >>> l.append(4)               #(append is used to add elements)
# >>> l
# [2, 3, 'abc', 3, 4]
# >>> l.append(20)
# >>> l
# [2, 3, 'abc', 3, 4, 20]
# >>> for x in l:                   #(use for loop to retrive elements)
# 	print(x)

	
# 2
# 3
# abc
# 3
# 4
# 20
# >>>



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
# l.append(s2)
# l.append(s3)

# for stu in l:
#     print(stu)



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



# List in List
# (using inner for loop)

# Ex:
# MH=["Pune", "Mumbai", "Nagpur"]
# JH=["Ranchi","Lohardaga"]
# India=[MH, JH]

# for l in India:
#     for city in l:
#         print(city)



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



# >>> l=[4,2,5,1,3,7]
# >>> l.sort()
# >>> l
# [1, 2, 3, 4, 5, 7]
# >>> l=sorted(l)
# >>> l
# [1, 2, 3, 4, 5, 7]
# >>> l=['ccc','aaa','bbb','ddd']
# >>> l
# ['ccc', 'aaa', 'bbb', 'ddd']
# >>> l.sort()
# >>> l
# ['aaa', 'bbb', 'ccc', 'ddd']
# >>> l=sorted(l)
# >>> l
# ['aaa', 'bbb', 'ccc', 'ddd']
# >>> l=[4,2,5,1,3,7]
# >>> l.sort(reverse=True)
# >>> l
# [7, 5, 4, 3, 2, 1]
# >>> l=sorted(l,reverse=True)
# >>> l
# [7, 5, 4, 3, 2, 1]
# >>>
