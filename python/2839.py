#https://www.acmicpc.net/problem/2839

N=int(input())
for i in range(5):
    X=N-3*i
    if X%5==0 and X>=0:
        print(int(i+X/5))
        break
else:
    print(-1)
