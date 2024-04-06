#https://www.acmicpc.net/problem/1629

def f(a,b,c):
    if b==1:
        return a%c
    return f((a**2)%c,b//2,c)*a**(b%2)

A,B,C=map(int,input().split())
print(f(A,B,C)%C)
