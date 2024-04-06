#https://www.acmicpc.net/problem/11057

N=int(input())
dp=[1 for i in range(10)]
for _ in range(N-1):
    for i in range(0,10):
        dp[i]+=sum(dp[i+1:])
print(sum(dp)%10007)
