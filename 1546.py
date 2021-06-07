#https://www.acmicpc.net/problem/1546

n=int(input())
L=input().split()
sum=0
max=0
for i in range(n):
    sum+=int(L[i])
    if int(L[i])>max:
        max=int(L[i])
print(sum/n/max*100)
