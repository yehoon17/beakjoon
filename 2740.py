#https://www.acmicpc.net/problem/2740

import sys

line=sys.stdin.readline().strip().split()
size_A=list(map(int,line))
A=[]
for i in range(size_A[0]):
    A.append(list(map(int,sys.stdin.readline().strip().split())))
        
line=sys.stdin.readline().strip().split()
size_B=list(map(int,line))
B=[]
for i in range(size_B[0]):
    B.append(list(map(int,sys.stdin.readline().strip().split())))

C=[]
for i in range(size_A[0]):
    C.append([])
    for j in range(size_B[1]):
        sum=0
        for k in range(size_A[1]):
            sum+=A[i][k]*B[k][j]
        C[i].append(sum)
        
for i in range(len(C)):
    print(*C[i])
