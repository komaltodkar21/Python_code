'''
list is mutable
tuple is immutable
it is a sequence order (indexing)
'''

# a=[2,3,4,5,7]
# for i in a:
#     print(i)        #(use for loop to retrive elements)
# print("first loop ends")
# for i in range(len(a)):
#     print(i)
# print("second loop ends")


# Program: To find greatest number from the list
# a=[11,4,17,5,8,16]
# k=0
# for i in range(len(a)):
#     #print(a[i])


#     if a[i]>k:               #smallest- a[i]<k 
#         k=a[i]
# print(k)

# OR

# a=[11,4,17,5,8,16]
# k=a[0]
# for i in a:
#     if i<k:
#         k=i

# print(k)


# Program: elements_less_than_5
# a=[2,3,5,7,4]
# print("elements less than 5 are: ")
# b=[]
# for i in a:
#     if i<5:
#         b.append(i)
# print(b)


# Program: list_of_less_than_x
# x=int(input("enter any number:"))
# a=[]
# for i in range(x):
#     a.append(i)
#
# print(a)


# Program: uncommon_elements
# a=[4,3,6,7,8,5,11,12]
# b=[1,2,3,4,5,6,7,8,9,10]
# c=[]
# for i in a:
#     for j in b:
#         if j==i:
#             c.append(j)

# print("comman elements are: ")
# print(c)

# x=[]
# for i in a:        
#     if i not in c:
#         x.append(i)

#print(x)
        

# y=[]
# for j in b:        
#     if j not in c:
#         y.append(j)

#print(y)

# c=[]
# for m in x:
#     c.append(m)

#print(c)

# for n in y:
#     c.append(n)

# print("uncomman elements are: ")
# print(c)


# Program: difference_of_consicutive_numbers
# a=[2,2,3,1,2,3]
# n=[]
# k=a[0]
# for i in range(1,len(a)):
#     #print(a[i])
#     x=k-a[i]
#     n.append(x)
#     k=a[i]
#  print(n)


#fuctions of list
# a=[2,5,3,6,8,0]
# print(len(a))
# print(max(a))
# print(min(a))
# print(sum(a))
# print(sorted(a))
# print(list(a))
# print(any(a))   # if any 1 is true
# print(all(a))   # if all are true

#methods of list
# a=[1,2,3,4,5]
# a.append(6)   # to add single element
# print(a)

# for i in a:
#     print(i*i)

# b=[6,7,8,9]
# a.extend(b)   # to add any itterable(can apply for loop in it)
# print(a)

# a.insert(3,17)
# print(a)

# print(a.index(4))  #(element to get index)

# print(a.count(8))

# a.copy()
# print(a)

# a.sort()
# print(a)

# a.sort(reverse=True)
# print(a)

# a.sorted()
# print(a)

# a=sorted(a,reverse=True)
# print(a)

# a.remove(3)
# print(a)

# a.pop()  # removes last element
# print(a)

# a.clear()
# print(a)

# a.reverse()
# print(a)
# a.sort(reverse=True)

# print(a)
# a.reverse()

#del v/s pop v/s remove


# #Remove Duplicates
# program to eliminate duplicates present in the list
# list1=[1,2,3,3,4,4,5,6,6,7,8]
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)


#slicing
# a=[11,12,13,14,15]
# print(a[0:3])
# print(a[1:])
# print(a[::-1])
# print(a[0])
# for i in range(len(a)):
#     print(a[i])

#accessiong list elements using while loop
# a=[11,12,13,14,15]
# s=len(a)
# i=0
# while i<=s-1:
#     print(a[i])
#     i=i+1


# print(a[4:])
# print(a[-1])
# print(a[-4:-1])


#traverse the list in reverse order dont use slice operator use range
# l=[10,20,30,40,50]
# n=len(l)
# for i in range(n-1,-1,-1):
#     print(l[i])


#accept 5 intergers from user, store them in a list, display these integers and also display their sum
# n=[]
# i=1
# while i<=5:
#     x=int(input("Enter "+str(i)+" elements:"))
#     n.append(x)
#     i=i+1
# print("The list is:")
# sum=0
# for j in n:
#     print(j)
#     sum+=j
# print("Sum is",sum)


#mutability
# n=[10,20,30,40]
# print(n)
# n[1]=777
# print(n)

#modifying
# sports=["cricket","hockey","football","snooker"]
# print(sports)
# sports[1:3]=["batminton","tennis"]
# print(sports)

#del
# sports=["cricket","hockey","football","snooker"]
# print(sports)
# del sports[2]
# print(sports)

#deleting multiple items by assigning empty list
# sports=["cricket","hockey","football","snooker"]
# print(sports)
# sports[1:3]=[]
# print(sports)

#passing slice to del operator
# sports=["cricket","hockey","football","snooker"]
# print(sports)
# del sports[1:3]
# print(sports)

#appending or prepending
# outdoor=["cricket","hockey","football"]
# indoor=["carrom","chess","table-tennis"]
# allsports=outdoor+indoor
# print(allsports)

# sports=["cricket","hockey","football"]
# sports=sports+list("boxing")
# print(sports)

# sports=["cricket","hockey","football"]
# sports=sports+["boxing"]
# print(sports)

# sports=["cricket","hockey","football"]
# sports=sports*3 
# print(sports)


#produce square of only those numbers which are divisible by 2 as well as 3 from 1 t0 20,
#store them in a list print the list
# mylist=[x**2 for x in range(1,21) if x%2==0 if x%3==0]
# print(mylist) 

#using for loop
# mynum=[]
# for x in range(1,21):
#     if x%2==0:
#         if x%3==0:
#             mynum.append(x**2)
# print(mynum)