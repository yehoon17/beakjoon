#https://www.acmicpc.net/problem/4673

def d(n):
    temp=n
    while True:
        n+=temp%10
        temp=int(temp/10)
        if temp==0:
            break
    return n

#main
for n in range(10000):
    N=n+1
    for i in range(N):
        if i==100:
            print(N)
            break
        if d(N-i-1)==N:
            break
    else:
        print(N)

