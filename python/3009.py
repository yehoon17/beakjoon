#https://www.acmicpc.net/problem/3009
  
  line1=input().split()
line2=input().split()
line3=input().split()
answer=[]
for i in range(2):
    if line1[i]==line2[i]:
        answer.append(line3[i])
    elif line2[i]==line3[i]:
        answer.append(line1[i])
    else:
        answer.append(line2[i])
print(answer[0],answer[1])
