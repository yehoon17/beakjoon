#https://www.acmicpc.net/problem/1330

L=input().split()
a=int(L[0])
b=int(L[1])
if a<b:
    print('<')
elif a>b:
    print('>')
else:
    print('==')
