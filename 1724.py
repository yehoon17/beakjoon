#https://www.acmicpc.net/problem/1724
def continuous(x1,y1,lines,x2,y2):
    for line in lines:
        if x1 == x2:
            x = x1
            y = max(y1,y2)
            if line[1] == y and line[3] == y:
                if min(line[0],line[2])<=x and max(line[0],line[2])>=x+1:
                    return False                
        else:
            x = max(x1,x2)
            y = y1
            if line[0] == x and line[2] == x:
                if min(line[1],line[3])<=y and max(line[1],line[3])>=y+1:
                    return False
    return True

def new_color(i,j,N,M,lines,colored,groups):
    colored[i][j] = True
    groups[(i,j)] ={(i,j)}
    if i > 0:
        if not colored[i-1][j]:
            if continuous(i,j,lines,i-1,j):
                colored[i-1][j] = True
                groups[(i,j)].add((i-1,j))
    if i < N-1:
        if not colored[i+1][j]:
            if continuous(i,j,lines,i+1,j):
                colored[i+1][j] = True
                groups[(i,j)].add((i+1,j))
    if j > 0:
        if not colored[i][j-1]:
            if continuous(i,j,lines,i,j-1):
                colored[i][j-1] = True
                groups[(i,j)].add((i,j-1))
    if j < M-1:
        if not colored[i][j+1]:
            if continuous(i,j,lines,i,j+1):
                colored[i][j+1] = True
                groups[(i,j)].add((i,j+1))
  
def merge_color(key,x,y,groups):
    for k, v in groups.items():
        if (x,y) in v:
            key2 = k
            break
    groups[key]=groups[key].union(groups.pop(key2))
    
def add_color(i,j,N,M,lines,colored,groups):
    for k, v in groups.items():
        if (i,j) in v:
            key = k
            break
    
    if i > 0:
        if continuous(i,j,lines,i-1,j):
            if not colored[i-1][j]:
                colored[i-1][j] = True
                groups[key].add((i-1,j))
            else:
                merge_color(key,i-1,j,groups)
    if i < N-1:
        if continuous(i,j,lines,i+1,j):
            if not colored[i+1][j]:
                colored[i+1][j] = True
                groups[key].add((i+1,j))
            else:
                merge_color(key,i+1,j,groups)
    if j > 0:
        if continuous(i,j,lines,i,j-1):
            if not colored[i][j-1]:
                colored[i][j-1] = True
                groups[key].add((i,j-1))
            else:
                merge_color(key,i,j-1,groups)
    if j < M-1:
        if continuous(i,j,lines,i,j+1):
            if not colored[i][j+1]:
                colored[i][j+1] = True
                groups[key].add((i,j+1))
            else:
                merge_color(key,i,j+1,groups)
                
N, M = map(int,input().split())
T = int(input())
lines = [list(map(int, input().split())) for _ in range(T)]

colored = [[False]*M for _ in range(N)]
groups = dict()

for i in range(N):
    for j in range(M):
        if not colored[i][j]:
            new_color(i,j,N,M,lines,colored,groups)
        else:
            add_color(i,j,N,M,lines,colored,groups)

max_area = -1
min_area = -1
for group in groups.values():
    area = len(group)
    max_area = max(max_area,area)
    if min_area<0:
        min_area = area
    else:
        min_area = min(min_area,area)
        
print(max_area) 
print(min_area)
