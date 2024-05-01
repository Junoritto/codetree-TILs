N = int(input())
matrix = []
for i in range(N):
    arr = list(map(int,input().split()))
    matrix.append(arr)

dp = [[0] * N for _ in range(N)]

dp[0][0] = matrix[0][0]

for i in range(1, N):
    dp[i][0] = dp[i-1][0] + matrix[i][0]
    dp[0][i] = dp[0][i-1] + matrix[0][i]

for i in range(1,N):
    for j in range(1,N):
        dp[i][j] = max(dp[i-1][j] + matrix[i][j], dp[i][j-1] + matrix[i][j])
print(dp[N-1][N-1])