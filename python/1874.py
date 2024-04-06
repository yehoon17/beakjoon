#https://www.acmicpc.net/problem/1874

import sys

n=int(sys.stdin.readline())
li=[i for i in range(n,0,-1)]
stack=[]
answer=[]
for _ in range(n):
    flag=False
    x=int(sys.stdin.readline())
    if li:
        while li[-1]<x:
            stack.append(li.pop())
            answer.append('+')
        if li[-1]==x:
            li.pop()
            answer.append('+')
            answer.append('-')
            flag=True
    if not flag:
        if stack[-1]==x:
            stack.pop()
            answer.append('-')
        else:
            answer=['NO']
            break
##    print(flag)
##    print(answer)
##    print(li)
##    print(stack)


for x in answer:
    print(x)
