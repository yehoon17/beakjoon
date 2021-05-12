#https://www.acmicpc.net/problem/10773

import sys

N = int(sys.stdin.readline().strip())

l = []

for i in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        l.pop()
    else:
        l.append(x)

sum = 0
for i in range(len(l)):
    sum += l[i]

print(sum)
