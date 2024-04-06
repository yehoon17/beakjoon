#https://www.acmicpc.net/problem/2751

import sys

def merge(l,start,end):
    mid=(start+end)//2

    if start+1<end:
        merge(l,start,mid)
        merge(l,mid,end)

        l1=l[start:mid]
        l2=l[mid:end]
        i,j=0,0
        for k in range(start,end):
            if i==mid-start:
                l[k]=l2[j]
                j+=1
            elif j==end-mid:
                l[k]=l1[i]
                i+=1
            else:               
                if l1[i]<l2[j]:
                    l[k]=l1[i]
                    i+=1
                else:
                    l[k]=l2[j]
                    j+=1
    


N=int(sys.stdin.readline())
l=[]
for i in range(N):
    l.append(int(sys.stdin.readline()))

merge(l,0,N)
for i in range(N):
    print(l[i])
