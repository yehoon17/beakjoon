#https://www.acmicpc.net/problem/8958

n=int(input())
for line in range(n):
    s=input()
    count=0
    score=0
    for i in range(len(s)):
        if s[i]=='O':
            count+=1
            score+=count
        else:
            count=0
    print(score)
