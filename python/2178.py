#https://www.acmicpc.net/problem/2178

import sys
from collections import deque

def search(N,M,maze,visited,que):
    if not que:
        return
    i,j=que.popleft()
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for t in range(4):
        x=i+dx[t]
        y=j+dy[t]
        if 0<=x<N and 0<=y<M:
            if maze[x][y]=='1' and visited[x][y]<0:
                que.append([x,y])
                visited[x][y]=visited[i][j]+1
                if x==N-1 and y==M-1:
                    return
    search(N,M,maze,visited,que)

sys.setrecursionlimit(10000)                    
N,M=map(int,sys.stdin.readline().split())
maze=[sys.stdin.readline().strip() for _ in range(N)]
visited=[[-1]*M for _ in range(N)]
que=deque([[0,0]])
visited[0][0]=1
search(N,M,maze,visited,que)
print(visited[-1][-1])
