# https://www.acmicpc.net/problem/9095

import sys

def solve(n):
    dp=[1,2,4]
    for i in range(n-3):
        dp[i%3]+=dp[i%3-1]+dp[i%3-2]
    return dp[n%3-1]

T=int(sys.stdin.readline())
for i in range(T):
    print(solve(int(sys.stdin.readline())))
