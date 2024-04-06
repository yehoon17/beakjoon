#https://www.acmicpc.net/problem/1780

import sys

def cut(l):
    size=len(l)//3
    count=[0,0,0]
    if size==0:
        count[l[0][0]]+=1
    elif size==1:
        for i in range(3):
            for j in range(3):
                count[l[i][j]]+=1
    else:
        for i in range(3):
            for j in range(3):
                temp=[]
                for k in range(size):
                    temp.append(l[i*size+k][j*size:j*size+size])
                x=cut(temp)
                for k in range(3):
                    count[k]+=x[k]
    for i in range(3):
        if count[i]==9 and count[i-1]==0 and count[i-2]==0:
            count[i]=1
            break
    return count


N=int(sys.stdin.readline().strip())

l=[]
for i in range(N):
    line=list(map(int,sys.stdin.readline().strip().split()))
    l.append(line)

count=cut(l)

for i in range(-1,2):
    print(count[i])
