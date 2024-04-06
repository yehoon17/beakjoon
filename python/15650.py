#https://www.acmicpc.net/problem/15650

import sys

def combin(n,m):
    l=[]
    if m==1:
        for i in range(1,n+1):
            l.append([i])
        return l
    elif n==m:
        return [list(range(1,n+1))]
    for i in range(1,n+1):
        temp=combin(n-i,m-1)
        for j in range(len(temp)):
            for k in range(len(temp[j])):
                temp[j][k]+=i
            temp[j]=[i]+temp[j]
        l+=temp
    return l


line=sys.stdin.readline().strip().split()
l=combin(int(line[0]),int(line[1]))
for c in l:
    print(*c)
