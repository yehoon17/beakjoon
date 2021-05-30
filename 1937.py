#https://www.acmicpc.net/problem/1937

import sys

def dfs(i,j,forest,dp,n):
    dp[i][j]=1
    if i>0:
        if forest[i][j]>forest[i-1][j]:
            if dp[i-1][j]<0:
                dfs(i-1,j,forest,dp,n)
            dp[i][j]=max(dp[i][j],dp[i-1][j]+1)
    if j>0:
        if forest[i][j]>forest[i][j-1]:
            if dp[i][j-1]<0:
                dfs(i,j-1,forest,dp,n)
            dp[i][j]=max(dp[i][j],dp[i][j-1]+1)
    if i<n-1:
        if forest[i][j]>forest[i+1][j]:
            if dp[i+1][j]<0:
                dfs(i+1,j,forest,dp,n)
            dp[i][j]=max(dp[i][j],dp[i+1][j]+1)
    if j<n-1:
        if forest[i][j]>forest[i][j+1]:
            if dp[i][j+1]<0:
                dfs(i,j+1,forest,dp,n)
            dp[i][j]=max(dp[i][j],dp[i][j+1]+1)

sys.setrecursionlimit(250000)
n=int(sys.stdin.readline())
forest=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp=[[-1]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if dp[i][j]<0:
            dfs(i,j,forest,dp,n)
temp=0
for i in range(n):
    temp=max(temp,max(dp[i]))
print(temp)
