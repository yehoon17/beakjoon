#https://www.acmicpc.net/problem/6603

import sys

def dfs(n,k,num,li):
    if n==0:
        print(*li)
    else:
        for i in range(k-n+1):
            li.append(num[i])
            dfs(n-1,k-1-i,num[i+1:],li)
            li.pop()
    
while True:
    line=list(map(int,sys.stdin.readline().split()))
    if line==[0]:
        break
    k=line[0]
    num=line[1:]
    dfs(6,k,num,[])
    print('')

    
