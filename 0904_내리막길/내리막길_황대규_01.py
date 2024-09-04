dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    if x == n - 1 and y == m - 1:  # 목표 지점에 도달한 경우
        return 1
    if dp[x][y] != -1:  # 이미 계산한 값이 있으면 그 값을 사용
        return dp[x][y]

    dp[x][y] = 0  # 처음 지나가는 길은 일단 0으로 초기화
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and arr[x][y] > arr[nx][ny]:
            dp[x][y] += dfs(nx, ny) # dfs가 돌아오면서 값을 채워넣으므로 print(0,0)을 진행

    return dp[x][y]


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]  # DP 배열 초기화

print(dfs(0, 0))  # (0, 0)에서 시작하여 (n-1, m-1)로 가는 경로의 수 출력
