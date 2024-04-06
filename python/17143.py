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
            n = n_rows * 2 - 2
            dx = self.speed % n
            if self.direction == 1:
                # print(i, dx, n)
                x = i - dx
                if x < 0:
                    x = -x
                    self.direction = 2
                    if x > n_rows - 1:
                        x = n + 1 - x
                        self.direction = 1
            else:
                x = i + dx
                if x > n_rows - 1:
                    x = n - x
                    self.direction = 1
                    if x < 0:
                        x = -x
                        self.direction = 2                        
            return x, j
        else:
            n = n_cols * 2 - 2
            dy = self.speed % n
            if self.direction == 4:
                y = j - dy
                if y < 0:
                    y = -y
                    self.direction = 3
                    if y > n_cols - 1:
                        y = n + 1 - y
                        self.direction = 4
            else:
                y = j + dy
                if y > n_cols - 1:
                    y = n - y
                    self.direction = 4
                    if y < 0:
                        y = -y
                        self.direction = 3   
            return i, y
    
    def __str__(self):
        return f'speed: {self.speed}, d: {self.direction}, size: {self.size}'
        
        
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
    
