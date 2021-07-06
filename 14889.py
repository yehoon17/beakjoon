#https://www.acmicpc.net/problem/14889

import sys

def select(n,m):
    l=[]
    if n==m:
        return [list(range(1,n+1))]
    elif m==1:
        return list(map(lambda x:[x],range(1,n+1)))
    else:
        for i in range(1,n-m+2):
            temp=select(n-i,m-1)
            for j in range(len(temp)):
                for k in range(len(temp[j])):
                    temp[j][k]+=i
                temp[j]+=[i]
            l+=temp
        return l

def permutate(n):
    l=[]
    for i in range(n):
        for j in range(n):
            if i!=j:
                l.append([i,j])
    return l

def power(team_start,table,size):
    index=permutate(size)
    team_start+=[0]
    team_link=[]
    for i in range(size*2):
        if i not in team_start:
            team_link.append(i)
    power_start=0
    power_link=0
    for x in index:
        i=team_start[x[0]]
        j=team_start[x[1]]
        power_start+=table[i][j]
        i=team_link[x[0]]
        j=team_link[x[1]]
        power_link+=table[i][j]
    diff=power_start-power_link
    if diff<0:
        diff*=-1
    return diff
   
    
N=int(sys.stdin.readline().strip())
table=[]
for i in range(N):
    line=list(map(int,sys.stdin.readline().strip().split()))
    table.append(line)

team0=select(N-1,int(N/2)-1)    

min=10000

for x in team0:
    temp=power(x,table,int(N/2))
    if min>temp:
        min=temp

print(min)
