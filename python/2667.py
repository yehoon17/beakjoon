def bfs(i, j, visited, grid):
    if visited[i][j]:
        return 0
    
    if grid[i][j] == '0':
        return 0
    
    visited[i][j] = True
    total = 1
    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        x = i + dx
        y = j + dy
        if -1 < x < n and -1 < y < n:
            total += bfs(x, y, visited, grid)
    
    return total
    

n = int(input())
grid = [input() for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

houses = []
for i in range(n):
    for j in range(n):
        x = bfs(i, j, visited, grid)
        if x > 0:
            houses.append(x)


houses.sort()
print(len(houses))
for house in houses:
    print(house)
