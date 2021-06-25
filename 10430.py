#https://www.acmicpc.net/problem/10430

L=input().split()
A=int(L[0])
B=int(L[1])
C=int(L[2])
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
