#https://www.acmicpc.net/problem/1699

N=int(input())
squares=[i**2 for i in range(1,318)]
dp=[i for i in range(1+N)]
for i in range(1,N+1):
    j=1
    while i+1>squares[j]:
        if dp[i]>dp[i-squares[j]]+1:
            dp[i]=dp[i-squares[j]]+1
        j+=1
print(dp[-1])
