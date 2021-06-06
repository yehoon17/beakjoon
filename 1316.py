#https://www.acmicpc.net/problem/1316

def isGroup(word):
    letter=[]
    for i in range(len(word)):
        if i==0:
            letter.append(word[i])
            continue
        if word[i]!=word[i-1]:
            if word[i] in letter:
                return False
            else:
                letter.append(word[i])
    return True

N=int(input())
count=0
for i in range(N):
    word=input()
    if isGroup(word):
        count+=1
print(count)
