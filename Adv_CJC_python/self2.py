# Syntax:
# class Student:
#     def display(self):
#         print(self.rollno)
#         print(self.name)

# s1=student()
# s1.rollno=1                         #rollno=1
# s1.name="xyz"                  #name=xyz
# s2=student()
# s2.rollno=2                         #rollno=2
# s2.name="pqr"                  #name=pqr

# s1.display()     #student.display(s1)
# s2.display()     #student.display(s2)



# Syntax:
# class Student:
#     def display(self):
#         print(self.rollno)
#         print(self.name)

# s1=student()
# s1.rollno=1                         #rollno=1
# s1.name="xyz"                  #name=xyz
# s2=student()
# s2.rollno=2                         #rollno=2
# s2.name="pqr"                  #name=pqr

# s1.display()     #student.display(s1)
# s2.display()     #student.display(s2)



# Program:
# class student:
#     pass

# s1=student()
# s1.rollno=1                             #rollno=1
# s1.name="xyz"                      #name=xyz

# s2=student()
# s2.rollno=2                             #rollno=2
# s2.name="pqr"                     #name=pqr

# print(s1.rollno)
# print(s1.name)
# print(s2.rollno)
# print(s2.name)
# print(id(s1))
# print(id(s2))



# Program:
# class student:
#     def display(self):
#         print(self.rollno)
#         print(self.name)

# s1=student()
# s1.rollno=1
# s1.name="xyz"                      

# s2=student()
# s2.rollno=2
# s2.name="pqr"

# print("main---",id(s1))
# s1.display()
# print("main---",id(2))
# s2.display()



# Program:
# class student:
#     def display(self):
#         print(id(self))
#         print(self.rollno)
#         print(self.name)

# s1=student()
# s1.rollno=1
# s1.name="xyz"                      

# s2=student()
# s2.rollno=2
# s2.name="pqr"

# print("main---",id(s1))
# s1.display()
# print("main---",id(s2))
# s2.display()



# Program:
# class student:
#     def display(self):
#         print("display---",id(self))

# s1=student()
# s1.rollno=1
# s1.name="xyz"                      

# s2=student()
# s2.rollno=2
# s2.name="pqr"

# print("kunal---",id(s1))
# student.display(s1)
# print("CJC---",id(s2))
# s2.display()



# Program:
# class student:
#     def display(self):
#         print("display---",id(self))
#         print(self.rollno)
#         print(self.name)

# s1=student()
# s1.rollno=1
# s1.name="xyz"                      

# s2=student()
# s2.rollno=2
# s2.name="pqr"

# print("kunal---",id(s1))
# student.display(s1)
# print("CJC---",id(s2))
# s2.display()
