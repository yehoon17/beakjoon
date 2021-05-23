import sys

T=int(sys.stdin.readline())
for _ in range(T):
    n=int(sys.stdin.readline())
    stickers=[list(map(int,sys.stdin.readline().split()))+[0] for _ in range(2)]
    for i in range(1,n+1):
        if stickers[0][i-1]>stickers[0][i-2]:
            stickers[1][i]+=stickers[0][i-1]
        else:
            stickers[1][i]+=stickers[0][i-2]
        if stickers[1][i-1]>stickers[1][i-2]:
            stickers[0][i]+=stickers[1][i-1]
        else:
            stickers[0][i]+=stickers[1][i-2]
    if stickers[0][n]>stickers[1][n]:
        print(stickers[0][n])
    else:
        print(stickers[1][n])
