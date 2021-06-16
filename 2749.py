#https://www.acmicpc.net/problem/2749

def power(X,size,n):
    if n==1:
        for i in range(size):
            for j in range(size):
                X[i][j]%=1000000
        return X
    elif n%2==0:
        temp=[]
        for i in range(size):
            temp.append([])
            for j in range(size):
                sum=0
                for k in range(size):
                    sum+=X[i][k]*X[k][j]
                temp[i].append(sum%1000000)
        return power(temp,size,n//2)
    else:
        temp=[]
        Y=power(power(X,size,2),size,n//2)
        for i in range(size):
            temp.append([])
            for j in range(size):
                sum=0
                for k in range(size):
                    sum+=X[i][k]*Y[k][j]
                temp[i].append(sum%1000000)
        return temp

N=int(input())

if N==0:
    print(0)
elif N==1:
    print(1)
else:
    X=[[0,1],[1,1]]
    Y=power(X,2,N-1)
    print(Y[1][1])
