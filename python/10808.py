#https://www.acmicpc.net/problem/10808

s=input()
t=[0]*26
for c in s:t[ord(c)-97]+=1
print(*t)
