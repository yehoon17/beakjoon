#https://www.acmicpc.net/problem/14891

import sys

def spin(gears,info,spun):
    index=info[0]-1
    temp=gears[index].copy()
    
    #spin
    if info[1]==1:
        for i in range(8):
            gears[index][i]=temp[i-1]
    else:
        for i in range(8):
            gears[index][i-1]=temp[i]
    spun[index]=True

    #check neighbor
    for i in (-1,1):
        if 0<=index+i and index+i<4:
            if not spun[index+i]:
                if temp[4-i*2]!=gears[index+i][4+i*2]:
                    spin(gears,[index+1+i,info[1]*-1],spun)
                
            

    

gears=[]
for i in range(4):
    gears.append(list(sys.stdin.readline().strip()))

K=int(sys.stdin.readline())
for i in range(K):
    spun=[False]*4
    spin(gears,list(map(int,sys.stdin.readline().split())),spun)

score=0

for i in range(4):
    if gears[i][0]=='1':
        score+=2**i

print(score)
