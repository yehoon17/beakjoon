import sys

n,m=map(int,sys.stdin.readline().split())
dp=[list(map(int,list(sys.stdin.readline().strip()))) for _ in range(n)]

for i in range(1,n):
    for j in range(1,m):
        if dp[i-1][j-1]>0 and dp[i][j]>0 and dp[i-1][j]>0 and dp[i][j-1]>0:
            dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
temp=0
for i in range(n):
    temp=max(temp,max(dp[i]))
print(temp**2)
