#https://www.acmicpc.net/problem/1931

import sys

def f0(x):
    return x[0]

def f1(x):
    return x[1]

N=int(sys.stdin.readline().strip())
L=[]
for i in range(N):
    temp=sys.stdin.readline().strip().split()
    for index in range(2):
        temp[index]=int(temp[index])
    L.append(temp)
    
start=0
count=0
last=0
for i in range(N):
    if last<L[i][0]:
        last=L[i][0]

L.sort(key=f0)
L.sort(key=f1) 

for x in L:
    if x[0]>=start:
        start=x[1]
        count+=1
        
        
print(count)
