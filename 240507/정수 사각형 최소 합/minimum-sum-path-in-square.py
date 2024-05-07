N = int(input())
matrix = []
for i in range(N):
    arr = list(map(int,input().split()))
    matrix.append(arr)

dp = [[0] * N for _ in range(N)]

dp[0][N-1] = matrix[0][N-1]

for i in range(N-1):
    dp[0][N-2-i] = dp[0][N-1-i] + matrix[0][N-2-i]
    dp[i+1][N-1] = dp[i][N-1] + matrix[i+1][N-1]


for i in range(1, N):
    for j in range(N-2,-1,-1):
        dp[i][j] = min(dp[i-1][j] + matrix[i][j], dp[i][j+1] + matrix[i][j])
print(dp[N-1][0])