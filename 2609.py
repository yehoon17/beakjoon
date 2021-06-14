#https://www.acmicpc.net/problem/2609

def gcd(a,b):
    if a>b:
        max=a
        min=b
    else:
        max=b
        min=a
    if max%min==0:
        return min
    return gcd(min,max-min)


line=input().split()
a=int(line[0])
b=int(line[1])
d=gcd(a,b)
print(d)
print(int(a*b/d))
