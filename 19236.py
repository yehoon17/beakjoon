N = 4
DIRECTIONS = {
    1: (-1, 0),
    2: (-1, -1),
    3: (0, -1),
    4: (1, -1),
    5: (1, 0),
    6: (1, 1),
    7: (0, 1),
    8: (-1, 1)
}


def rotate(i, j, x, y, fish_dir):
    while True:
        dx, dy = DIRECTIONS[fish_dir]
        x_ = x + dx
        y_ = y + dy
        if -1 < x_ < N and -1 < y_ < N:
            if i != x_ or j != y_:
                break
        
        fish_dir += 1
        if fish_dir > 8:
            fish_dir -= 8
                
    return fish_dir
        

def move(grid, x, y, fish_dir, fish):
    dx, dy = DIRECTIONS[fish_dir]
    x_ = x + dx
    y_ = y + dy
    fish_no = grid[x][y]
    fish_no_ = grid[x_][y_]
    grid[x][y], grid[x_][y_] = grid[x_][y_], grid[x][y]
    fish[fish_no] = [x_, y_, fish_dir]
    if fish_no_ > 0:
        fish[fish_no_] = [x, y, fish[fish_no_][2]]
    

def shark_destinations(i, j, shark_dir, new_grid):
    dx, dy = DIRECTIONS[shark_dir]
    l = []
    while True:
        i += dx
        j += dy
        if -1 < i < N and -1 < j < N:
            if new_grid[i][j] > 0:
                l.append((i, j))
        else:
            break
            
    return l
    

def dfs(i, j, fish, grid):
    fish_no = grid[i][j]
    total = fish_no
    shark_dir = fish[fish_no][2]
    fish.pop(fish_no)
    grid[i][j] = 0
    
    new_grid = [[a for a in line] for line in grid]
    new_fish = {k: v for k, v in fish.items()}
    for fish_no in sorted(new_fish.keys()):
        x, y, fish_dir = new_fish[fish_no]
        # print(fish_dir, DIRECTIONS[fish_dir])
        new_fish_dir = rotate(i, j, x, y, fish_dir)
        # print(new_fish_dir, DIRECTIONS[new_fish_dir])
        move(new_grid, x, y, new_fish_dir, new_fish)

    
    l = [0]
    for i_, j_ in shark_destinations(i, j, shark_dir, new_grid):
        new_grid_ = [[a for a in line] for line in new_grid]
        new_fish_ = {k: v for k, v in new_fish.items()}
        l.append(dfs(i_, j_, new_fish_, new_grid_))
    
    return total + max(l)
    

fish = {}
grid = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        j0 = j*2
        j1 = j0 + 1
        fish_no = line[j0]
        fish_dir = line[j1]
        grid[i][j] = fish_no
        fish[fish_no] = [i, j, fish_dir]
        
print(dfs(0, 0, fish, grid))
