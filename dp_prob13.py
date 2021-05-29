N=int(input())
seq=list(map(int,input().split()))

dp=[1]
for i in range(1,N):
    temp=1
    for j in range(i):
        if seq[i]<seq[j]:
            temp=max(temp,dp[j]+1)
    dp.append(temp)
print(max(dp))
