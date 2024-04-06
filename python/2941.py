#https://www.acmicpc.net/problem/2941

S=input()
count=0
i=0
while(i<len(S)):
    count+=1
    if S[i:i+3]=='dz=':
        i+=3
    elif S[i:i+2] in ('c=','c-','d-','lj','nj','s=','z='):
        i+=2
    else:
        i+=1
print(count)
