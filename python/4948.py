#https://www.acmicpc.net/problem/4948

def isPrime(x,primes):
    for p in primes:
        if x<p**2:
            return True
        if x%p==0:
            return False
    else:
        return True


primes=[]
for x in range(2,123456*2+2):
    if isPrime(x,primes):
        primes.append(x)
        
while(True):
    N=int(input())
    if N==0:
        break
    start=0
    while(primes[start]<=N):
        start+=1
    end=start
    while(primes[end]<=2*N):
        end+=1
    print(end-start)
