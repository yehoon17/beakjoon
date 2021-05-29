import sys

def f(i,j,altitude,dp,visited,N,M):
    sum=0
    visited[i][j]=True
    if i>0:
        if altitude[i-1][j]>altitude[i][j]:
            if not visited[i-1][j]:
                f(i-1,j,altitude,dp,visited,N,M)
            sum+=dp[i-1][j]
    if j>0:
        if altitude[i][j-1]>altitude[i][j]:
            if not visited[i][j-1]:
                f(i,j-1,altitude,dp,visited,N,M)
            sum+=dp[i][j-1]
    if i<N-1:
        if altitude[i+1][j]>altitude[i][j]:
            if not visited[i+1][j]:
                f(i+1,j,altitude,dp,visited,N,M)
            sum+=dp[i+1][j]
    if j<M-1:
        if altitude[i][j+1]>altitude[i][j]:
            if not visited[i][j+1]:
                f(i,j+1,altitude,dp,visited,N,M)
            sum+=dp[i][j+1]
    dp[i][j]=sum

    
    
N,M=map(int,sys.stdin.readline().split())
altitude=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp=[[0]*M for _ in range(N)]
visited=[[False]*M for _ in range(N)]
dp[0][0]=1
visited[0][0]=True

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            f(i,j,altitude,dp,visited,N,M)

print(dp[-1][-1])
