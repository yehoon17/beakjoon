#https://www.acmicpc.net/problem/18258

from collections import deque
from sys import stdin
que=deque()
N=int(stdin.readline())
for _ in range(N):
    line=stdin.readline().strip().split()
    if line[0]=='push':
        que.append(line[1])

    if line[0]=='pop':
        if que:
            print(que.popleft())
        else:
            print(-1)

    if line[0]=='size':
        print(len(que))

    if line[0]=='empty':
        if que:
            print(0)
        else:
            print(1)

    if line[0]=='front':
        if que:
            print(que[0])
        else:
            print(-1)

    if line[0]=='back':
        if que:
            print(que[-1])
        else:
            print(-1)
