#https://www.acmicpc.net/problem/2156

import sys

def add(dp,x):
    temp=[0]*6
    temp[0]=dp[4]
    temp[1]=dp[0]
    
    if dp[0]>dp[3]:
        temp[2]=dp[0]+x
    else:
        temp[2]=dp[3]+x
    
    if dp[5]>dp[2]:
        temp[3]=dp[5]
    else:
        temp[3]=dp[2]
        
    if dp[2]>dp[5]:
        temp[4]=dp[2]+x
    else:
        temp[4]=dp[5]+x

    temp[5]=dp[1]+x

    return temp
    


N=int(sys.stdin.readline().strip())
dp=[0,0,0,0,0,0]
for i in range(N):
    x=int(sys.stdin.readline().strip())
    dp=add(dp,x)
    
max=0
for i in range(6):
    if max<dp[i]:
        max=dp[i]
print(max)
