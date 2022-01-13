#opening a file
# f=open(filename,mode)
# f=open("abc.txt","w")

#closing a file
# f.close()

#various properties of file object
# f=open("abc.txt",'w')
# print("File Name:",f.name)
# print("File Mode:",f.mode)
# print("Is File Readable:",f.readable())
# print("Is File Writable:",f.writable())
# print("Is File Closed:",f.closed)
# f.close()
# print("Is File Closed",f.closed)


#writing data to text files
# f=open("abc.txt","w")
# f.write("Durga\n")
# f.write("Software\n")
# f.write("Solutions\n")
# print("Data written to the file successfully")    #overridden
# f.close()

#Ex:
# f=open("abc.txt",'w')
# list=["sunny\n","bunny\n","vinny\n","chinny"]
# f.writelines(list)                                #list of lines
# print("List of lines written to the file successfully")
# f.close()

#To read total data from the file
# f=open("abc.txt",'r')
# data=f.read()
# print(data)
# f.close()

#To read only first 10 characters
# f=open("abc.txt",'r')
# data=f.read(10)
# print(data)
# f.close()


#To read data line by line
# f=open("abc.txt",'r')
# line1=f.readline()
# print(line1,end='')
# line2=f.readline()
# print(line2,end='')
# line3=f.readline()
# print(line3,end='')
# f.close()


#To read all lines into list
# f=open("abc.txt",'r')
# lines=f.readlines()
# for line in lines():
#     print(line,end='')
# f.close()

#Ex:
# f=open("abc.txt",'r')
# print(f.read(3))
# print(f.readline())
# print(f.read(4))
# print("Remaining data")
# print(f.read())


#with statement
# with open("abc.txt",'w') as f:
#     f.write("Durga\n")
#     f.write("Software\n")
#     f.write("Solutions\n")
#     print("Is File Closed:",f.closed)
# print("Is File Closed:",f.closed)


#The seek() and tell() methods:
#tell():
# f=open("open.txt",'r')
# print(f.tell())
# print(f.read(2))
# print(f.tell())
# print(f.read(3))
# print(f.tell())


#seek()
# data="All Students are STUPIDS"
# f=open("abc.txt",'w')
# f.write(data)
# with open("abc.txt",'r+') as f:
#     text=f.read()
#     print(text)
#     print("The Current Cursor Position:",f.tell())
#     f.seek(17)
#     print("The Current Cursor Position:",f.tell())
#     f.write("GEMS!!!")
#     f.seek(0)
#     text=f.read()
#     print("Data After Modification:")
#     print(text)


#How to check a particular file exists or not?
# os.path.isfile(fname)

#How to check a particular file exists or not?
# If it is available print its content?
# import os,sys
# fname=input("Enter File Name: ")
# if os.path.isfile(fname):
#     print("File exists:",fname)
#     f=open(fname,'r')
# else:
#     print("File does not exist:",fname)
#     sys.exit(0)
# print("The content of the file is:")
# data=f.read()
# print(data)


#Program to print the number of lines,word and characters present in the given file?
# import os,sys
# fname=input("Enter File Name:")
# if os.path.isfile(fname):
#     print("File exists:",fname)
#     f=open(fname,'r')
# else:
#     print("File does not exist:",fname)
#     sys.exit(0)
# Icont=wcount=ccount=0
# for line in f:
#     Icount=Icount+1
#     ccount=ccount+len(line)
#     words=line.split()
#     wcount=wcount+len(words)
# print("The number of Lines:",Icount)
# print("The number of Words:",wcount)
# print("The number of Characters:",ccount)

# Enter File Name:abc.txt
# File exists: abc.txt
# The number of lines: 1
# The number of Words: 4
# The number of Characters: 24


#Handling Binary Data
#Program to read image file and write to a new image file?
# f1=open("rossum.jpg",'rb')
# f2=open("newpic.jpg",'wb')
# bytes=f1.read()
# f2.write(bytes)
# print("New image is available with the name: newpic.jpg")


#Handling CSV files
#Writing data to CSV file
# import csv
# with open("abc.txt",'w',newline='') as f:       #emp.csv
#     w=csv.writer(f)   #returns csv writer object
#     w.writerow(["ENO","ENAME","ESAL","EADDR"])
#     n=int(input("Enter Number of Employees:"))
#     for i in range(n):
#         eno=input("Enter Employee No:")
#         ename=input("Enter Employee Name:")
#         esal=input("Enter Employee Salary:")
#         eaddr=input("Enter Employee Address:")
#         w.writerow([eno,ename,esal,eaddr])
# print("Total Employees data written to csv file successfully")


#observer the difference between inline attribute and without
# with open("emp.csv","w",newline='') as f:
# with open("emp.csv","w") as f:


#reading data from csv file
# import csv
# f=open("emp.csv",'r')
# r=csv.reader(f)   #returns csv reader object
# data=list(r)
# #print(data)
# for line in data:
#     for word in line:
#         print(word,"\t",end='')
#     print()


#zipping and unzipping files
# from zipfile import *
# f=ZipFile("files.zip",'w',ZIP_DEFLATED)
# f.write("file1.txt")
# f.write("file2.txt")
# f.write("file3.txt")
# f.close()
# print("files.zip file created successfully")


#To perform unzip operation
# f=ZipFile("files.zip","r",ZIP_STORED)

# names=f.namelist()


#Ex:
# from zipfile import *
# f=ZipFile("files.zip",'r',ZIP_STORED)
# names=f.namelist()
# for name in names:
#     print("File Name:",name)
#     print("The Content of this file is:")
#     f1=open(name,'r')
#     print(f1.read())
#     print()


#To know Current Working Directory
# import os
# cwd=os.getcwd()
# print("Current Working Directory:",cwd)


# To create a sub directory in the current working directory:
# import os
# os.mkdir("mysub")
# print("mysub directory created in cwd")


# To create multiple directories like sub1 in that sub2 in that sub3:
# import os
# os.makedirs("sub1/sub2/sub3")
# print("sub1 and in that sub2 and in that sub3 directories created")

# To remove a directory:
# import os
# os.rmdir("mysub/mysub2")
# print("mysub2 directory deleted")


# To remove multiple directories in the path:
# import os
# os.removedirs("sub1/sub2/sub3")
# print("All 3 directories sub1,sub2 and sub3 removed")


# To rename a directory:
# import os
# os.rename("mysub","newdir")
# print("mysub directory renamed to newdir")

#To know contents of directory:
# import os
# print(os.listdir(".")) 

#To know contents of directory including sub directories:
# os.walk(path,topdown=True,onerror=None,followlinks=False)

# To display all contents of Current working directory including sub directories:
# import os 
# for dirpath,dirnames,filenames in os.walk('.'):
#     print("Current Directory Path:",dirpath) 
#     print("Directories:",dirnames) 
#     print("Files:",filenames) 
#     print()

#Ex:
# import os
# os.system("dir *.py")
# os.system("py abc.py")

# How to get information about a File:
# stats = os.stat("abc.txt")

#To print all statistics of file abc.txt
# import os
# stats=os.stat("abc.txt")
# print(stats)

#To print specified properties:
# import os 
# from datetime import * 
# stats=os.stat("abc.txt") 
# print("File Size in Bytes:",stats.st_size) 
# print("File Last Accessed Time:",datetime.fromtimestamp(stats.st_atime)) 
# print("File Last Modified Time:",datetime.fromtimestamp(stats.st_mtime)) 