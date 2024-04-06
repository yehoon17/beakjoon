#https://www.acmicpc.net/problem/11047

N,K=map(int,input().split())
a=[int(input()) for _ in range(N)]

count=0
for x in a[::-1]:
    count+=K//x
    K=K%x
     
print(count)
