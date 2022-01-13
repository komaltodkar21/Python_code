# string interpolation
# name="komal"
# age="34"
# print("My name is",name,"and my age is",age)
# print("My name is {0} and my age is {1}".format(name,age))
# print(f"My name is {name} and my age is {age}")

# formatting the string - for default, positional, keyword arguments

#IMP
#access each charecter of string using while loop
# s="Learning Python is very easy!!!"
# n=len(s)
# i=0
# print("forward direction")
# while i<n:
#     print(s[i],end='')
#     i+=1
# print("\nbackward direction")
# # rs=""
# # while n>0:
# #     rs=str[n-1]
# #     count=count-1
# # print(rs)

#using for loop
# s="Learning Python is very easy!!!"
# print("forward direction")
# for i in s:
#     print(i,end='')

# print("\nforward direction")
# for i in s[::]:
#     print(i,end='')

# print("\nbackward direction")
# for i in s[::-1]:
#     print(i,end='')

#strip() - removes spaces
# text=" Good Morning "
# newtext=text.strip()
# print("original text:"+text+"done!")
# print("New text:"+newtext+"done!")
# newtext=text.rstrip()
# print("New text:"+newtext+"done!")
# newtext=text.lstrip()
# print("New text:"+newtext+"done!")

#split()
# text='Live and let live'
# print(text.split())
# grocery='Milk,Butter,Bread'
# print(grocery.split(","))
# print(grocery.split(":"))


# s="durga software solutions"
# I=s.split()
# for x in I:
#     print(x)

# s="22-02-2018"
# I=s.split('-')
# for x in I:
#     print(x)


#join() - list object has no attribute join
# mylist=["C","C++","Java","Python"]
# s="->"
# print(s.join(mylist))


# name="durga"
# salary="10000"
# age=48
# print("{}'s salary is  {} and his age is {}".format(name,salary,age))
# print("{0}'s salary is  {1} and his age is {2}".format(name,salary,age))
# print("{x}'s salary is  {y} and his age is {z}".format(z=name,y=salary,x=age))