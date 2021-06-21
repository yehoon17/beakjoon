#https://www.acmicpc.net/problem/7562

def knight_move(positions, end, moved, board_size, visited):
    for p in positions:
        if p[0] == end[0] and p[1] == end[1]:
            return moved

    moves = [(x,y) for x in (-1,1) for y in (2,-2)] \
            + [(x,y) for y in (-1,1) for x in (2,-2)]

    next_positions = []

    for p in positions:
        for move in moves:
            x = p[0] + move[0]
            y = p[1] + move[1]

            if 0 <= x and x <board_size and\
               0 <= y and y <board_size:
                if not visited[x][y]:
                    next_positions.append([x,y])
                    visited[x][y] = True

    return knight_move(next_positions, end, moved+1, board_size, visited)


#main
task_cases = int(input())

for i in range(task_cases):
    board_size = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    visited = [[False] * board_size for _ in range(board_size)]
    visited[start[0]][start[1]] = True

    print(knight_move([start], end, 0, board_size, visited))
