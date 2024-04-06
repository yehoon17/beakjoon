#https://www.acmicpc.net/problem/1436

def isEvil(n):
    count=0
    while(n>0):
        if n%10==6:
            count+=1
        else:
            count=0
        if count==3:
            return True
        n=n//10
    else:
        return False


N=int(input())
count=0
n=665
while(count<N):
    n+=1
    if isEvil(n):
        count+=1
print(n)
