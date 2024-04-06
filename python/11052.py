# https://www.acmicpc.net/problem/11052

N=int(input())
cards=list(map(int,input().split()))
dp=[0]+cards
for i in range(1,N+1):
    for j in range(i//2+1):
        if dp[j]+dp[i-j]>dp[i]:
            dp[i]=dp[j]+dp[i-j]
        
print(dp[-1])
