#https://www.acmicpc.net/problem/4344

n=int(input())
for line in range(n):
    L=input().split()
    total=int(L.pop(0))
    sum=0
    for i in range(total):
        sum+=int(L[i])
    avg=sum/total
    count=0
    for i in range(total):
        if int(L[i])>avg:
            count+=1
    print('%.3f%%'%(count/total*100))
    
