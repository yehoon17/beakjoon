#https://www.acmicpc.net/problem/11054

import sys

N=int(sys.stdin.readline().strip())
arr=list(map(int,sys.stdin.readline().strip().split()))

length=[1]
mark=0
for i in range(1,N):
    if arr[i]>arr[i-1]:
        max=length[i-1]
        for j in range(mark-1,-1,-1):
            if arr[i]>arr[j]:
                if max<length[j]:
                    max=length[j]
        length.append(max+1)
    else:
        mark=i
        max=0
        for j in range(i-1,-1,-1):
            if arr[i]>arr[j]:
                if max<length[j]:
                    max=length[j]
        length.append(max+1)
        
arr=arr[::-1]
length2=[1]
mark=0
for i in range(1,N):
    if arr[i]>arr[i-1]:
        max=length2[i-1]
        for j in range(mark-1,-1,-1):
            if arr[i]>arr[j]:
                if max<length2[j]:
                    max=length2[j]
        length2.append(max+1)
    else:
        mark=i
        max=0
        for j in range(i-1,-1,-1):
            if arr[i]>arr[j]:
                if max<length2[j]:
                    max=length2[j]
        length2.append(max+1)
max=0
for i in range(N):
    if max<length[i]+length2[N-1-i]:
        max=length[i]+length2[N-1-i]
print(max-1)
