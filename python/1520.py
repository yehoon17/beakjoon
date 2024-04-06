#https://www.acmicpc.net/problem/1520
import sys

def f(i,j,data,dp,N,M):
    dp[i][j]=0
    if i>0:
        if data[i-1][j]>data[i][j]:
            if dp[i-1][j]<0:
                f(i-1,j,data,dp,N,M)
            dp[i][j]+=dp[i-1][j]
    if j>0:
        if data[i][j-1]>data[i][j]:
            if dp[i][j-1]<0:
                f(i,j-1,data,dp,N,M)
            dp[i][j]+=dp[i][j-1]
    if i<N-1:
        if data[i+1][j]>data[i][j]:
            if dp[i+1][j]<0:
                f(i+1,j,data,dp,N,M)
            dp[i][j]+=dp[i+1][j]
    if j<M-1:
        if data[i][j+1]>data[i][j]:
            if dp[i][j+1]<0:
                f(i,j+1,data,dp,N,M)
            dp[i][j]+=dp[i][j+1]

    
    
N,M=map(int,sys.stdin.readline().split())
data=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp=[[-1]*M for _ in range(N)]
dp[0][0]=1

for i in range(N):
    for j in range(M):
        if dp[i][j]<0:
            f(i,j,data,dp,N,M)

print(dp[-1][-1])
