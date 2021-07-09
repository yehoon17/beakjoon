#https://www.acmicpc.net/problem/15649

import sys

def per(n,m,chosen):
    l=[]
    if m==1:
        for i in range(1,n+1):
            if i not in chosen:
                l.append([i])
        return l    
    else:
        for i in range(1,n+1):
            if i not in chosen:
                temp=per(n,m-1,chosen+[i])
                for j in range(len(temp)):
                    temp[j]=[i]+temp[j]
                l+=temp
        return l
            
        

#main
line=sys.stdin.readline().strip().split()
l=per(int(line[0]),int(line[1]),[])
for p in l:
    print(*p)
