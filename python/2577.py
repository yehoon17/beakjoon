#https://www.acmicpc.net/problem/2577

x=int(input())*int(input())*int(input())
L=[0]*10
while True:
    n=x%10
    x=int(x/10)
    L[n]+=1
    if x==0:
        break
for i in range(10):
    print(L[i])
