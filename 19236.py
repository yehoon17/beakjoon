import copy
from abc import ABC, abstractmethod

DEBUG = False
SEA_SIZE = 4

def log(x, indent=0):
    if DEBUG:
        lines = x.__str__().split('\n')
        for line in lines:
            print('  '*indent, line, sep='')
            

class MarineLife(ABC):
    def __init__(self, number=0):
        self.number = number
    
    def move(self, new_location):
        self.location = new_location

    @property
    def destination(self):
        i, j = self.location
        dx, dy = self.direction.vector
        return (i + dx, j + dy)

class Shark(MarineLife):
    def eat(self, fish):
        self.move(fish.location)
        self.number += fish.number
        self.direction = fish.direction    
        
    def __str__(self):
        return f'number: {self.number}, location: {self.location}, direction: {self.direction}'

class Fish(MarineLife):
    def __init__(self, i, j, number, direction):
        super().__init__(number)
        self.location = (i, j)
        self.direction = direction

    def rotate(self):
        self.direction_id = self.direction.rotate()

    def __str__(self):
        return f'number: {self.number}, location: {self.location}, direction: {self.direction}'
    

class Sea:
    def __init__(self, size, shark):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.fish_dict = {}
        self.shark = shark

    def add(self, fish):
        i, j = fish.location
        self.grid[i][j] = fish.number
        self.fish_dict[fish.number] = fish

    def is_destination_valid(self, marin_life):
        i, j = marin_life.destination
        return -1 < i < self.size and -1 < j < self.size

    def is_shark(self, fish):
        return self.shark.location == fish.destination
        
    @property
    def fish_list(self):
        return sorted(self.fish_dict.keys())

    def shark_eat(self, location):
        i, j = location
        eaten_fish_number = self.grid[i][j]
        eaten_fish = self.fish_dict[eaten_fish_number]
        self.shark.eat(eaten_fish)
        self.fish_dict.pop(eaten_fish_number)
        self.grid[i][j] = 0

    def rotate_fish(self, fish_number):
        # log(f'rotating {fish_number} fish', 2)
        while True:
            fish = self.fish_dict[fish_number]
            # log(f'direction: {fish.direction}', 3)
            if self.is_destination_valid(fish):
                if not self.is_shark(fish):
                    break

            fish.rotate()
        # log(self, 2)

    def swap(self, location1, location2):
        i1, j1 = location1
        i2, j2 = location2
        self.grid[i1][j1], self.grid[i2][j2] = self.grid[i2][j2], self.grid[i1][j1]

    def fish_at(self, location):
        i, j = location
        return self.grid[i][j]
        
    def move_fish(self, fish_number):
        fish = self.fish_dict[fish_number]
        destination_fish_number = self.fish_at(fish.destination)
        
        self.swap(fish.location, fish.destination)

        location = fish.location
        fish.move(fish.destination)
        if destination_fish_number > 0:
            self.fish_dict[destination_fish_number].move(location)

    def is_fish(self, location):
        i, j = location 
        return self.grid[i][j] > 0
    
    def shark_destinations(self):
        destinations = []
        while self.is_destination_valid(self.shark):
            self.shark.move(self.shark.destination)
            if self.is_fish(self.shark.location):
                destinations.append(self.shark.location)
        return destinations
    
    def get_shark_number(self):
        return self.shark.number

    def __str__(self):
        grid_ = []
        for line in self.grid:
            line_ = []
            for fish_number in line:
                if fish_number > 0:
                    s = f'{fish_number:>2}, {self.fish_dict[fish_number].direction}'
                else:
                    s = f'{fish_number:>2}    '
                line_.append(s)
            grid_.append(line_)

        grid_.append('')
        return '\n'.join([str(line) for line in grid_])
    
class Direction:
    vectors = {
        1: (-1, 0),
        2: (-1, -1),
        3: (0, -1),
        4: (1, -1),
        5: (1, 0),
        6: (1, 1),
        7: (0, 1),
        8: (-1, 1)
    }
    arrows = {
        1: " ↑",
        2: "↖",
        3: " ←",
        4: "↙",
        5: " ↓",
        6: "↘",
        7: " →",
        8: "↗",
    }

    
    def __init__(self, direction_id):
        self.direction_id = direction_id

    @property
    def vector(self):
        return self.vectors[self.direction_id]
        
    @property
    def arrow(self):
        return self.arrows[self.direction_id]

    def rotate(self):
        self.direction_id += 1
        if self.direction_id > 8:
            self.direction_id = 1

        return self.direction_id

    def __str__(self):
        return self.arrow
    
def dfs(location, sea):
    log('dfs start ------------------------------')
    log(f'location: {location}')
    # log(sea)

    sea.shark_eat(location)
    log(f'shark ate: {sea.shark}')
    log(sea)

    log('rotate and move fish')
    for fish_number in sea.fish_list:
        # log('rotate', 1)
        sea.rotate_fish(fish_number)
        # log(sea, 1)

        # log('move', 1)
        sea.move_fish(fish_number)
        # log(sea, 1)
    log(sea)

    sea_list = [sea]
    shark_destinations = sea.shark_destinations()
    log(f'shark_destinations: {shark_destinations}')
    for shark_destination in shark_destinations:
        new_sea = copy.deepcopy(sea)
        sea_list.append(dfs(shark_destination, new_sea))

    log(f'sharks: {[s.shark.number for s in sea_list]}')
    max_shark_number_sea = max(sea_list, key=lambda x: x.shark.number)
    log('dfs end ================================')
    return max_shark_number_sea
    

shark = Shark()
sea = Sea(SEA_SIZE, shark)
for i in range(SEA_SIZE):
    line = list(map(int, input().split()))
    for j in range(SEA_SIZE):
        j0 = j*2
        j1 = j0 + 1
        number = line[j0]
        direction = Direction(line[j1])
        fish = Fish(i, j, number, direction)
        sea.add(fish)

location = (0, 0)
sea = dfs(location, sea)
log('#'*30)
print(sea.get_shark_number())
