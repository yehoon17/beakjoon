#https://www.acmicpc.net/problem/2293

import sys

n,k=map(int,sys.stdin.readline().split())
dp=[1]+[0]*k
for _ in range(n):
    coin=int(sys.stdin.readline())
    temp=dp.copy()
    for i in range(1,1+k):
        if i-coin>=0:    
            dp[i]=temp[i]+dp[i-coin]
print(dp[-1])
    
