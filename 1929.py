#https://www.acmicpc.net/problem/1929

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
    
line=input().split()
M=int(line[0])
N=int(line[1])

for x in range(M,N+1):
    if isPrime(x):
        print(x)
