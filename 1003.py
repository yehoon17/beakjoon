#https://www.acmicpc.net/problem/1003

import sys

def fibo(N,a,b):
    if N==0:
        return b,a
    if N==1:
        return a,b
    else:
        return fibo(N-1,b,a+b)    



N=int(sys.stdin.readline().strip())
for i in range(N):
    x=int(sys.stdin.readline().strip())
    print(*fibo(x,0,1))
