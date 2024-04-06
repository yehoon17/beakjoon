#https://www.acmicpc.net/problem/1427

N=input()
count=[0]*10
for c in N:
    count[int(c)]+=1
answer=''
for i in range(9,-1,-1):
    for j in range(count[i]):
        answer+=str(i)
print(answer)
