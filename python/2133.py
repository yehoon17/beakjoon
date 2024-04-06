#https://www.acmicpc.net/problem/2133

N=int(input())
dp=[3,11]
if N%2==0:
    for i in range(2,N//2):
        temp=2+dp[-1]*3+sum(dp[:-1])*2
        dp.append(temp)
    print(dp[N//2-1])
else:
    print(0)
