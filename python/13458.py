#https://www.acmicpc.net/problem/13458

N=int(input())
A=list(map(int,input().split()))
B,C=map(int,input().split())

count=0
for i in range(N):
    count+=1
    if A[i]<B:
        continue
    else:
        x=A[i]-B
        count+=(x+(-x)%C)//C

print(count)
