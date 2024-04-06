#https://www.acmicpc.net/problem/2562

max=0
line=0
for i in range(9):
    x=int(input())
    if x>max:
        max=x
        line=i
print(max)
print(line+1)
        
