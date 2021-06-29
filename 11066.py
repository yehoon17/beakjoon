#https://www.acmicpc.net/problem/11066

import sys

def cost(K,f):
    dp=[f]
    dp.append([f[i]+f[i+1] for i in range(K-1)])
    for i in range(2,K):
        temp=[]
        for j in range(K-i):
            x=min(dp[i-1][j],dp[i-1][j+1])
            for k in range(1,i-1):
                x=min(x,dp[k][j]+dp[i-k-1][j+k+1])
            temp.append(x+sum(f[j:j+1+i]))
        dp.append(temp)
    return dp[-1][0]
    

T=int(sys.stdin.readline())
for _ in range(T):
    K=int(sys.stdin.readline())
    files=list(map(int,sys.stdin.readline().split()))
    print(cost(K,files))
    


