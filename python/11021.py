#https://www.acmicpc.net/problem/11021

n=int(input())
for i in range(n):
    L=input().split()
    a=int(L[0])
    b=int(L[1])
    print('Case #%d: %d'%(i+1,a+b))
