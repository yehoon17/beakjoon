#https://www.acmicpc.net/problem/1037

N=int(input())
line=input().split()
min=1000000
max=1
for x in line:
    a=int(x)
    if a<min:
        min=a
    if a>max:
        max=a
print(min*max)
