#https://www.acmicpc.net/problem/1724
def continuous(x1,y1,line,x2,y2):
    pass

def color(i,j,N,M,lines,colored):
    area = 1
    colored[i][j] = True
    if i > 0:
        if not colored[i-1][j]:
            if continuous(i,j,line,i-1,j):
                area += color(i-1,j,N,M,lines,colored)
    if i < N-1:
        if not colored[i+1][j]:
            if continuous(i,j,line,i+1,j):
                area += color(i+1,j,N,M,lines,colored)
    if j > 0:
        if not colored[i][j-1]:
            if continuous(i,j,line,i,j-1):
                area += color(i,j-1,N,M,lines,colored)
    if j < M-1:
        if not colored[i][j+1]:
            if continuous(i,j,line,i,j+1):
                area += color(i,j+1,N,M,lines,colored)
    return area
                
    
N, M = map(int,input().split())
T = int(input())
lines = [list(map(int, input().split())) for _ in range(T)]

colored = [[False]*M for _ in range(N)]

max_area = -1
min_area = -1

for i in range(N):
    for j in range(M):
        if not colored[i][j]:
            area = color(i,j,N,M,lines,colored)
            max_area = max(area,max_area)
            if min_area < 0:
                min_area = area
            else:
                min_area = min(area,min_area)
                
print(max_area) 
print(min_area)
