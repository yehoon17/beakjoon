CLOCKWISE = [[0, 1], [1, 0], [0, -1], [-1, 0]]
ANTI_CLOCKWISE = [[0, 1], [-1, 0], [0, -1], [1, 0]]


class Room:
    def __init__(self, grid, r, c):
        self.n_rows = r
        self.n_cols = c
        self.air_cleaner = [(i, 0) for i in range(r) if grid[i][0] == -1]
        for i, j in self.air_cleaner:
            grid[i][j] = 0
        self.dust = grid
        
    def is_inside(self, x, y):
        return -1 < x < self.n_rows and -1 < y < self.n_cols
    
    def diffuse(self):
        new_dust = [[0 for _ in range(self.n_cols)] for _ in range(self.n_rows)]
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                if (dust := self.dust[i][j]) > 0:
                    dust_diffused = dust // 5
                    for dx, dy in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                        x = i + dx
                        y = j + dy
                        if self.is_inside(x, y) and (x, y) not in self.air_cleaner:
                            new_dust[x][y] += dust_diffused
                            dust -= dust_diffused
                    new_dust[i][j] += dust
        self.dust = new_dust
        
    def clean(self):
        for start, orientations in zip(self.air_cleaner, [ANTI_CLOCKWISE, CLOCKWISE]):
            i, j = start
            orientation_idx = 0
            dx, dy = orientations[orientation_idx]
            carry_dust = 0
            while True:
                if not self.is_inside(i + dx, j + dy):
                    orientation_idx += 1
                    dx, dy = orientations[orientation_idx]
                x = i + dx
                y = j + dy
                
                if (x, y) == start:
                    break
                    
                new_carry_dust = self.dust[x][y]
                self.dust[x][y] = carry_dust
                carry_dust = new_carry_dust
                
                i = x
                j = y
                
    def count_dust(self):
        total = 0
        
        for line in self.dust:
            total += sum(line)
            
        return total
    

r, c, t = map(int, input().split())
grid = []
for _ in range(r):
    grid.append(list(map(int, input().split())))
    
room = Room(grid, r, c)

for _ in range(t):
    room.diffuse()
    room.clean()
    
print(room.count_dust())
