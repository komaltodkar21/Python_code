# d={}             #empty dictionary
# d=dict{}
# d=dict({100:"durga",200:"ravi"})   #creates dictionary with specified elements
# d=dict([(100,"durga"),(200,"ravi")])  #creates dictionary with given list of tuple elements


# d={}
# d[100]="durga"
# d['name']="ravi"
# d[300.50]="shiva"
# print(d)

#dictionary values can be a list
# d={'Rahul':['C','C++'],'Ajay':['Java','C','Python'],'Neeraj':['Oracle','Python']}

#create a dictionary with elements
# d=dict({1:'apple',2:'ball'})

#create a dictionary with other sequences
# d=dict([(1,'apple'),(2,'ball')])

#accessing individual elements   (starts with 1)
# d={1:'Amit',2:'Brajesh',3:'Chetan',4:'Deepak',5:'Neeraj'}
# print(d[3])        #Chetan
# print(d.get(3))    #Chetan  


#iterate only on keys
# d={1:'Amit',2:'Brajesh',3:'Chetan',4:'Deepak',5:'Neeraj'}
# for roll in d:
#     print("Roll:",roll)

# d={1:'Amit',2:'Brajesh',3:'Chetan',4:'Deepak',5:'Neeraj'}
# for roll in d.keys():
#     print("Roll:",roll)


#get values
# d={1:'Amit',2:'Brajesh',3:'Chetan',4:'Deepak',5:'Neeraj'}
# for roll in d:
#     print("Roll:",roll,"Name:",d[roll])       #keys    values


# d={1:'Amit',2:'Brajesh',3:'Chetan',4:'Deepak',5:'Neeraj'}
# for roll,name in d.items():
#     print("Roll:",roll,"Name:",name)


# d={1:'Amit',2:'Brajesh',3:'Chetan',4:'Deepak',5:'Neeraj'}
# for name in d.values():
#     print("Name:",name)


#output is in the same order as data is inserted
#dictionaries remember the order of items inserted.


#updating a dictionary
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d)
# d[400]="pavan"       #added
# print(d)
# d[100]="sunny"       #updated
# print(d)


#using update() method
# d1={1:'Amit',2:'Brajesh',3:'Chetan',4:'Deepak',5:'Neeraj'}
# d2={100:"durga",200:"ravi",300:"shiva"}
# d1.update(d2)
# print(d1)


#pop()
# d.pop(key,[default])

# months={"Jan":31,"Feb":28,"Mar":3,"Apr":30,"May":31,"Jun":30}
# print(months)
# print(months.pop("Jun"))       #pops its value
# print(months)                  #pops that item    
# print(months.pop("Jul","Not Found"))
# print(months.pop("Jul"))


#popitem()
# months={"Jan":31,"Feb":28,"Mar":3}
# print(months)
# print(months.popitem())
# print(months)
# print(months.popitem())
# print(months)
# print(months.popitem())

#del operator - we have to pass key as argument
# months={"Jan":31,"Feb":28,"Mar":3}
# print(months)
# del months["Feb"]   
# print(months)

#we cannot use del to delete total dictionary
# months={"Jan":31,"Feb":28,"Mar":3}
# print(months)
# del months
# print(months)
# del months["Jan"]       #delets only particular item
# print(months)


# clear() clears all items
# months={"Jan":31,"Feb":28,"Mar":3}
# print(months)
# months.clear()   
# print(months)


#copy() vs =
#copy() - returns shallow copy of dictionary
# original={1:'one',2:'two'}
# new=original.copy()
# print('new:',new)
# print('original:',original)


# original={1:'one',2:'two'}
# new=original
# print('new:',new)
# print('original:',original)


# setdefault()
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.setdefault(400,"pavan"))
# print(d)
# print(d.setdefault(100,"sachin"))
# print(d)

#in And not in
# cars={"Maruti":"ciaz","Hyndai":"Verna","Honda":"Amaze"}
# print(cars)
# print("Hyundai is present:","Hyndai" in cars)
# print("Audi is present:","Audi" in cars)
# print("Renault not present:","Renault" not in cars)

#.items()
# d={100:"durga",200:"ravi",300:"shiva"}
# for k,v in d.items():
#     print(k,"_",v)

# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.keys())
# for k in d.keys():
#     print(k)

# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.values())
# for k in d.values():
#     print(k)

#functions of dictionary
# t1={"Jan":31,"Feb":28,"Mar":3,"Apr":30,"May":31,"Jun":30}
# print(len(t1))
# print(max(t1))
# print(min(t1))
# print(sorted(t1))
# print(any(t1))
# print(all(t1))

# months=dict(jan=31,Feb=28)
# print(type(months))
# print('months=',months)
# print(type(months))

# months=dict((('Jan',31),('Feb',28)))
# print('months=',months)

# months=dict({'Jan':31,'Feb':28})
# print('months=',months)

# months=dict(12)    #int object is not iterable
# print('months=',months)

#kwargs
# def addnos(x,y,z):
#     print("sum:",x+y+z)
# addnos(10,20,30)
# addnos(10,20,30,40,50)      #error


#args
# def addnos(*args):
#     sum=0
#     for x in args:
#         sum=sum+x
#     print("sum:",sum)
# addnos(10,20,30)
# addnos(10,20,30,40,50)


#kwargs
# def show_details(**data):
#     print("\n Data type of argument:",type(data))
#     for key,value in data.items():
#         print('{} is {}'.format(key,value))
#
# show_details(Firstname="Sachin",Lastname="Kapoor",Age=38,Phone=9826012345)
#
# show_details(Firstname="Amit",Lastname="Sharma",Email="amit@gmail.com",Country="India",Age=25,Phone=9893198931)

#copy()



# dict={'r':'red','y':'yellow','g':'green','b':'blue'}
# print(dict.get('r'))
# print(dict['r'])

# dict['r']='reddish'   #Update
# print(dict)
# dict['p']='pink'
# print(dict)

# for k in dict.keys():
#     print(k)

# for k in dict.values():
#     print(k)

# for k,v in dict.items():
#     print(k,v)

# dict={'r':'red','y':'yellow','g':'green','b':'blue'}
# dict2={'s':'school','c':'college'}
# dict.update(dict2)        #adding another dictionary
# print(dict)

# '''
# for removing last key and values from the dictionary popitem()
# '''
# dict.popitem()
# print(dict)

# dict.pop('g')
# print(dict)

# dict.clear()
# print(dict)