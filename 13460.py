#https://www.acmicpc.net/problem/13460

import sys

def is_open(r,b,board):
    # return [above,left,below,right]
    l1=[True]*4
    l2=[True]*4
        
    for i in [-1,1]:
        if board[r[0]+i][r[1]]=='#':
            l1[1+i]=False
        if board[r[0]][r[1]+i]=='#':
            l1[2+i]=False
            
        if board[b[0]+i][b[1]]=='#':
            l2[1+i]=False
        if board[b[0]][b[1]+i]=='#':
            l2[2+i]=False

    if r[0]==b[0]:
        if r[1]-b[1]==1:
            l1[1]=False
            l2[3]=False
        
        if r[1]-b[1]==-1:
            l1[3]=False
            l2[1]=False
        
    if r[1]==b[1]:
        if r[0]-b[0]==1:
            l1[2]=False
            l2[0]=False
        
        if r[0]-b[0]==-1:
            l1[0]=False
            l2[2]=False
        
    l=[False]*4
    for i in range(4):
        if l1[i] or l2[i]:
            l[i]=True
    return l

def move_marble(board,marble,case,step):
    temp=marble.copy()
    while(True):
        temp[case+1]+=step
        c=board[temp[0]][temp[1]]
        if c=='O':
            return [-1,-1]
        elif c=='#':
            break
    temp[case+1]-=step
    return temp

def tilt(board,i,r,b):
    case=i%2-1
    step=i//2*2-1
    is_r_bigger=0
    if r[case]==b[case]:
        if r[case+1]>b[case+1]:
            is_r_bigger=1
        else:
            is_r_bigger=-1    
    temp_b=move_marble(board,b,case,step)
    temp_r=move_marble(board,r,case,step)

    if temp_b==temp_r and temp_b!=[-1,-1]:
        if step*is_r_bigger>0:
            temp_b[case+1]-=step
        else:
            temp_r[case+1]-=step

    return temp_r,temp_b
    
def solve(board,r,b,pre,count):
    # pre=0:up, 1:left, 2:down, 3:right
    if b==[-1,-1]:
        return -1
    elif r==[-1,-1]:
        return count
    elif count==10:
        return -1

        
    moves=is_open(r,b,board)
    x=-1
    if pre>0:
        x=(pre-2)%4
    temp=[]
    for i in range(4):
        if moves[i] and i!=pre and i!=x:
##            print('==============')
##            print(r,b)
            r_moved,b_moved=tilt(board,i,r,b)
##            print(r_moved,b_moved)
##            print('==============')
            temp.append(solve(board,r_moved,b_moved,i,count+1))
    
    min=11
    for i in range(len(temp)):
        if temp[i]>0:
            if min>temp[i]:
                min=temp[i]

    return min
    

##main
line=sys.stdin.readline().strip().split()
N=int(line[0])
M=int(line[1])

board=[]
for i in range(N):
    line=list(sys.stdin.readline().strip())
    for j in range(M):
        if line[j]=='O':
            o=[i,j]
        if line[j]=='R':
            r=[i,j]
            line[j]='.'
        if line[j]=='B':
            b=[i,j]
            line[j]='.'
    board.append(line)
            
temp=solve(board,r,b,-1,0)

if temp>10:
    print(-1)
else:
    print(temp)
