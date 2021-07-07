#https://www.acmicpc.net/problem/14890

import sys

def passable(N,L,road):
    count=1
    need_slope=False
    for i in range(1,N):
        if road[i]==road[i-1]:
            count+=1
            if need_slope and count==L:
                count=0
                need_slope=False
        elif road[i]==road[i-1]+1:
            if count>=L and not need_slope:
                count=1
            else:
                return False
        elif road[i]==road[i-1]-1:
            if need_slope:
                return False
            elif L==1:
                count=0
            else:
                count=1
                need_slope=True
        else:
            return False
    if need_slope:
        return False
    return True

N,L=map(int,sys.stdin.readline().split())
board=[]
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

count=0
for i in range(N):
    if passable(N,L,board[i]):
        count+=1
##        print('passable')
##    else:
##        print('---')
    road=[]
    for j in range(N):
        road.append(board[j][i])
    if passable(N,L,road):
        count+=1
##        print('passable')
##    else:
##        print('---')

print(count)
