#https://www.acmicpc.net/problem/2884

L=input().split()
H=int(L[0])
M=int(L[1])
if M<45:
    print((H-1)%24,(M-45)%60)
else:
    print(H,M-45)
