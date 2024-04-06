#https://www.acmicpc.net/problem/1992

import sys

def get_color(l):
    size=len(l)
    color=l[0][0]
    for i in range(size):
        for j in range(size):
            if l[i][j]!=color:
                return -1
    else:
        return color

def cut(l):
    color=get_color(l)
    if color=='0':
        return '0'
    elif color=='1':
        return '1'
    else:
        size=int(len(l)/2)
        quad1=[]
        for i in range(size):
            quad1.append(l[i][:size])
        q1=cut(quad1)
        quad2=[]
        for i in range(size):
            quad2.append(l[i][size:])
        q2=cut(quad2)
        quad3=[]
        for i in range(size,2*size):
            quad3.append(l[i][:size])
        q3=cut(quad3)
        quad4=[]
        for i in range(size,2*size):
            quad4.append(l[i][size:])
        q4=cut(quad4)
        return '('+q1+q2+q3+q4+')'


N=int(sys.stdin.readline().strip())

l=[]
for i in range(N):
    line=sys.stdin.readline().strip()
    l.append(line)

print(cut(l))
