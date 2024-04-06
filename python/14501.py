#https://www.acmicpc.net/problem/14501

import sys

def cal(N,profit,i,time,earn):
    if i+time<=N:
        max=0
        for j in range(i+time,N):
            if max<profit[j]:
                max=profit[j]
        profit[i]=earn+max
    

N=int(sys.stdin.readline())
schedule=[]
for i in range(N):
    schedule.append(list(map(int,sys.stdin.readline().split())))

profit=[0]*(N+1)
max=0
for i in range(N-1,-1,-1):
    cal(N,profit,i,*schedule[i])
    if max<profit[i]:
        max=profit[i]

print(max)
