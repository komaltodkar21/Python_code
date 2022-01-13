#pattern printing
# for i in range(1,5):
#     x=i
#     for j in range(1,i+1):
#         print("*", end=' ')
#     print('')
    
# for i in range(3,0,-1):
#     x=i-1
#     for j in range(1,i+1):
#         print("*", end=' ')
#     print('')

#constructor
class Student():
    def __init__(self,x,y):
        print('cont of stu')
        self.x=x
        self.y=y
    
    def add(self,z):
        print(self.x+self.y+z)


s=Student(10,20)
print(s.x)
print(s.y)
s.add(30)



#generator
# def add(l):
#     sum=0
#     for i in l:
#         yield sum
#         sum=sum+i

# a=add([1,2,3,4,5])

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# print(type(a))

def check(func):
    def inner(a,b):
        if b==0:
            print("invalid inputs")
        else:
            func(a,b)
            print("succesful")
    return inner

@check
def div(a,b):
    print(a/b)
div(10,5)
