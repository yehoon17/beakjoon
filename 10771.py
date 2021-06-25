#https://www.acmicpc.net/problem/10771

import sys

M=int(sys.stdin.readline())
time=0
friends={}
for _ in range(M):
    C,X=sys.stdin.readline().split()
    X=int(X)
    if C=='W':
        time+=X-1
        continue
    if X not in friends:
        friends[X]=[time,0,False]
    else:
        if C=='S':
            friends[X][1]+=time-friends[X][0]
            friends[X][2]=True
        else:
            friends[X][0]=time
            friends[X][2]=False
    time+=1
for x in sorted(friends.keys()):
    if friends[x][2]:
        print(x,friends[x][1])
    else:
        print(x,-1)
    
