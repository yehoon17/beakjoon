#https://www.acmicpc.net/problem/14503

import sys

def check(N,M,r,c,d,room):
    for k in range(4):
        i,j=0,0
        d=(d-1)%4
        if d==0:
            i=-1
        elif d==1:
            j=1
        elif d==2:
            i=1
        elif d==3:
            j=-1
            
        if room[r+i][c+j]==0:
            operate(N,M,r+i,c+j,d,room)
            break
    else:
        if room[r-i][c-j]==-1:
            check(N,M,r-i,c-j,d,room)
        

def operate(N,M,r,c,d,room):
    #direction 0:N, 1:E, 2:S, 3:W
    
    #clean
    room[r][c]=-1

    #check
    check(N,M,r,c,d,room)
            
    


N,M=map(int,sys.stdin.readline().split())
r,c,d=map(int,sys.stdin.readline().split())
room=[]
for i in range(N):
    room.append(list(map(int,sys.stdin.readline().split())))

operate(N,M,r,c,d,room)

count=0

for i in range(N):
    for j in range(M):
        if room[i][j]==-1:
            count+=1

print(count)
