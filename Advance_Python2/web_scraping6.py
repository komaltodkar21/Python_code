# Eg:
# import re,urllib 
# import urllib.request 
# sites="google rediff".split() 
# print(sites) 
# for s in sites: 
#     print("Searching...",s) 
#     u=urllib.request.urlopen("http://"+s+".com") 
#     text=u.read() 
#     title=re.findall("<title>.*</title>",str(text),re.I) 
#     print(title[0])


# Eg: Program to get all phone numbers of redbus.in by using web 
# scraping and regular expressions
# import re,urllib 
# import urllib.request 
# u=urllib.request.urlopen("https://www.redbus.in/info/contactus") 
# text=u.read() 
# numbers=re.findall("[0-9-]{7}[0-9-]+",str(text),re.I) 
# for n in numbers:
#     print(n) 

# Q. Write a Python Program to check whether the given mail id is 
# valid gmail id or not?
# import re 
# s=input("Enter Mail id:") 
# m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s) 
# if m!=None: 
#     print("Valid Mail Id"); 
# else: 
#     print("Invalid Mail id") 


# Q. Write a python program to check whether given car registration 
# number is valid Telangana State Registration number or not?
# import re 
# s=input("Enter Vehicle Registration Number:") 
# m=re.fullmatch("TS[012][0-9][A-Z]{2}\d{4}",s) 
# if m!=None: 
#     print("Valid Vehicle Registration Number"); 
# else: 
#     print("Invalid Vehicle Registration Number") 


# Write a Python Program to check whether the given mobile number
# is valid OR not (10 digit OR 11 digit OR 12 digit)
# import re
# n=input("Enter mobile number:")
# m=re.fullmatch("(0|91)?[7-9][0-9]{9}",s)
# if m!= None:
#     print("Valid Mobile Number")
# else:
#     print("Invalid Mobile Number")