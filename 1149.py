#https://www.acmicpc.net/problem/1149

import sys

def get_min(c,h):
    for i in range(3):
        min=c[i-1]
        if min>c[i-2]:
            min=c[i-2]
        h[i]+=min
    return h


N=int(sys.stdin.readline().strip())

cost=[0,0,0]
for i in range(N):
    house=list(map(int,sys.stdin.readline().strip().split()))
    cost=get_min(cost,house)

min=cost[0]
for i in range(1,3):
    if min>cost[i]:
        min=cost[i]

print(min)
