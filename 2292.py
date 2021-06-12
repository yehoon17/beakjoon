#https://www.acmicpc.net/problem/2292

import math
N=int(input())
answer=math.ceil((-3+(12*N-3)**0.5)/6)+1
print(answer)

