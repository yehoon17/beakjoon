#https://www.acmicpc.net/problem/20292

import sys

temp=[]
while True:
    line=sys.stdin.readline().strip().split()
    if line[0]=='EXIT':
        for x in temp:
            print(*x)
        print(line[0])
        break
    flag=False
    for x in temp:
        if line[0]=='READ':
            if x[0]=='WRITE':
                if x[3]==line[1]:
                    flag=True
                    break
        else:
            if x[0]=='READ':
                if x[1]==line[3]:
                    flag=True
                    break
            else:
                if line[3]==x[1] or line[3]==x[3] or line[1]==x[3]:
                    flag=True
                    break
            
    if flag:
        for x in temp:
            print(*x)
        print('WAIT')
        temp=[]
    temp.append(line)
