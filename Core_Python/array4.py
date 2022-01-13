# Types of array
# One dimensional array - Single row Multiple columns
# [1,2,3,4,5]
# Multi-dimensional array - Multiple rows Multiple columns
# [1,2,3,4,5],
# [11,22,33,44,55]
# python doesnot support multi-dimensional array but we can
# create multidimentional array using third party packages like numpy.

# 1D array
# import array
# array_name=array.array("type_code",[elements])

# import array
# stu_roll=array.array('i',[101,102,103,104,105])

# accessing 1D array
# from array import *
# stu_roll=array('i',[101,102,103,104,105])
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[-2])
# print(stu_roll[2])

# import array
# stu_roll=array.array('i',[101,102,103,104,105])
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[-2])
# print(stu_roll[2])

# for
# from array import *
# stu_roll=array('i',[101,102,103,104,105])
# for i in stu_roll:
#     print(i)

# from array import *           #Important
# a=[101,102,103,104,105]
# stu_roll=array('i',a)
# for i in stu_roll:
#     print(i)

# using len
# from array import *
# stu_roll=array('i',[101,102,103,104,105])
# n=len(stu_roll)
# for i in range(n):
#     print(stu_roll[i])


#accessing array elements using while loop
#while accessing using index number always access with 0 not 1

# from array import array
# stu_roll=array('i',[101,102,103,104,105])
# n=len(stu_roll)
# i=0
# while(i<n):
#     print(stu_roll[i])
#     i+=1

# array append
# from array import array
# stu_roll=array('i',[101,102,103,104,105])
# n=len(stu_roll)
# i=0
# while(i<n):
#     print(stu_roll[i])
#     i+=1

# print("Array after append")
# stu_roll.append(106)
# print(stu_roll)
# n=len(stu_roll)
# i=0
# while(i<n):
#     print(stu_roll[i])
#     i+=1


# getting input from user using for loop   
# from array import array
# stu_roll=array('i',[])
# n=int(input("Enter number of elements: "))
#
# for i in range(n):
#     stu_roll.append(int(input("Enter element:")))
#
# for i in range(len(stu_roll)):
#     print(stu_roll[i])


#getting input from users using while
# from array import *
# stu_roll = array('i',[])
# n=int(input("Enter number of elements: "))
# i=0
# j=0
# while i<n:
#     stu_roll.append(int(input("Enter element:")))
#     i+=1

# while(j<len(stu_roll)):
#     print(stu_roll[j])
#     j+=1

# insert
# from array import *
# stu_roll = array('i',[101,102,103,104,105])
# n=len(stu_roll)
# i=0
# while(i<n):
#     print(stu_roll[i])
#     i+=1

# print("Array after insert")
# stu_roll.insert(1,106)
# stu_roll.insert(3,107)
# n=len(stu_roll)
# i=0
# while(i<n):
#     print(stu_roll[i])
#     i+=1


#pop/remove/reverse
# from array import *
# stu_roll = array('i',[101,102,103,104,105])
# n=len(stu_roll)
# i=0
# while(i<n):
#     print(stu_roll[i])
#     i+=1

# print("Array after pop")     #print("Array after remove")    #print("Array after reverse") 
# stu_roll.pop()               #stu_roll.remove(101)           #stu_roll.reverse()
# n=len(stu_roll)
# i=0
# while(i<n):
#     print(stu_roll[i])
#     i+=1

#index
# from array import *
# stu_roll=array('i',[101,102,103,104,105])
# print(stu_roll.index(104))

#extend
# from array import *
# stu_roll=array('i',[101,102,103,104,105])
# arr=array('i',[106,107,108])
# n=len(stu_roll)
# i=0
# while(i<n):
#     print(stu_roll[i])
#     i+=1

# print("Array after extend")
# stu_roll.extend(arr)
# n=len(stu_roll)
# i=0
# while(i<n):
#     print(stu_roll[i])
#     i+=1


#slicing
# from array import *
# stu_roll=array('i',[101,102,103,104,105,106,107])
# print("Original Array")
# n=len(stu_roll)
# for i in range(n):
#     print(i, "=", stu_roll[i])

# print("************************")
# a=stu_roll[-5:-3]
# for i in a:
#     print(i)