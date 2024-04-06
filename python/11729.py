#https://www.acmicpc.net/problem/11729

def hanoi(N,start,target):
    if N==1:
        print(start,target)
        return
    temp=3-(start+target)%3
    hanoi(N-1,start,temp)
    print(start,target)
    hanoi(N-1,temp,target)

N=int(input())
print(2**N-1)
hanoi(N,1,3)
