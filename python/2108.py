#https://www.acmicpc.net/problem/2108

import sys

N=int(sys.stdin.readline().strip())

l=[0]*8001
sum=0
for i in range(N):
    x=int(sys.stdin.readline().strip())
    index=x+4000
    l[index]+=1
    sum+=x

max_mode=0
flag=True
mid_flag=True
is_left=True
is_min=True
is_max=True
count=0
for i in range(8001):
    if l[i]>max_mode:
        max_mode=l[i]
        mode=i-4000
        flag=True
    elif l[i]==max_mode:
        if flag:
            flag=False
            mode=i-4000
            
    count+=l[i]
    if N%2==0:
        if mid_flag:
            if count>=N/2 and is_left:
                left=i-4000
                is_left=False
            if count>N/2:
                right=i-4000
                mid=(left+right)/2
                mid_flag=False
    else:
        if count>=(N+1)/2 and mid_flag:
            mid=i-4000
            mid_flag=False
    if is_min and count>0:
        min=i-4000
        is_min=False
    if is_max and count==N:
        max=i-4000
        is_max=False
if sum<0:
    step=-0.5
else:
    step=0.5

print(int(step+sum/N))
print(mid)
print(mode)
print(max-min)
