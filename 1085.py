#https://www.acmicpc.net/problem/1085

line=input().split()
x=int(line[0])
y=int(line[1])
w=int(line[2])
h=int(line[3])
min=1001
d=[x,y,w-x,h-y]
for i in d:
    if min>i:
        min=i
print(min)
