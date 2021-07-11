#https://www.acmicpc.net/problem/16677

word = input()
N = int(input())
answer = ''
max_weight = -1
for _ in range(N):
    vocab, g = input().split()
    g = int(g)
    i = j = 0
    is_in_dic = False
    while True:
        if word[i] == vocab[j]:
            i += 1
        j += 1
        if i == len(word):
            is_in_dic = True
            break
        if j == len(vocab):
            break
    if is_in_dic:
        if max_weight < g / (len(vocab) - len(word)):
            max_weight = g / (len(vocab) - len(word))
            answer = vocab
if max_weight > 0:
    print(answer)
else:
    print("No Jam")
