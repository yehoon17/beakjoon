#https://www.acmicpc.net/problem/1018

line=input().split()
N=int(line[0])
M=int(line[1])
board=[]
for i in range(N):
    board.append(input())
min=64
for i in range(N-7):
    for j in range(M-7):
        for corner in ('B','W'):
            count=0
            for x in range(8):
                for y in range(8):
                    if (x+y)%2==0 and board[i+x][j+y]==corner:
                        count+=1
                    if (x+y)%2==1 and board[i+x][j+y]!=corner:
                        count+=1
            if min>count:
                min=count
print(min)
