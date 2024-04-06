#https://www.acmicpc.net/problem/1181

import sys

N=int(sys.stdin.readline().strip())

s=set()
for i in range(N):
    word=sys.stdin.readline().strip()
    s.add(word)

l=list(s)
l.sort()
l.sort(key=len)

for i in range(len(l)):
        print(l[i])
