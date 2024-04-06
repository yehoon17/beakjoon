#https://www.acmicpc.net/problem/12100

import sys

def move(board,i,N):
    moved=[]
    if i==0:
        for i in range(N):
            line=[0]*N
            x=0
            merged=True
            for j in range(N):
                if board[i][j]>0:
                    if merged:
                        line[x]=board[i][j]
                        x+=1
                        merged=False
                    else:
                        if line[x-1]==board[i][j]:
                            line[x-1]*=2
                            merged=True
                        else:
                            line[x]=board[i][j]
                            x+=1
            moved.append(line)
    elif i==1:
        for i in range(N):
            line=[0]*N
            x=N-1
            merged=True
            for j in range(N-1,-1,-1):
                if board[i][j]>0:
                    if merged:
                        line[x]=board[i][j]
                        x-=1
                        merged=False
                    else:
                        if line[x+1]==board[i][j]:
                            line[x+1]*=2
                            merged=True
                        else:
                            line[x]=board[i][j]
                            x-=1
            moved.append(line)
    elif i==2:
        merged=[True]*N
        x=[0]*N
        moved=[[0]*N for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j]>0:
                    if merged[j]:
                        moved[x[j]][j]=board[i][j]
                        x[j]+=1
                        merged[j]=False
                    else:
                        if moved[x[j]-1][j]==board[i][j]:
                            moved[x[j]-1][j]*=2
                            merged[j]=True
                        else:
                            moved[x[j]][j]=board[i][j]
                            x[j]+=1
    elif i==3:
        merged=[True]*N
        x=[N-1]*N
        moved=[[0]*N for i in range(N)]
        for i in range(N-1,-1,-1):
            for j in range(N):
                if board[i][j]>0:
                    if merged[j]:
                        moved[x[j]][j]=board[i][j]
                        x[j]-=1
                        merged[j]=False
                    else:
                        if moved[x[j]+1][j]==board[i][j]:
                            moved[x[j]+1][j]*=2
                            merged[j]=True
                        else:
                            moved[x[j]][j]=board[i][j]
                            x[j]-=1
    return moved
        

def get_max(board,N):
    max=0
    for i in range(N):
        for j in range(N):
            if max<board[i][j]:
                max=board[i][j]

    return max

def play(board,count,N):
    if count==5:
        return get_max(board,N)
        
    l=[]
    for i in range(4):
        l.append(play(move(board,i,N),count+1,N))

    max=0
    for i in range(4):
        if max<l[i]:
            max=l[i]
    return max


N=int(sys.stdin.readline())
board=[]
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().strip().split())))

print(play(board,0,N))
