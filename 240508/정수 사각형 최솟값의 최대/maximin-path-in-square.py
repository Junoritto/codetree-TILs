N = int(input())
matrix = []
for _ in range(N):
    arr = list(map(int,input().split()))
    matrix.append(arr)

flag = matrix[0][0]
dp = [[flag] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if (i > 0 and j > 0):
            dp[i][j] = min(matrix[i][j], max(dp[i-1][j], dp[i][j-1]))
        elif (i == 0 and j > 0):
            dp[i][j] = min(matrix[i][j], dp[i][j-1])
        elif (i > 0 and j == 0):
            dp[i][j] = min(matrix[i][j], dp[i-1][j])
print(dp[N-1][N-1])