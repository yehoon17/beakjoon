https://www.acmicpc.net/problem/1825
  
line=input().split()
N=int(line[0])
M=int(line[1])
K=int(line[2])

incr=[]
decr=[]

if N+1>=M+K and N<=M*K:
    length=N
    section=M

    while(section-1+K<=length and section>0 and K!=1):
        incr=list(range(length,length-K,-1))+incr
        length-=K
        section-=1

    if length>section:
        section-=1
        incr=list(range(length,section,-1))+incr

    incr=list(range(1,section+1))+incr

    length=N
    section=K
    start=1

    while(section-1+M<=length and section>0 and M!=1):
        decr=list(range(start,M+start))+decr
        length-=M
        section-=1
        start+=M

    if length>section:
        section-=1
        decr=list(range(start,start+length-section))+decr
        start+=length-section

    decr=list(range(N,N-section,-1))+decr

    print(*incr)
    print(*decr)

else:
    print(-1)


