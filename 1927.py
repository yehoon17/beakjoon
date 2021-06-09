#https://www.acmicpc.net/problem/1927

import sys

def heapify(heap,i):
    size=len(heap)
    if i==0:
        while(2*i+1<=size-1):
            child=2*i+1
            if child+1<=size-1 and heap[child]>heap[child+1]:
                child+=1
            if heap[i]>heap[child]:
                heap[i],heap[child]=heap[child],heap[i]
                i=child
            else:
                break
    else:
        while(i>0):
            parent=(i-1)//2
            if heap[i]>heap[parent]:
                break
            else:
                heap[i],heap[parent]=heap[parent],heap[i]
                i=parent

heap=[]
N=int(sys.stdin.readline())
for i in range(N):
    x=int(sys.stdin.readline())
    size=len(heap)
    if x==0:
        if size==0:
            print(0)
        else:
            heap[0],heap[-1]=heap[-1],heap[0]
            print(heap.pop())
            heapify(heap,0)        
    else:
        heap.append(x)
        heapify(heap,size)
