#https://www.acmicpc.net/problem/1260

import sys
from collections import deque

def dfs(V,graph,visited,answer):
    if visited[V-1]:
        return
    answer.append(V)
    visited[V-1]=True
    temp=[]
    for x in graph:
        for i in range(2):
            if x[i]==V and not visited[x[i-1]-1]:
                temp.append(x[i-1])
    temp.sort()
    for x in temp:
        dfs(x,graph,visited,answer)
            
def bfs(graph,visited,answer,que):
    if len(que)==0:
        return
    parent=que.popleft()
    answer.append(parent)
    temp=[]
    for x in graph:
        for i in range(2):
            if x[i]==parent and not visited[x[i-1]-1]:
                temp.append(x[i-1])
                visited[x[i-1]-1]=True
    temp.sort()
    for x in temp:
        que.append(x)
    bfs(graph,visited,answer,que)
    
    
sys.setrecursionlimit(10000)
N,M,V=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split())) for _ in range(M)]

visited=[False for _ in range(N)]
answer=[]
dfs(V,graph,visited,answer)
print(*answer)

visited=[False for _ in range(N)]
que=deque([V])
answer=[]
visited[V-1]=True
bfs(graph,visited,answer,que)
print(*answer)
