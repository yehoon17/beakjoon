#https://www.acmicpc.net/problem/15953

T = int(input())

prize_a = [500, 300, 200, 50, 30, 10]
amount_a = [1, 2, 3, 4, 5, 6]
prize_b = [512, 256, 128, 64, 32]
amount_b = [1, 2, 4, 8, 16]

for _ in range(T):
    a, b = map(int, input().split())
    prize = 0
    if a > 0:
        for i in range(len(amount_a)):
            if a <= amount_a[i]:
                prize+=prize_a[i]
                break
            a-=amount_a[i]
    if b > 0:
        for i in range(len(amount_b)):
            if b <= amount_b[i]:
                prize+=prize_b[i]
                break
            b-=amount_b[i]
    
    print(prize*10000)
        
