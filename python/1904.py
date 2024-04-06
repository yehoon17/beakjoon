#https://www.acmicpc.net/problem/1904

import sys

N=int(sys.stdin.readline().strip())
a=1
b=2
if N==1:
    print(a)
elif N==2:
    print(b)
else:
    for i in range(N-2):
        b=(a+b)%15746
        a=b-a
    print(b)
