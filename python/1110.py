#https://www.acmicpc.net/problem/1110

n=int(input())
temp=n
count=0
while True:
    a=int(temp/10)
    b=temp%10
    c=(a+b)%10
    temp=b*10+c
    count+=1
    if n==temp:
        break
print(count)
