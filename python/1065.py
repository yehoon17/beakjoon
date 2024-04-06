#https://www.acmicpc.net/problem/1065

def check(n):
    L=[]
    while n!=0:
        L.append(n%10)
        n=int(n/10)
    diff=[]
    for i in range(len(L)-1):
        diff.append(L[i]-L[i+1])
    if diff==diff[0:1]*len(diff):
        return True
    else:
        return False
    
#main
n=int(input())
count=0
for i in range(n):
    if check(n-i):
        count+=1
print(count)
