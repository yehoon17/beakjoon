#https://www.acmicpc.net/problem/20125

import sys

N=int(sys.stdin.readline())
head=False
is_body=True
body=0
left_leg=right_leg=1
for i in range(N):
    line=sys.stdin.readline().strip()
    if not head:
        for j in range(N):
            if line[j]=='*':
                heart=[i+2,j+1]
                head=True
                break
        else:
            continue
    else:        
        if heart[0]-1==i:
            left=0
            right=0
            for j in range(N):
                if line[j]=='*':
                    if heart[1]-1>j:
                        left+=1
                    if heart[1]-1<j:
                        right+=1
        elif is_body:
            if line[heart[1]-1]=='*':
                body+=1
            else:
                is_body=False
        else:
            if line[heart[1]-2]=='*':
                left_leg+=1
            if line[heart[1]]=='*':
                right_leg+=1
print(*heart)
print(left,right,body,left_leg,right_leg)
