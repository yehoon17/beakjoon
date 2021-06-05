#https://www.acmicpc.net/problem/1193

import math

def get_order(X,group):
    max_order=(group*(group+1))/2
    return group+X-max_order

X=int(input())
sol=(-1+(1+8*X)**0.5)/2
group=math.ceil(sol)
order=get_order(X,group)
if group%2==0:
    print('%d/%d'%(order,group+1-order))
else:
    print('%d/%d'%(group+1-order,order))
    
