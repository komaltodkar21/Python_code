# # dictionary comprehensions
# l=[1,2,3,4,5]
# d={i:i*i for i in l}
# print(d)

# squares={x:x*x for x in range(1,6)}
# print(squares)

# doubles={x:2*x for x in range(1,6)}
# print(doubles)

#copy
# cars={"Maruti":"ciaz","Hyndai":"Verna","Honda":"Amaze"}
# newcars={k:v for (k,v) in cars.items()}
# print(newcars)

# cars={"Maruti":"ciaz","Hyndai":"Verna","Honda":"Amaze"}
# newcars={}
# for (k,v) in cars.items():
#     newcars[k]=v
# print(newcars)

# dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
# double_dict1={k:v*2 for (k,v) in dict1.items()}
# print(double_dict1)

# dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
# double_dict1={k*2:v for (k,v) in dict1.items()}
# print(double_dict1)

#take string and count how many times each letter is occuring
# str=input("Type a string:")
# mydict={ch:str.count(ch) for ch in str}
# for k,v in mydict.items():
#     print(k,":",v)


# dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
# dict2={k*2:v for (k,v) in dict1.items() if v>2}
# print(dict2)


# dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
# dict2={k:v*2 for (k,v) in dict1.items() if v>2}
# print(dict2)


# dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
# dict2={k:'even' if v%2==0 else 'odd' for (k,v) in dict1.items()}
# print(dict2)

#restrictions on keys
#keys can be integer,float,boolean,str, tuple
#duplicates are not allowed if present second overrides first
#neither list or another dictionary can serve as key because keys are immutable

#no ristrictions on values
#values can be integer,float,boolean,str,tuple,list, another dictionary
# duplicates are allowed 


# s='komal todkar'
# dict={i:s.count(i) for i in s}
# print(dict)


# l1=[2,4,6,8]
# l2=[3,5,7,9]
# for i in range(len(l1)):
#     print(l1[i],l2[i])
    
# dict={l1[i]:l2[i] for i in range(len(l1))}
# print(dict)


# Program:
# d={5:'java',10:'python'}
# d[15]='django'
# print(d)

# d={"a":50,"b":60,"c":500}
# for key in d.items():
#     print(key)

# for value in d.items():
#     print(value)

# for value in d.items():
#     print(value)
# o/p:
# {5: 'java', 10: 'python', 15: 'django'}
# ('a', 50)
# ('b', 60)
# ('c', 500)
# ('a', 50)
# ('b', 60)
# ('c', 500)
# a
# 50
# b
# 60
# c
# 500

# Program:
# mh=['mumbai','pune']
# jh=['ranchi','lohardaga']
# india={'Maharashtra':mh, 'Jharkhand':jh}
# for key,value in india.items():
#     print(key)
#     for city in value:
#         print(city)
# o/p:
# Maharashtra
# mumbai
# pune
# Jharkhand
# ranchi
# lohardaga

# Program:
# mh=['mumbai','pune']
# jh=['ranchi','lohardaga']
# india={'Maharashtra':mh, 'Jharkhand':jh}
# for k,v in india.items():
#     print(k)
#     print(v)
# o/p:
# Maharashtra
# ['mumbai', 'pune']
# Jharkhand
# ['ranchi', 'lohardaga']