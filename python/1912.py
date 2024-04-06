#https://www.acmicpc.net/problem/1912

N=int(input())
arr=list(map(int,input().split()))

l=[arr[0]]
answer=arr[0]
for i in range(1,N):
    max=l[i-1]+arr[i]
    if max<arr[i]:
        max=arr[i]
    l.append(max)
    if answer<max:
        answer=max
print(answer)
    
