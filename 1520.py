#https://www.acmicpc.net/problem/1520

def dfs(M, N, data, visited, row = 0, col = 0):
    if row == M-1 and col == N-1:
        return 1
    answer= 0
    visited[row][col]=True
    if row>0:
        if (data[row][col]>data[row-1][col] and
            not visited[row-1][col]):
            answer+=dfs(M, N, data,visited,row-1,col)
    if row<M-1:
        if (data[row][col]>data[row+1][col] and
            not visited[row+1][col]):
            answer+=dfs(M, N, data,visited,row+1,col)
    if col>0:
        if (data[row][col]>data[row][col-1] and
            not visited[row][col-1]):
            answer+=dfs(M, N, data,visited,row,col-1)
    if col<N-1:
        if (data[row][col]>data[row][col+1] and
            not visited[row][col+1]):
            answer+=dfs(M, N, data,visited,row,col+1)
    visited[row][col]=False
    return answer

M, N = map(int,input().split())
data = [list(map(int, input().split())) for _ in range(M)]
visited = [[False]*N for _ in range(M)]
print(dfs(M, N, data, visited))
