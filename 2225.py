#https://www.acmicpc.net/problem/2225

N,K=map(int,input().split())
dp=[1 for _ in range(N+1)]
for _ in range(K-1):
    for i in range(1,N+1):
        dp[i]+=dp[i-1]
print(dp[-1]%1000_000_000)
