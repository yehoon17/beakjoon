class Pool:
    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.grid = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        self.shark_at = {}
        
    def add(self, i, j, shark):
        if self.grid[i][j] < shark.size:
            self.grid[i][j] = shark.size
            self.shark_at[(i, j)] = shark
        
    def catch(self, j):
        for i in range(self.n_rows):
            if self.grid[i][j] > 0:
                caught_size = self.grid[i][j]
                self.grid[i][j] = 0
                self.shark_at.pop((i, j))
                return caught_size
        return 0
    
    def move_sharks(self):
        self.grid = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        shark_at_ = self.shark_at
        self.shark_at = {}
        for (i, j), shark in shark_at_.items():
            # print(f'shark: {shark}')
            # print(f"from: {i}, {j}")
            x, y = shark.move(i, j, self.n_rows, self.n_cols)
            # print(f'to: {x}, {y}')
            self.add(x, y, shark)
            

class Shark:
    def __init__(self, speed, direction, size):
        self.speed = speed
        self.direction = direction
        self.size = size

    def move(self, i, j, n_rows, n_cols):
        #1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽
        if self.direction < 3:
            dx = self.speed*(-1)**self.direction
            x = i + dx
            if -1 < x < n_rows:
                return x, j

            n = n_rows * 2 - 2
            x %= n
            # print(f'{-1 + self.direction} <= {x} < {n_rows - 2 + self.direction}')
            if not (-1 + self.direction <= x < n_rows - 2 + self.direction):
                self.direction = 3 - self.direction
                
            x = min(x, n-x)
            return x, j
            
        else:
            dy = self.speed*(-1)**(self.direction+1)
            y = j + dy
            if -1 < y < n_cols:
                return i, y

            n = n_cols * 2 - 2
            y %= n
            
            if not (4 - self.direction <= y < n_cols + 3 - self.direction):
                self.direction = 7 - self.direction
                
            y = min(y, n-y)
            return i, y
    
    def __str__(self):
        return f'speed: {self.speed}, d: {arrows[self.direction]}, size: {self.size}'
        
n_rows, n_cols, n_sharks = map(int, input().split())
pool = Pool(n_rows, n_cols)
for _ in range(n_sharks):
    i, j, speed, direction, size = map(int, input().split())
    shark = Shark(speed, direction, size)
    pool.add(i-1, j-1, shark)
    
total_size = 0
for j in range(n_cols):
    total_size += pool.catch(j)
    pool.move_sharks()

print(total_size)
    
        
