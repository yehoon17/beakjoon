#https://www.acmicpc.net/problem/2581

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

N=int(input())
M=int(input())
sum=0
min=10001
for x in range(N,M+1):
    if isPrime(x):
        sum+=x
        if min>x:
            min=x
if sum==0:
    print(-1)
else:
    print(sum)
    print(min)
            
