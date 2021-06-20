#https://www.acmicpc.net/problem/5086

import sys
while(True):
    line=sys.stdin.readline().strip().split()
    if line==['0','0']:
        break
    a=int(line[0])
    b=int(line[1])
    if a%b==0:
        print('multiple')
    elif b%a==0:
        print('factor')
    else:
        print('neither')
