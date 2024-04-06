#https://www.acmicpc.net/problem/20291

import sys

N=int(sys.stdin.readline())
f=sorted([sys.stdin.readline().strip().split('.')[1] for _ in range(N)])
count=0
for i in range(N):
    if f[i]!=f[i-1]:
        if i>0:
            print(f[i-1],count)
        count=1
    else:
        count+=1
print(f[-1],count)
        
