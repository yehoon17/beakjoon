#https://www.acmicpc.net/problem/11048

import sys

N,M=map(int,sys.stdin.readline().split())
maze=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        max=maze[i][j]
        if i>0:
            temp=maze[i][j]+maze[i-1][j]
            if max<temp:
                max=temp
        if j>0:
            temp=maze[i][j]+maze[i][j-1]
            if max<temp:
                max=temp
        if i>0 and j>0:
            temp=maze[i][j]+maze[i-1][j-1]
            if max<temp:
                max=temp
        maze[i][j]=max

print(maze[-1][-1])
