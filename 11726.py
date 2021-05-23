# https://www.acmicpc.net/problem/11726

n=int(input())

dp=[1,2]
for i in range(n-2):
    dp[i%2]+=dp[i%2-1]
print(dp[n%2-1]%10007)
