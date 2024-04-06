#https://www.acmicpc.net/problem/1932

import sys

def get_max(f,m):
    for i in range(len(f)):
        if i==0:
            f[i]+=m[i]
        elif i==len(f)-1:
            f[i]+=m[i-1]
        else:           
            if m[i-1]<m[i]:
                f[i]+=m[i]
            else:
                f[i]+=m[i-1]
    return f

N=int(sys.stdin.readline().strip())
max=[0]
for i in range(1,N+1):
    floor=sys.stdin.readline().strip()
    floor=floor.split()
    for j in range(i):
        floor[j]=int(floor[j])
    max=get_max(floor,max)
answer=0
for x in max:
    if answer<x:
        answer=x
print(answer)
