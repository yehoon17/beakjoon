#https://www.acmicpc.net/problem/6588

import sys

prime=[True]*500000
for i in range(3,1000000,2):
    if prime[i//2-1]:
        for j in range(i*3,1000000,i*2):
            prime[j//2-1]=False
            
while True:
    x=int(sys.stdin.readline())
    if x==0:
        break
    found=False
    for i in range(len(prime)):
        if prime[i]:
            a=i*2+3
            b=x-a
            if prime[b//2-1]:
                found=True
                break
        if i*2+3>x//2:
            break
        
    if found:
        print(f"{x} = {a} + {b}")
    else:
        print("Goldbach's conjecture is wrong.")
