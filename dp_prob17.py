import sys

N=int(sys.stdin.readline())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp=[[0]*N for _ in range(N)]
dp[0][0]=1
for i in range(N):
    for j in range(N):
        for k in range(i):
            if k+board[k][j]==i:
                dp[i][j]+=dp[k][j]
        for k in range(j):
            if k+board[i][k]==j:
                dp[i][j]+=dp[i][k]
print(dp[-1][-1])
