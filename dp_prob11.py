N=int(input())
seq=list(map(int,input().split()))

dp=[seq[0]]

for i in range(1,N):
    temp=seq[i]
    for j in range(i):
        if seq[j]>=seq[i]:
            continue
        else:
            temp=max(temp,seq[i]+dp[j])
    dp.append(temp)
print(max(dp))
