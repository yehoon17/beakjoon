#https://www.acmicpc.net/problem/1005

import sys

def dfs(N,K,time,order,W,dp):
    dp[W-1]=time[W-1]
    for x in order:
        if x[1]==W:
            if dp[x[0]-1]<0:
                dfs(N,K,time,order,x[0],dp)
            dp[W-1]=max(dp[W-1],dp[x[0]-1]+time[W-1])        

def solve(N,K,time,order,W):
    dp=[-1]*N
    dfs(N,K,time,order,W,dp)
    return dp[W-1]   

T=int(sys.stdin.readline())
for _ in range(T):
    N,K=map(int,sys.stdin.readline().split())
    time=list(map(int,sys.stdin.readline().split()))
    order=[list(map(int,sys.stdin.readline().split())) for _ in range(K)]
    W=int(sys.stdin.readline())
    print(solve(N,K,time,order,W))
