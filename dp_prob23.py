x=input()
y=input()
dp=[[0]*(len(x)+1) for _ in range(len(y)+1)]

for i in range(len(y)):
    for j in range(len(x)):
        if y[i]==x[j]:
            dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1],dp[i][j]+1)
        else:
            dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1],dp[i][j])
            

print(dp[-1][-1])
