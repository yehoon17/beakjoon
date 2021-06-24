#https://www.acmicpc.net/problem/10250

T=int(input())
for _ in range(T):
    H,W,N = map(int,input().split())
    if N%H==0:
        floor=H
        temp=0
    else:
        floor=N%H
        temp=1
    YY=str(floor)
    if N//H<10-temp:
        XX='0'+str(N//H+temp)
    else:
        XX=str(N//H+temp)
    print(YY+XX)
