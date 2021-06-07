#https://www.acmicpc.net/problem/1463

N=int(input())

l=[0]

for i in range(2,N+1):
    min=i
    if i%3==0:
        temp=i//3-1
        if min>l[temp]:
            min=l[temp]
    if i%2==0:
        temp=i//2-1
        if min>l[temp]:
            min=l[temp]
    if min>l[i-2]:
        min=l[i-2]
    l.append(min+1)

print(l[-1])
