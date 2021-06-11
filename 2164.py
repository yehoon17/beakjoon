#https://www.acmicpc.net/problem/2164

from collections import deque

N=int(input())
card=deque(range(1,1+N))
for _ in range(N-1):
    card.popleft()
    card.append(card.popleft())
print(card[0])
