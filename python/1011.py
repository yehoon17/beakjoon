#https://www.acmicpc.net/problem/1011

import math
T=int(input())
for i in range(T):
    line=input().split()
    x=int(line[0])
    y=int(line[1])
    distance=y-x
    cap=math.ceil(distance**0.5)
    if cap*(cap-1)<distance:
        print(2*cap-1)
    else:
        print(2*cap-2)
