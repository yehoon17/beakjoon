#https://www.acmicpc.net/problem/11650

import sys

def f1(e):
    return e[0]
def f2(e):
    return e[1]

N=int(sys.stdin.readline().strip())

l=[]
for i in range(N):
    line=sys.stdin.readline().strip().split()
    l.append([int(line[0]),int(line[1])])
    
l.sort(key=f2)
l.sort(key=f1)
    
for i in range(N):
    print(*l[i])
