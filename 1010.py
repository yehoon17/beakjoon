# https://www.acmicpc.net/problem/1010

import sys

T=int(sys.stdin.readline())
for i in range(T):
    N,M=map(int,sys.stdin.readline().split())
    a=b=1
    for x,y in zip(range(M-N+1,M+1),range(1,N+1)):
        a*=x
        b*=y
    print(a//b)
