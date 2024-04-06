#https://www.acmicpc.net/problem/2579

import sys

def get_max(s,m):
    l=[]
    if m[1]>m[2]:
        l.append(m[1])
    else:
        l.append(m[2])
    l.append(m[0]+s)
    l.append(m[1]+s)
    return l
    

N=int(sys.stdin.readline().strip())
max=[0]*3
for i in range(1,N+1):
    step=int(sys.stdin.readline().strip())
    max=get_max(step,max)
if max[1]>max[2]:
    print(max[1])
else:
    print(max[2])
