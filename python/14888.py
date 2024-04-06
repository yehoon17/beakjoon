#https://www.acmicpc.net/problem/14888

import sys

def cal(numbers,plus,minus,mult,div,max,min):     

    if plus>0:
        n=numbers[1:].copy()
        n[0]=numbers[0]+n[0]
##        print(n)
        max,min=cal(n,plus-1,minus,mult,div,max,min)
    if minus>0:
        n=numbers[1:].copy()
        n[0]=numbers[0]-n[0]
##        print(n)
        max,min=cal(n,plus,minus-1,mult,div,max,min)
    if mult>0:
        n=numbers[1:].copy()
        n[0]=numbers[0]*n[0]
##        print(n)
        max,min=cal(n,plus,minus,mult-1,div,max,min)
    if div>0:
        n=numbers[1:].copy()
        flag=False
        if numbers[0]<0:
            flag=True
            numbers[0]*=-1
        n[0]=numbers[0]//n[0]
        if flag:
            n[0]*=-1
##        print(n)
        max,min=cal(n,plus,minus,mult,div-1,max,min)
    if plus==0 and minus==0 and mult==0 and div==0:
        if max<numbers[0]:
            max=numbers[0]
        if min>numbers[0]:
            min=numbers[0]
    return max,min

        
N=int(sys.stdin.readline().strip())

line=sys.stdin.readline().strip().split()
numbers=[]
for i in range(N):
    numbers.append(int(line[i]))

line=sys.stdin.readline().strip().split()
plus=int(line[0])
minus=int(line[1])
mult=int(line[2])
div=int(line[3])

max=-100000000001
min=100000000001

max,min=cal(numbers,plus,minus,mult,div,max,min)

print(max)
print(min)
