#https://www.acmicpc.net/problem/4153

while(True):
    l=input().split()
    if l==['0']*3:
        break
    for i in range(3):
        l[i]=int(l[i])
    for i in range(2):
        if l[i]>l[i+1]:
            temp=l[i]
            l[i]=l[i+1]
            l[i+1]=temp
    if l[0]*l[0]+l[1]*l[1]==l[2]*l[2]:
        print('right')
    else:
        print('wrong')
            
