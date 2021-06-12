#https://www.acmicpc.net/problem/2231

N=int(input())
for i in range(1,N):
    sum=i
    temp=i
    while(i>0):
        sum+=i%10
        i=i//10
    if sum==N:
        print(temp)
        break
else:
    print(0)

    
