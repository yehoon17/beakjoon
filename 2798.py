#https://www.acmicpc.net/problem/2798

line=input().split()
N=int(line[0])
M=int(line[1])
card=input().split()
for i in range(N):
    card[i]=int(card[i])
min_diff=300000
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum=card[i]+card[j]+card[k]
            if min_diff>M-sum and M>=sum:
                min_diff=M-sum
print(M-min_diff)
