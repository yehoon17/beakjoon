#https://www.acmicpc.net/problem/2447

def star(N,pattern):
    if N==3:
        lines=pattern.split('\n')
        edge=[]
        mid=[]
        for l in lines:
            edge.append(l*3)
            mid.append(l+' '*len(l)+l)
        newPattern=''
        for l in edge:
            newPattern+=l+'\n'
        for l in mid:
            newPattern+=l+'\n'
        for l in edge:
            newPattern+=l+'\n'
        return newPattern[:-1]
            
    else:
        return star(3,star(N/3,'*'))



N=int(input())
print(star(N,'*'))
