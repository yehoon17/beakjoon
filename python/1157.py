#https://www.acmicpc.net/problem/1157

S=input().upper()
alpha={}
for c in S:
    if c in alpha:
        alpha[c]+=1
    else:
        alpha[c]=0
max=-1
count=0
for k,v in alpha.items():
    if max<v:
        answer=k
        count=0
        max=v
    elif max==v:
        count+=1
if count==0:
    print(answer)
else:
    print('?')
