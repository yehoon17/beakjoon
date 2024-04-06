#https://www.acmicpc.net/problem/11653

N=int(input())
if N>1:
    for i in range(2,int(1+N**0.5)):
        while N%i==0:
            N=N/i
            print(int(i))
        if N==1:
            break
    else:
        print(int(N))

