def clean(room, t):
    pass

def get_total(room):
    pass


r, c, t = map(int, input())
room = []
for _ in range(r):
    room.append(list(map(int, input().split())))
    
for _ in range(t):
    room = clean(room, t)
    
print(get_total(room))
