#https://www.acmicpc.net/problem/14925

M, N = map(int,input().split())

land = [list(map(int,input().split())) for _ in range(M)]

dp = [[0]*N for _ in range(M)]

answer = 0
for i in range(M):
    for j in range(N):
        if land[i][j] == 0:
            dp[i][j]=1
            if i>0 and j>0:
                if (land[i-1][j-1] == 0 and 
                    land[i-1][j] == 0 and 
                    land[i][j-1] == 0):
                    dp[i][j]=min(dp[i-1][j-1],
                                 dp[i-1][j],
                                 dp[i][j-1])+1                
            answer = max(answer, dp[i][j])    
print(answer)
