#https://www.acmicpc.net/problem/2869

import math
line=input().split()
A=int(line[0])
B=int(line[1])
V=int(line[2])
x=math.ceil((V-A)/(A-B))
print(x+1)
