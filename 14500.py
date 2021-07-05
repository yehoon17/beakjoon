#https://www.acmicpc.net/problem/14500

import sys

N,M=map(int,sys.stdin.readline().split())
board=[]
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

max=0

for i in range(N-3):
    for j in range(M):
        sum=board[i][j]+board[i+1][j]+board[i+2][j]+board[i+3][j]
        if max<sum:
            max=sum

for i in range(N):
    for j in range(M-3):
        sum=board[i][j]+board[i][j+1]+board[i][j+2]+board[i][j+3]
        if max<sum:
            max=sum

for i in range(N-1):
    for j in range(M-1):
        sum=board[i][j]+board[i+1][j]+board[i][j+1]+board[i+1][j+1]
        if max<sum:
            max=sum

for i in range(N-2):
    for j in range(M):
        temp=0
        sum=board[i][j]+board[i+1][j]+board[i+2][j]
        if j<M-1:
            for k in range(3):
                if temp<board[i+k][j+1]:
                    temp=board[i+k][j+1]
        if j>0:
            for k in range(3):
                if temp<board[i+k][j-1]:
                    temp=board[i+k][j-1]
        if max<sum+temp:
            max=sum+temp

for i in range(N):
    for j in range(M-2):
        temp=0
        sum=board[i][j]+board[i][j+1]+board[i][j+2]
        if i<N-1:
            for k in range(3):
                if temp<board[i+1][j+k]:
                    temp=board[i+1][j+k]
        if i>0:
            for k in range(3):
                if temp<board[i-1][j+k]:
                    temp=board[i-1][j+k]
        if max<sum+temp:
            max=sum+temp

for i in range(N-1):
    for j in range(1,M-1):
        sum=board[i][j]+board[i+1][j]
        if board[i][j-1]+board[i+1][j+1]<board[i][j+1]+board[i+1][j-1]:
            sum+=board[i][j+1]+board[i+1][j-1]
        else:
            sum+=board[i][j-1]+board[i+1][j+1]
        if max<sum:
            max=sum

for i in range(1,N-1):
    for j in range(M-1):
        sum=board[i][j]+board[i][j+1]
        if board[i-1][j]+board[i+1][j+1]<board[i+1][j]+board[i-1][j+1]:
            sum+=board[i+1][j]+board[i-1][j+1]
        else:
            sum+=board[i-1][j]+board[i+1][j+1]
        if max<sum:
            max=sum

print(max)
            
