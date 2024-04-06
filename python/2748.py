#https://www.acmicpc.net/problem/2748

import sys

def fibo(N,a,b):
    if N==0:
        return a
    if N==1:
        return b
    else:
        return fibo(N-1,b,a+b)

N=int(sys.stdin.readline().strip())
print(fibo(N,0,1))
