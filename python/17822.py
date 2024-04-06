#https://www.acmicpc.net/problem/17822

from collections import deque

N, M, T = map(int, input().split())
disks = [deque(map(int, input().split())) for _ in range(N)]
spins = [list(map(int, input().split())) for _ in range(T)]

for spin in spins:
    x, d, k = spin
    for i in range(N):
        if (i+1)%x == 0:
            for _ in range(k):
                if d == 0:
                    #clockwise
                    disks[i].appendleft(disks[i].pop())
                else:
                    #anti-clockwise
                    disks[i].append(disks[i].popleft())
    # step 2
    hasdup = False
    isdup = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if disks[i][j]>0:
                if disks[i][j] == disks[i][j-1]:
                    hasdup = True
                    isdup[i][j] = True
                    isdup[i][j-1] = True
    for i in range(N-1):
        for j in range(M):
            if disks[i][j]>0:
                if disks[i][j] == disks[i+1][j]:
                    hasdup = True
                    isdup[i][j] = True
                    isdup[i+1][j] = True
    if hasdup:
        for i in range(N):
            for j in range(M):
                if isdup[i][j]:
                    disks[i][j] = 0
    else:
        sum = 0
        count = 0
        for i in range(N):
            for j in range(M):
                if disks[i][j] > 0:
                    sum+=disks[i][j]
                    count+=1
        if count != 0:
            avg = sum/count
            for i in range(N):
                for j in range(M):
                    if disks[i][j] > 0:
                        if disks[i][j] > avg:
                            disks[i][j]-=1
                        elif disks[i][j] < avg:
                            disks[i][j]+=1
answer = 0
for i in range(N):
    for j in range(M):
        answer+=disks[i][j]
print(answer)
                
        
                
