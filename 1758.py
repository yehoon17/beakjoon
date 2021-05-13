#https://www.acmicpc.net/problem/1758

N = int(input())
tips = [int(input()) for _ in range(N)]
tips.sort(reverse = True)
answer = 0
for i in range(N):
    if tips[i]-i>0:
        answer += tips[i]-i
print(answer)
