#https://www.acmicpc.net/problem/1920

N=int(input())
arr=list(map(int,input().split()))
arr.sort()
M=int(input())
find=list(map(int,input().split()))
for i in range(M):
    start=0
    size=len(arr)
    while(size>1):
        if find[i]<arr[start+size//2]:
            size=size//2
        else:
            start=start+size//2
            size=(size+1)//2
    if find[i]==arr[start]:
        print(1)
    else:
        print(0)
            
