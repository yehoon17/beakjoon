#https://www.acmicpc.net/problem/20165

import sys

def play(board,donimos,N,M,attack,defend):
    score=0
    #attack
    x,y,d=attack
    i=j=0
    if d=='N':
        i=-1
    elif d=='S':
        i=1
    elif d=='E':
        j=1
    else:
        j=-1
    height=1
    while (-1<x and x<N and -1<y and y<M):
        if height==0:
            break
        if board[x][y]!='F':
            board[x][y]='F'
            score+=1
            if height<dominos[x][y]:
                height=dominos[x][y]
        height-=1
        x+=i
        y+=j
        


    #defend
    x,y=defend
    board[x-1][y-1]=dominos[x-1][y-1]

    return score     
                

N,M,R=map(int,sys.stdin.readline().split())
dominos=[]
board=[]
for i in range(N):
    line=list(map(int,sys.stdin.readline().split()))
    dominos.append(line)
    board.append(line.copy())

score=0
for i in range(R):
    attack=sys.stdin.readline().split()
    for j in range(2):
        attack[j]=int(attack[j])-1
    defend=list(map(int,sys.stdin.readline().split()))
    score+=play(board,dominos,N,M,attack,defend)
    


print(score)
for i in range(N):
    line=board[i]
    for j in range(M):
        if line[j]!='F':
            line[j]='S'
    print(*line)
