#find sum of all mumbers
def find_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum

if __name__=='__main__':
    print(find_sum(5))

#using recursion
def find_sum(n):
    if n==1:
        return 1
    return n + find_sum(n-1)

if __name__=='__main__':
    print(find_sum(6))


#fibonacci series
# 0,1,1,2,3,5,8
# ---------------
# 0,1,2,3,4,5,6

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)  

if __name__=='__main__':
    print(fib(6))
