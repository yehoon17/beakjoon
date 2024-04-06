#https://www.acmicpc.net/problem/11399

n=int(input())
li=list(map(int,input().split()))
li.sort()
sum=0
for i,x in enumerate(li):
    sum+=x*(len(li)-i)
print(sum)
