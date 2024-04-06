#https://www.acmicpc.net/problem/15652

import sys

def per(n,m,max):
    l=[]
    if m==1:
        for i in range(max,n+1):
            l.append([i])
        return l
    else:
        for i in range(max,n+1):
            temp=per(n,m-1,i)
            for j in range(len(temp)):
                temp[j]=[i]+temp[j]
            l+=temp
        return l


#main
line=sys.stdin.readline().strip().split()
l=per(int(line[0]),int(line[1]),1)
for p in l:
    print(*p)
