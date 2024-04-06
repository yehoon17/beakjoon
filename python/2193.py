# https://www.acmicpc.net/problem/2193

N=int(input())
dp=[1,0]
if N>1:
    for i in range(N-2):
        temp=dp[0]
        dp[0]+=dp[1]
        dp[1]=temp
print(sum(dp))
