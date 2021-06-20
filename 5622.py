#https://www.acmicpc.net/problem/5622

def getTime(c):
    if ord(c)<80:
        return 2+(ord(c)-62)//3
    elif ord(c)<84:
        return 8
    elif ord(c)<87:
        return 9
    else:
        return 10
    
S=input()
sum=0
for c in S:
    sum+=getTime(c)
print(sum)
