#https://www.acmicpc.net/problem/1978

N=int(input())
count=0
line=input().split()
for i in range(N):
    x=int(line[i])
    if x==1:
        continue
    for d in range(1,int(x**0.5)):
        if x==d+1:
            continue
        if x%(d+1)==0:
            break
    else:
        count+=1
print(count)
