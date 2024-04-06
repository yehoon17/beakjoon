#https://www.acmicpc.net/problem/1002

T=int(input())
for i in range(T):
    line=input().split()
    x1=int(line[0])
    y1=int(line[1])
    r1=int(line[2])
    x2=int(line[3])
    y2=int(line[4])
    r2=int(line[5])
    d=((x1-x2)**2+(y1-y2)**2)**0.5
    if r1>r2:
        max=r1
        min=r2
    else:
        max=r2
        min=r1
    if d==0:
        if r1==r2:
            print(-1)
        else:
            print(0)
    else:
        if d==r1+r2 or d+min==max:
            print(1)
        elif d>r1+r2:
            print(0)
        elif d+min<max:
            print(0)
        else:
            print(2)
