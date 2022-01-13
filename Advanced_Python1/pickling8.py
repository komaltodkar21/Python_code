#Pickling and Unpickling of objects
# The process of writing state of object to the file is called pickling.
# The process of reading state of an object from the file is called unpickling.

# pickle module contains dump() function to perform pickling
# pickle.dump(object,file)

# pickle module contains load() function to perform unpickling
# obj=pickle.load(file)

# Writing and Reading State of object by using pickle Module:
# import pickle
# class Employee:
#     def __init__(self,eno,ename,esal,eaddr):
#         self.eno=eno;
#         self.ename=ename;
#         self.esal=esal;
#         self.eaddr=eaddr;
#     def display(self):
#         print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
# with open("emp.dat","wb") as f:
#     e=Employee(100,"Durga",1000,"Hyd")
#     pickle.dump(e,f)
#     print("Pickling of Employee Object completed...")
# with open("emp.dat","rb") as f:
#     obj=pickle.load(f)
#     print("Printing Employee Information after unpickling")
#     obj.display()

# Pickling of Employee Object completed...
# Printing Employee Information after unpickling
# 100 	 Durga 	 1000 	 Hyd


#Writing multiple Employee Objects to the file:
# emp.py:-
# class Employee:
#     def __init__(self,eno,ename,esal,eaddr):
#         self.eno=eno;
#         self.ename=ename;
#         self.esal=esal;
#         self.eaddr=eaddr;
#     def display(self):
#         print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)


# pick.py:-
# import emp,pickle
# f=open("emp.dat","wb")
# n=int(input("Enter The number of Employees:"))
# for i in range(n):
#     eno=int(input("Enter Employee Number:"))
#     ename=input("Enter Employee Name:")
#     esal=float(input("Enter Employee Salary:"))
#     eaddr=input("Enter Employee Address:")
#     e=emp.Employee(eno,ename,esal,eaddr)
#     pickle.dump(e,f)
# print("Employee Objects pickled successfully")

# Enter The number of Employees:2
# Enter Employee Number:23
# Enter Employee Name:komal
# Enter Employee Salary:1000
# Enter Employee Address:jhkjklj
# Enter Employee Number:45
# Enter Employee Name:kjhk
# Enter Employee Salary:36687
# Enter Employee Address:gjhkji
# Employee Objects pickled successfully


# unpick.py:-
# import emp,pickle
# f=open("emp.dat","rb")
# print("Employee Details:")
# while True:
#     try:
#         obj=pickle.load(f)
#         obj.display()
#     except EOFError:
#         print("All employees Completed")
#         break
#     f.close()

# Employee Details:
# All employees Completed