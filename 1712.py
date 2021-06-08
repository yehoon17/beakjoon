#https://www.acmicpc.net/problem/1712

line=input().split()
A=int(line[0])
B=int(line[1])
C=int(line[2])
if C-B>0:   
    print(int(A/(C-B))+1)
else:
    print(-1)
