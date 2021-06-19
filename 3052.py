#https://www.acmicpc.net/problem/3052

d=set()
for i in range(10):
    d.add(int(input())%42)
print(len(d))
