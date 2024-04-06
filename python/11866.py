#https://www.acmicpc.net/problem/11866

from collections import deque

N,K=map(int,input().split())
que=deque(range(1,1+N))
answer=[]
for i in range(N):
    for j in range(K-1):
        que.append(que.popleft())
    answer.append(que.popleft())
print('<'+str(answer)[1:-1]+'>')
