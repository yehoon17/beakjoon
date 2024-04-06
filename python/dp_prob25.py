import sys 
N=int(sys.stdin.readline())
dp_max=[0]*3
dp_min=[0]*3
for _ in range(N):
    x=list(map(int,sys.stdin.readline().split()))
    temp=dp_max.copy()
    dp_max[0]=max(temp[:2])+x[0]
    dp_max[1]=max(temp)+x[1]
    dp_max[2]=max(temp[1:3])+x[2]
    temp=dp_min.copy()
    dp_min[0]=min(temp[:2])+x[0]
    dp_min[1]=min(temp)+x[1]
    dp_min[2]=min(temp[1:3])+x[2]
##    print(dp_min)
##    print(dp_max)
print(max(dp_max),min(dp_min))
