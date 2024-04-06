#https://www.acmicpc.net/problem/7568

N=int(input())
group=[]
for i in range(N):
    line=input().split()
    for j in range(2):
        line[j]=int(line[j])
    group.append(line)
answer=[]
for i in range(N):
    count=1
    for j in range(N):
        if i==j:
            continue
        if group[i][0]<group[j][0] and group[i][1]<group[j][1]:
            count+=1
    answer.append(str(count))
print(' '.join(answer))
