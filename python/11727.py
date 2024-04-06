# https://www.acmicpc.net/problem/11727

n=int(input())
dp=[1,3]

for i in range(n-2):
    dp[i%2]=dp[i%2]*2+dp[i%2-1]
print(dp[n%2-1]%10007)
