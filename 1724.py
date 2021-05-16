#https://www.acmicpc.net/problem/1724

def color(i,j,N,M,lines,colored):
    pass

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
