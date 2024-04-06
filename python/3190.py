#https://www.acmicpc.net/problem/3190

import sys

def eat_apple(head,apple):
    for i in range(len(apple)):
        if head==apple[i]:
            apple[i],apple[-1]=apple[-1],apple[i]
            apple.pop()
            return True
    return False

def game_over(snake,face,N,t_face,t_speed):
    head=snake[0]
    body=snake[1]
    tail=snake[2]
    if head[face]==0 or head[face]==N+1:
##        print('==wall==')
        return True
    if len(body)>2:
        for i in range(1,len(body)-2):
            face=body[i-1][1]
            speed=body[i-1][2]
            x=-1*((speed+1)//2)
            y=(speed-1)//2
            if head[face-1]==body[i][0][face-1]:
                if body[i+x][0][face]<=head[face] and head[face]<=body[i+y][0][face]:
##                    print('==body==')
                    return True
                
        if head[t_face-1]==body[0][0][t_face-1]:
            if t_speed>0:
                if tail[t_face]<=head[t_face] and head[t_face]<=body[0][0][t_face]:
                    return True
            else:
                if tail[t_face]>=head[t_face] and head[t_face]>=body[0][0][t_face]:
                    return True
##            print('==tail==')
    return False    



def turn(t,move,face,speed):
    i=0
    if move[0]<time:
       i=1
       if move[1]=='L':
            if face==1:
                speed*=-1
       else:
            if face==0:
                speed*=-1      
       face=(face-1)%2
    return face,speed,i
       
##main  
N=int(sys.stdin.readline())
K=int(sys.stdin.readline())
apple=[]
for i in range(K):
    apple.append(list(map(int,sys.stdin.readline().strip().split())))


L=int(sys.stdin.readline())
move=[]
for i in range(L):
    line=sys.stdin.readline().strip().split()
    line[0]=int(line[0])
    move.append(line)

time=0
snake=[[1,1],[],[1,1]]
h_face=1
h_speed=1
t_face=1
t_speed=1
index=0
while(True):
    time+=1
    head=snake[0]
    body=snake[1]
    tail=snake[2]
    if index<L:
        h_face,h_speed,i=turn(time,move[index],h_face,h_speed)
        index+=i
        if i>0:
            body.append([head.copy(),h_face,h_speed])
    head[h_face]+=h_speed
    if game_over(snake,h_face,N,t_face,t_speed):
##        print(snake)
        break

    if eat_apple(head,apple):
        continue
    else:
        if len(body)>0:
            if tail==body[0][0]:
                t_face=body[0][1]
                t_speed=body[0][2]
                body.pop(0)
        tail[t_face]+=t_speed
##    print(body)

print(time)
