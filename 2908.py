#https://www.acmicpc.net/problem/2908

S=input().split()
a=int(S[0][::-1])
b=int(S[1][::-1])
if a>b:
    print(a)
else:
    print(b)
