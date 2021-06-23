#https://www.acmicpc.net/problem/9461

import sys

T=int(sys.stdin.readline().strip())
for i in range(T):
    N=int(sys.stdin.readline().strip())
    l=[1,1,1,2,2]
    for i in range(N-5):
        l[i%5]+=l[i%5-1]
    print(l[N%5-1])
