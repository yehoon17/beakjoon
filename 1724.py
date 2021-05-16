#https://www.acmicpc.net/problem/1724
def continuous(x1,y1,lines,x2,y2):
    for line in lines:
        

def color(i,j,N,M,lines,colored):
    colored[i][j] = True
    group =[[i,j]]
    if i > 0:
        if not colored[i-1][j]:
            if continuous(i,j,line,i-1,j):
                group += color(i-1,j,N,M,lines,colored)
    if i < N-1:
        if not colored[i+1][j]:
            if continuous(i,j,line,i+1,j):
                group += color(i+1,j,N,M,lines,colored)
    if j > 0:
        if not colored[i][j-1]:
            if continuous(i,j,line,i,j-1):
                group += color(i,j-1,N,M,lines,colored)
    if j < M-1:
        if not colored[i][j+1]:
            if continuous(i,j,line,i,j+1):
                group += color(i,j+1,N,M,lines,colored)
    return group
                
    
N, M = map(int,input().split())
T = int(input())
lines = [list(map(int, input().split())) for _ in range(T)]

colored = [[False]*M for _ in range(N)]

max_area = -1
min_area = -1

for i in range(N):
    for j in range(M):
        if not colored[i][j]:
            area = len(color(i,j,N,M,lines,colored))
            max_area = max(area,max_area)
            if min_area < 0:
                min_area = area
            else:
                min_area = min(area,min_area)
                
print(max_area) 
print(min_area)
