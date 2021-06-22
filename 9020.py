#https://www.acmicpc.net/problem/9020

def isPrime(x):
    if x==1:
        return False
    for d in range(1,int(x**0.5)):
        if x==d+1:
            continue
        if x%(d+1)==0:
            return False
    else:
        return True

T=int(input())
for i in range(T):
    n=int(input())
    mid=int(n/2)
    for j in range(mid):
        if isPrime(mid-j) and isPrime(mid+j):
            a=mid-j
            b=mid+j
            break
    print(a,b)
    
