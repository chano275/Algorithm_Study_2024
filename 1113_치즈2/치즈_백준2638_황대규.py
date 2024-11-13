from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def check_air():
    air = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    air[0][0] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = True
                    air[nx][ny] = 1
                    q.append((nx, ny))
                elif arr[nx][ny] == 1: # 치즈일 경우 그냥 방문 처리
                    visited[nx][ny] = True
    return air

# 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

time = 0
while True:
    air = check_air() # 공기 전파 먼저 체크
    melt = []
    
    # 녹일 치즈 셀 찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                count = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        if air[ni][nj] == 1:
                            count += 1
                if count >= 2:
                    melt.append((i, j))
    if not melt:
        print(time)
        break
    for x, y in melt:
        arr[x][y] = 0
    time += 1