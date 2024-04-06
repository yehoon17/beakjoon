#https://www.acmicpc.net/problem/20124

import sys

N=int(sys.stdin.readline())
li=[]
for i in range(N):
    line=sys.stdin.readline().split()
    line[1]=int(line[1])
    li.append(line)
    
li.sort(key=lambda x:x[0])
li.sort(key=lambda x:x[1],reverse=True)
print(li[0][0])
