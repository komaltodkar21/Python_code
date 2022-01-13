# #list comprehensions
# l=[1,2,3,4,5]
# b=[i*i for i in l]
# print(b)

# l=[1,2,3,4,5]
# c=[i+1 for i in l]
# print(c)

#print words of a string in a list
# text=input("Type of string:")
# upperlist=[x.upper() for x in text.split()]
# print(upperlist)

#accept 5 intergers from user and store them in a list
#now display the list and sum of the elements
# text=input("Enter 5 integers:")
# mynum=[int(x) for x in text.split()]

# print("List is:",mynum)
# print("Sum is:",sum(mynum))


#using for loop
# mynum=[]
# text=input("Enter 5 integers:")
# for x in text.split():
#     mynum.append(int(x))

# print("List is:",mynum)
# print("Sum is:",sum(mynum))



#print square of odd numbers from 1 to 5 in list.
# squarelist=[x**2 for x in range(1,6) if x%2!=0]
# print(squarelist)

#remove vowels & split each character of a string in a list
# def removevowels(text):
#     mylist=[x for x in text if x not in "aeiou"]
#     return mylist

# text=input("Type a string:")
# finallist=removevowels(text)
# print(finallist)


#using for loop
# def removevowels(text):
#     mylist=[]
#     for x in text:
#         if x not in "aeiou":
#             mylist.append(x)
#     return mylist

# text=input("Type a string:")
# finallist=removevowels(text)
# print(finallist)


#print numbers from the following list
# mylist=["bhopal",25,"$","hello",34,21,"indore",22]
# def get_numbers(mylist):
#     mynumberlist=[x for x in mylist if type(x) is int]
#     return mynumberlist

# print("Actual List")
# print(mylist)
# print("List with numbers only")
# mynumberlist=get_numbers(mylist)
# print(mynumberlist)

#get length of each word of any string in list format 
# def getlength(str):
#     mylist=[len(x) for x in str.split() if x!="the"]
#     return mylist

# text=input("Type a string:")
# mylist=getlength(text)
# print(mylist)


# multiple conditions in list comprehension
# program to produce square of only those numbers which are divisible by 2
# as well as 3 from 1 to 20, store them in list and print the list.
# mylist=[x**2 for x in range(1,21) if x%2==0 if x%3==0]
# print(mylist)

#using for loop
# mynums=[]
# for x in range(1,21):
#     if x%2==0:
#         if x%3==0:
#             mynums.append(x**2)
# print(mynums)


#get uppercase letters without any vowels
# def get_upper(text):
#     mylist=[x for x in text if 65<=ord(x)<=90 if x not in "AEIOU"]
#     return mylist

# text=input("Type a string:")
# mylist=get_upper(text)
# print(mylist)

#using logical and/or
# a=[1,2,3,4,5,6,7,8,9,10]
# b=[x for x in a if x%2==0 or x%3==0]
# print(b)

#remove max min element from list
# def remove_min_max(mylist):
#     mynewlist=[x for x in mylist if x!=min(mylist) and x!=max(mylist)]
#     return mynewlist

# a=[10,3,15,12,24,6,1,18]
# print("original list")
# print(a)
# print("After removing min and max element")
# print(remove_min_max(a))


#if-else
# mylist=["Even" if i%2==0 else "Odd" for i in range(1,11)]
# print(mylist)


#nested list comprehension
# a=[20,40,60]
# b=[2,4,6]
# c=[]
# for x in a:
#     for y in b:
#         c.append(x*y)
# print(c)


#flatten() - convert nested list to single list
# def flatten(mylist):
#     newlist=[y for x in mylist for y in x]
#     return newlist
# mylist=[[1,2,3],[4,5,6],[7,8]]
# print("Before calling flatten list is")
# print(mylist)
# newlist=flatten(mylist)
# print("After calling flatten list is")
# print(newlist)


# s=[x*x for x in range(1,11)]
# print(s)
# v=[2**x for x in range (1,6)]
# print(v)
# m=[x for x in s if x%2==0]
# print(m)

#print first letter of each element
# words=['Balaiah','Nag','Venkatesh','Chiranjeevi']
# I=[w[0] for w in words]
# print(I)


# n1=[10,20,30,40]
# n2=[30,40,50,60]
# n3=[i for i in n1 if i not in n2]
# print(n3)
# n4=[i for i in n1 if i in n2]   # comman elements present in n1 and n2
# print(n4)


# words="the quick brown fox jumps over the lazy dog".split()
# print(words)
# I=[[w.upper(),len(w)] for w in words]
# print(I)

#display unique vowels present in the given word
# vowels=['a','e','i','o','u']
# word=input("Enter the word to search for vowels:")
# found=[]
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# print(found)
# print("The number of different vowels present in",word,"is",len(found))


#tuple comprehension is not supported by python.