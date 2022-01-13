# List Comprehension
# Program:
# #without comprehension
# l=[1,2,3,4,5,6,7,8]
# n_l=[]
# for x in l:
#     x=x**2
#     n_l.append(x)
# print(n_l)

# #with comprehension
# l=[1,2,3,4,5,6,7,8]
# n_l=[x**2 for x in l]
# print(n_l)


# Program:
# #without comprehension
# l=[1,2,3,4,5,6,7,8]
# n_l=[]
# for x in l:
#     if x%2==0:
#         x=x**2
#         n_l.append(x)
# print(n_l)

# #with comprehension
# l=[1,2,3,4,5,6,7,8]
# n_l=[v**2 for v in l if v%2==0]
# print(n_l)



# Program:
# #without comprehension
# mh=['mumbai','pune','nagpur']
# jh=['ranchi','lohardaga']
# india=[mh,jh]

# all_city=[]
# for l in india:
#     for city in l:
#         all_city.append(city)
# print(all_city)


# #with comprehension
# mh=['mumbai','pune','nagpur']
# jh=['ranchi','lohardaga']
# india=[mh,jh]

# all_city=[city for l in india for city in l]
# print(all_city)



# Program:
# #without comprehension
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#     def __str__(self):
#         return "Rollno:- {} and Name:- {}".format(self.rollno,self.name)

# s1=student(1,'aaa')
# s2=student(2,'abc')
# s3=student(3,'Ankita')
# s4=student(1,'komal')

# l=[s1,s2,s3,s4]
# n_l=[]
# for stu in l:
#     if stu.name.startswith('a'):
#         n_l.append(stu)

# for s in n_l:
#     print(s)


# #with comprehension
# n_l=[stu for stu in l if stu.name.startswith('a')]
# for s in n_l:
#     print(s)



# Program: 
# #without comprehension
# class student:
#     def __init__(self,rollno,name):
#         self.rollno=rollno
#         self.name=name

#     def __str__(self):
#         return "Rollno:- {} and Name:- {}".format(self.rollno,self.name)

# s1=student(1,'aaa')
# s2=student(2,'abc')
# s3=student(3,'Ankita')
# s4=student(1,'komal')

# l=[s1,s2,s3,s4]
# n_l=[]
# for stu in l:
#     if stu.name.startswith('a') or stu.name.startswith('A'):
#         n_l.append(stu)

# for s in n_l:
#     print(s)

# #with comprehension
# n_l=[stu for stu in l if stu.name.startswith('a') or stu.name.startswith('A')]
# for s in n_l:
#     print(s)


# Set comprehension
# Instead of [ ] use { }

# Ex:
# n_l={stu for stu in l if stu.name.startswith('a') or stu.name.startswith('A')}



# Dictionary Comprehension
# d={key,value for key,value in iterable condition}

# l=[1,2,3,4,5,6]   #d=[1:1, 2:4, 3:9, 4:10, 5:25]



# Program:
# l=[1,2,3,4,5,6]
# d={v:v**2 for v in l}
# print(d)


# d={v:v**2 for v in l if v%2==0}
# print(d)


# mh=['Pune','Mumbai']
# jh=['Ranchi','Lohardaga']
# india={'Maharashtra':mh, 'Jharkhand':jh}
# n_india={k:v for k,v in india.items()}
# print(n_india)


