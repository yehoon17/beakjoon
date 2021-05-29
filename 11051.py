#https://www.acmicpc.net/problem/11051

N,K=map(int,input().split())
dp=1
for i in range(1,K+1):
    dp=(dp*(N+1-i)//i)
print(dp%10007)
