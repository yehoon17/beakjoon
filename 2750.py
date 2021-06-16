#https://www.acmicpc.net/problem/2750

N=int(input())
l=[]
for i in range(N):
    l.append(int(input()))
for i in range(N-1):
    for j in range(N-i-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
for i in range(N):
    print(l[i])
