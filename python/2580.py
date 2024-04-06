#https://www.acmicpc.net/problem/2580
import sys

def search(board,i,j):
    count=[0]*10
    
    #row
    for k in range(9):
        count[board[i][k]]+=1
            
    #column     
    for k in range(9):
        count[board[k][j]]+=1
        
    #square      
    x=i//3
    y=j//3
    for n in range(3):
        for m in range(3):
            count[board[3*x+n][3*y+m]]+=1
            
    #get candidate     
    candidate=[]
    for k in range(9,0,-1):
        if count[k]==0:
            candidate.append(k)

    return candidate

def sudoku(board,blank,k):
    if k==len(blank):
        return board
    
    i,j=blank[k]
    candidate=search(board,i,j)
    if candidate:
        for x in candidate:
            board[i][j]=x
            flag=sudoku(board,blank,k+1)
            if flag:
                return flag
        else:
            board[i][j]=0
            return []
    else:
        return []


board=[]
blank=[]
for i in range(9):
    line=list(map(int,sys.stdin.readline().split()))
    board.append(line)
    for j in range(9):
        if line[j]==0:
            blank.append([i,j])

board=sudoku(board,blank,0)

for i in range(9):
    print(*board[i])
