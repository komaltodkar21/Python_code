# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'

# g=mygen()
# print(type(g))

# print(next(g))
# print(next(g))
# print(next(g))
# # print(next(g))

# Ex:
# def countdown(num):
#     print("Start Countdown")
#     while(num>0):
#         yield num
#         num=num-1

# values=countdown(5)
# for x in values:
#     print(x)

# To generate first n numbers
# def firstn(num):
#     n=1
#     while n<=num:
#         yield n
#         n=n+1

# values=firstn(5)
# for x in values:
#     print(x)

#fibonacci series
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for f in fib():
#     if f>100:
#         break
#     print(f)



#generator vs normal collections wrt performance
# import random
# import time

# names=['Sunny','Bunny','Chinny','Vinny']
# subjects=['Python','Java','Blockchain']

# def people_list(num_people):
#     results=[]
#     for i in range(num_people):
#         person={
#             'id':i,
#             'name':random.choice(names),
#             'subject':random.choice(subjects)
#         }
#     results.append(person)
#     return results

# def people_generator(num_people):
#     for i in range(num_people):
#         person={
#             'id':i,
#             'name':random.choice(names),
#             'major':random.choice(subjects)
#         }
    # yield person

# # t1=time.process_time()          #use process_time instead of clock
# # people=people_list(10000000)
# # t2=time.process_time()

# t1=time.process_time()
# people=people_generator(10000000)
# t2=time.process_time()

# print('Took{}'.format(t2-t1))



#Generator vs Normal Collections wrt Memory Utilization
#Normal collection
# I=[x*x for x in range(1000000000000000)]
# print(I[0])

#Generators
# g=(x*x for x in range(10000000000000))
# print(next(g))