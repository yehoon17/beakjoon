#https://www.acmicpc.net/problem/11720

N=int(input())
s=input()
sum=0
for i in range(N):
    sum+=int(s[i])
    
print(sum)
