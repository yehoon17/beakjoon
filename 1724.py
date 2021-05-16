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

def group_color(color1,color2,groups):
    for i, group in enumerate(groups):
        if color1 in group:
            g1 = groups.pop(i)
            break
    for i, group in enumerate(groups):
        if color2 in group:
            g2 = groups.pop(i)
            break
    try:
        groups.append(g1.union(g2))
    except UnboundLocalError as e:
        groups.append(g1)

    
def color_neighbors(i,j,N,M,lines,colors,canvas,color,count):
    if i > 0:
        if continuous(i,j,lines,i-1,j):
            if canvas[i-1][j] < 0:
                canvas[i-1][j] = color
                count[color]+=1
            else:
                group_color(color,canvas[i-1][j],groups)
    if i < N-1:
        if continuous(i,j,lines,i+1,j):
            if canvas[i+1][j] < 0:
                canvas[i+1][j] = color
                count[color]+=1
            else:
                group_color(color,canvas[i+1][j],groups)
    if j > 0:
        if continuous(i,j,lines,i,j-1):
            if canvas[i][j-1] < 0:
                canvas[i][j-1] = color
                count[color]+=1
            else:
                group_color(color,canvas[i][j-1],groups)
    if j < M-1:
        if continuous(i,j,lines,i,j+1):
            if canvas[i][j+1] < 0:
                canvas[i][j+1] = color
                count[color]+=1
            else:
                group_color(color,canvas[i][j+1],groups)


N, M = map(int,input().split())
T = int(input())
lines = [list(map(int, input().split())) for _ in range(T)]

canvas = [[-1]*M for _ in range(N)]
next_color = 0
groups = []
count = []

for i in range(N):
    for j in range(M):
        if canvas[i][j] < 0:
            canvas[i][j] = next_color
            groups.append({canvas[i][j]})
            count.append(1)
            next_color += 1
        color = canvas[i][j]
        color_neighbors(i,j,N,M,lines,groups,canvas,color,count)
        
max_area = -1
min_area = -1

for group in groups:
    area = 0
    for i in group:
        area+=count[i]
    max_area = max(max_area,area)
    if min_area<0:
        min_area = area
    else:
        min_area = min(min_area,area)
    
print(max_area) 
print(min_area)
