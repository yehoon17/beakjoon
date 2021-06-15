#https://www.acmicpc.net/problem/2675

N=int(input())
for i in range(N):
    line=input().split()
    repeat=int(line[0])
    answer=''
    for c in line[1]:
        for j in range(repeat):
            answer+=c
    print(answer)
