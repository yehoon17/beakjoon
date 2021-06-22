#https://www.acmicpc.net/problem/9012

import sys

N=int(sys.stdin.readline().strip())

for i in range(N):
    line=sys.stdin.readline().strip()
    l=[]
    flag=True
    for j in range(len(line)):
        if not flag:
            break
        if line[j]=='(':
            l.append(1)
        if line[j]==')':
            if len(l)>0:
                l.pop()
            else:
                flag=False
                break
    if len(l)>0:
        flag=False
    if flag:
        print('YES')
    else:
        print('NO')
        
