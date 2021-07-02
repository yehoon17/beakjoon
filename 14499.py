#https://www.acmicpc.net/problem/14499

import sys

def rotate(dice,command):
    #아래:0, 동쪽:1, 서쪽:2, 북쪽:3, 남쪽:4, 위:5
    opposite=command+command%2*2-1
    temp=dice[0]
    dice[0]=dice[command]
    dice[command]=dice[5]
    dice[5]=dice[opposite]
    dice[opposite]=temp

    
def roll(dice,position,command,N,M,numbers):   
    x=position[0]
    y=position[1]
    if command==1:
        y+=1
    elif command==2:
        y-=1
    elif command==3:
        x-=1
    elif command==4:
        x+=1
    if x<0 or x>=N or y<0 or y>=M:
        return -1
    position[0]=x
    position[1]=y
    rotate(dice,command)

    if numbers[x][y]==0:
        numbers[x][y]=dice[0]
    else:
        dice[0]=numbers[x][y]
        numbers[x][y]=0
    return dice[5]

N,M,*position,K=map(int,sys.stdin.readline().split())
numbers=[]
for i in range(N):
    numbers.append(list(map(int,sys.stdin.readline().split())))
commands=list(map(int,sys.stdin.readline().split()))
dice=[0,0,0,0,0,0]

for command in commands:
    temp=roll(dice,position,command,N,M,numbers)
    if temp>=0:
        print(temp)
