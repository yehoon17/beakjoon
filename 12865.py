#https://www.acmicpc.net/problem/12865

import sys

def solve(temp,W,V,K):
    for i in range(K,W-1,-1):
        if temp[i]<temp[i-W]+V:
            temp[i]=temp[i-W]+V
        

N,K=map(int,sys.stdin.readline().split())
##X=[list(map(int,sys.stdin.readline().split())) for i in range(N)]
temp=[0]*(K+1)
for i in range(N):
    W,V=map(int,sys.stdin.readline().split())
    solve(temp,W,V,K)

print(temp[K])
