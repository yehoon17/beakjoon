#https://www.acmicpc.net/problem/10809

S=input()
alpha=[-1]*26
answer=''
for i in range(len(S)):
    alpha[ord(S[len(S)-i-1])-97]=len(S)-i-1
for i in range(26):
    answer+=str(alpha[i])+' '
print(answer)
