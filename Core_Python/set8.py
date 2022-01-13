# Program:

# s={1,2,3,4,5}
# s.add(10)         #use add instead of append
# print(s)
# s.update(50)    #int object is not iterable
# s.update("komal")
# print(s)

# s={1,2,3,4,5}
# s.update(range(1,10,2))  #add these numbers
# print(s)

# s={1,2,3,4,5}
# s1=s.copy()
# print(s1)

# s={1,2,3,4,5}
# s1=s.pop()     #returns some random element from the list
# print(s1)      #set doesnot support pop

# s={1,2,3,4,5}
# s.remove(3)
# print(s)


# s={1,2,3,4,5}
# s.remove(30)   #if value is not present error
# print(s)


# s1={6,8,5,4}
# s1.discard(70)  #if no value no error print as it is
# print(s1)
# s1.discard(8)
# print(s1)
# s1.discard(40)  #no error
# print(s1)

# s1.clear()
# print(s1)     #set()

# s2={7,8,5,3}
# print(s2)
# s2.pop()        #set doesnot support pop
# print(s2)       #it pops any random element from the list


# Program:
# s1={3,4,5,6}
# s2={5,6,7,8}
# print(s1.union(s2))   #all unique elements
# print(s1|s2)          #alternative for union

# print(s1.intersection(s2))  #comman elements
# print(s1&s2)                #alternative for intersection

# print(s1.difference(s2))
# print(s1-s2)
# print(s2.difference(s1))
# print(s2-s1)

# print(s1^s2)     #selected difference/all uncommans

# s1={5,6}
# s2={5,6,7,8}
# print(s1.issubset(s2))
# print(s2.issubset(s1))
# print(s2.issuperset(s1))
# print(s1.issuperset(s2))