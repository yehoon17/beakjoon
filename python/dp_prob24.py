import sys

def f(m,c,dp):
    temp=[]
    i=0
    for start,end,cost in dp:
        if m>end:
            pass
        else:
            
        
N,M=map(int,sys.stdin.readline().split())
memory=list(map(int,sys.stdin.readline().split()))
cost=list(map(int,sys.stdin.readline().split()))
dp=[[0,M,-1]]
for m,c in zip(memory,cost):
    f(m,c,dp)
    








'''
dp=[-1]*M
for m,c in zip(memory,cost):
    temp=dp.copy()
    for i in range(m):
        if dp[i]<0:
            dp[i]=c
        else:
            dp[i]=min(dp[i],c)
    for i in range(m,M):
        if temp[i-m]>=0:
            if dp[i]<0:
                dp[i]=temp[i-m]+c
            else:
                dp[i]=min(dp[i],temp[i-m]+c)
        else:
            break
print(dp[-1])
'''
