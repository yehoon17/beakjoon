#https://www.acmicpc.net/problem/15552

import sys
n=int(sys.stdin.readline().rstrip())
for i in range(n):
    L=sys.stdin.readline().rstrip().split()
    a=int(L[0])
    b=int(L[1])
    print(a+b)
