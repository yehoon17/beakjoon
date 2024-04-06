#https://www.acmicpc.net/problem/1309

N=int(input())
dp=[1,1]
for _ in range(N-1):
    temp=dp[0]
    dp[0]+=dp[1]*2
    dp[1]+=temp
print((sum(dp)+dp[1])%9901)
