# 1. compile()
# re module contains compile() function to compile a pattern into RegexObject.
# pattern = re.compile("ab")
# 2. finditer():
# Returns an Iterator object which yields Match object for every Match
# matcher = pattern.finditer("abaababa")

# On Match object we can call the following methods.
# 1. start() --> Returns start index of the match
# 2. end() --> Returns end+1 index of the match
# 3. group() --> Returns the matched string


# Eg:
# import re 
# count=0
# pattern=re.compile("ab") 
# matcher=pattern.finditer("abaababa") 
# for match in matcher: 
#     count+=1 
#     print(match.start(),"...",match.end(),"...",match.group()) 
# print("The number of occurrences: ",count) 


# Eg:
# import re 
# count=0 
# matcher=re.finditer("ab","abaababa") 
# for match in matcher: 
#     count+=1 
#     print(match.start(),"...",match.end(),"...",match.group()) 
# print("The number of occurrences: ",count)


# Character classes:
# We can use character classes to search a group of characters
# 1. [abc]===>Either a or b or c
# 2. [^abc] ===>Except a and b and c
# 3. [a-z]==>Any Lower case alphabet symbol
# 4. [A-Z]===>Any upper case alphabet symbol
# 5. [a-zA-Z]==>Any alphabet symbol
# 6. [0-9] Any digit from 0 to 9
# 7. [a-zA-Z0-9]==>Any alphanumeric character
# 8. [^a-zA-Z0-9]==>Except alphanumeric characters(Special Characters)


# Eg:
# import re 
# matcher=re.finditer("x","a7b@k9z") 
# for match in matcher: 
#     print(match.start(),"......",match.group())


# Pre defined Character classes:
# \s  Space character
# \S  Any character except space character
# \d  Any digit from 0 to 9
# \D  Any character except digit
# \w  Any word character [a-zA-Z0-9]
# \W  Any character except word character (Special Characters)
# .  Any character including special characters


# Eg:
# import re 
# matcher=re.finditer("x","a7b k@9z") 
# for match in matcher: 
#     print(match.start(),"......",match.group()) 


# Qunatifiers:
# We can use quantifiers to specify the number of occurrences to match.
# a  Exactly one 'a'
# a+  Atleast one 'a'
# a*  Any number of a's including zero number
# a?  Atmost one 'a' ie either zero number or one number
# a{m}  Exactly m number of a's
# a{m,n}  Minimum m number of a's and Maximum n number of a's
# Eg:
# import re 
# matcher=re.finditer("x","abaabaaab") 
# for match in matcher: 
#     print(match.start(),"......",match.group())



# Important functions of re module:
# 1. match()
# 2. fullmatch()
# 3. search()
# 4. findall()
# 5. finditer()
# 6. sub()
# 7. subn()
# 8. split()
# 9. compile()


# 1. match():
# Eg:
# import re
# s=input("Enter pattern to check: ")
# m=re.match(s,"abcabdefg")
# if m!= None:
#     print("Match is available at the beginning of the String")
#     print("Start Index:",m.start(), "and End Index:",m.end())
# else:
#     print("Match is not available at the beginning of the String")


# 2. fullmatch():
# Eg:
# import re 
# s=input("Enter pattern to check: ") 
# m=re.fullmatch(s,"ababab") 
# if m!= None: 
#     print("Full String Matched") 
# else: 
#     print("Full String not Matched") 


# 3. search():
# Eg:
# import re 
# s=input("Enter pattern to check: ") 
# m=re.search(s,"abaaaba") 
# if m!= None: 
#     print("Match is available") 
#     print("First Occurrence of match with start index:",m.start(),"and end index:",m.end()) 
# else:
#     print("Match is not available")


# 4. findall():
# To find all occurrences of the match.
# This function returns a list object which contains all occurrences.
# Eg:
# import re 
# l=re.findall("[0-9]","a7b9c5kz") 
# print(l)


# 5. finditer():
# Returns the iterator yielding a match object for each match.
# On each match object we can call start(), end() and group() functions.
# Eg:
# import re 
# itr=re.finditer("[a-z]","a7b9c5k8z") 
# for m in itr: 
#     print(m.start(),"...",m.end(),"...",m.group()) 


# 6. sub():
# sub means substitution or replacement
# re.sub(regex,replacement,targetstring)
# In the target string every matched pattern will be replaced with provided replacement.
# Eg:
# import re 
# s=re.sub("[a-z]","#","a7b9c5k8z") 
# print(s) 


# 7. subn():
# It is exactly same as sub except it can also returns the number of replacements.
# This function returns a tuple where first element is result string and second element is number of 
# replacements.
# (resultstring, number of replacements)
# Eg:
# import re 
# t=re.subn("[a-z]","#","a7b9c5k8z") 
# print(t) 
# print("The Result String:",t[0]) 
# print("The number of replacements:",t[1]) 


# 8. split():
# If we want to split the given target string according to a particular pattern then we should go for 
# split() function.
# This function returns list of all tokens.
# Eg:
# import re 
# l=re.split(",","sunny,bunny,chinny,vinny,pinny") 
# print(l) 
# for t in l: 
#     print(t) 



# Eg:
# import re 
# l=re.split("\.","www.durgasoft.com") 
# for t in l: 
#     print(t) 


# ^ symbol:
# We can use ^ symbol to check whether the given target string starts with our provided pattern or 
# not.
# Eg:
# res=re.search("^Learn",s)


# test.py:
# import re 
# s="Learning Python is Very Easy" 
# res=re.search("^Learn",s) 
# if res != None: 
#     print("Target String starts with Learn") 
# else: 
#     print("Target String Not starts with Learn") 

# $ symbol:
# We can use $ symbol to check whether the given target string ends with our provided pattern or 
# not
# Eg: res=re.search("Easy$",s)



# test.py:
# import re 
# s="Learning Python is Very Easy" 
# res=re.search("Easy$",s) 
# if res != None: 
#     print("Target String ends with Easy") 
# else: 
#     print("Target String Not ends with Easy") 


# Eg: res = re.search("easy$",s,re.IGNORECASE)
# test.py:
# import re 
# s="Learning Python is Very Easy" 
# res=re.search("easy$",s,re.IGNORECASE) 
# if res != None: 
#     print("Target String ends with Easy by ignoring case") 
# else: 
#     print("Target String Not ends with Easy by ignoring case") 


# Write a python program to check whether the given string is Yava 
# language identifier or not?
# import re 
# s=input("Enter Identifier:") 
# m=re.fullmatch("[a-k][0369][a-zA-Z0-9#]*",s) 
# if m!= None: 
#     print(s,"is valid Yava Identifier") 
# else: 
#     print(s,"is invalid Yava Identifier") 

# Write a Python Program to check whether the given number 
# is valid mobile number or not?
# import re 
# n=input("Enter number:") 
# m=re.fullmatch("[7-9]\d{9}",n) 
# if m!= None: 
#     print("Valid Mobile Number") 
# else: 
#     print("Invalid Mobile Number") 


# Write a python program to extract all mobile numbers present in 
# input.txt where numbers are mixed with normal text data
# import re 
# f1=open("input.txt","r") 
# f2=open("output.txt","w") 
# for line in f1: 
#     list=re.findall("[7-9]\d{9}",line) 
#     for n in list: 
#         f2.write(n+"\n") 
# print("Extracted all Mobile Numbers into output.txt") 
# f1.close()
# f2.close() 