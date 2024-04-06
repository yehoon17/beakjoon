class Ocean:
    def __init__(self, n):
        self.size = n
        
    def input(self):
        self.grid = []
        for _ in range(n):
            self.grid.append(list(map(int, input().split())))

        
class BabyShark:
    def __init__(self, ocean):
        self.size = 2
        self.eat_count = 0
        self.location = self.locate(ocean)
        
    def locate(self, ocean):
        for i in range(ocean.size):
            for j in range(ocean.size):
                if ocean.grid[i][j] == 9:
                    ocean.grid[i][j] = 0
                    return (i, j)
                
    def eatable(self, x, y, ocean):
        if 0 < ocean.grid[x][y] < self.size:
            return True
        else:
            return False
        
    def eat(self, x, y):
        self.eat_count += 1
        self.location = (x, y)
        if self.eat_count == self.size:
            self.eat_count = 0
            self.size += 1
        

def movable(x, y, size, ocean, visited):
    movable_locations = set()
    for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
        x_ = x + dx
        y_ = y + dy
        if -1 < x_ < ocean.size and -1 < y_ < ocean.size:
            if not visited[x_][y_] and ocean.grid[x_][y_] <= size:
                movable_locations.add((x_, y_))
        
    return movable_locations
    
def bfs(baby_shark, ocean):
    visited = [[False for _ in range(ocean.size)] for _ in range(ocean.size)]
    travel_time = 1
    queue = [baby_shark.location]
    while queue:
        new_queue = set()
        for x, y in queue:
            visited[x][y] = True
            new_queue |= movable(x, y, baby_shark.size, ocean, visited)
        
        queue = sorted(new_queue)
        for x, y in queue:
            if baby_shark.eatable(x, y, ocean):
                baby_shark.eat(x, y)
                ocean.grid[x][y] = 0
                return travel_time
            
        travel_time += 1
        
    return -1           
        
        
n = int(input())

ocean = Ocean(n)
ocean.input()

baby_shark = BabyShark(ocean)

total_time = 0
while True:
    travel_time = bfs(baby_shark, ocean)
    if travel_time > 0:
        total_time += travel_time
    else:
        break
    
print(total_time)
