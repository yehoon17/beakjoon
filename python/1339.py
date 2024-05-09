n = int(input())
count = {}
for _ in range(n):
    s = input()
    size = len(s)
    for c in s:
        size -= 1
        if c in count:
            count[c] += 10**size
        else: 
            count[c] = 10**size
        
number = {x:9-i for i, x in enumerate(sorted(count.keys(), key=lambda x: -count[x]))}
        
total = 0
for x in count:
    total += count[x]*number[x]
    
print(total)
