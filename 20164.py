#https://www.acmicpc.net/problem/20164

def f(N):
    sum=0
    if N<10:
        min=max=N%2
    elif N<100:
        a=N//10
        b=N%10
        if a+b<10:
            min=max=a%2+b%2+(a+b)%2
        else:
            min=max=a%2+b%2+2
    else:
        digit=len(str(N))
        temp=N
        for i in range(digit):
            sum+=(temp%10)%2
            temp//=10
        max=0
        min=10000000
        for i in range(1,digit):
            for j in range(1,digit-i):
                a=N%(10**i)
                b=(N//(10**i))%(10**j)
                c=N//(10**(i+j))
                temp1,temp2=f(a+b+c)
                if min>temp1:
                    min=temp1
                if max<temp2:
                    max=temp2
    return min+sum,max+sum


N=int(input())
min,max=f(N)
print(min,max)
