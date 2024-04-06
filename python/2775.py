#https://www.acmicpc.net/problem/2775

def F(k,n):
    series=[]
    for i in range(n):
        series.append(i+1)
    for j in range(k):
        for i in range(1,n):
            series[i]+=series[i-1]
    return series[n-1]


T=int(input())
for i in range(T):
    k=int(input())
    n=int(input())
    print(F(k,n))
