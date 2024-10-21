from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def melt_cheese():
    visit = [[False] * row for _ in range(col)]
    q = deque()
    q.append((0, 0))
    visit[0][0] = True
    melted = []

    while q:
        x, y = q.popleft()

        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < col and 0 <= ny < row and not visit[nx][ny]:
                visit[nx][ny] = True

                if arr[nx][ny] == 0:  # 공기라면 큐에 추가
                    q.append((nx, ny))
                elif arr[nx][ny] == 1:  # 치즈라면 녹일 대상에 추가 치즈라면 맛있겠다...
                    melted.append((nx, ny))

    # 녹인 치즈를 배열에서 없애기
    for x, y in melted:
        arr[x][y] = 0

    return len(melted)  # 이번 턴에 녹은 치즈의 개수

# 입력 받기
col, row = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(col)]
time = 0  # 치즈가 녹는 시간
last_cheese = 0  # 마지막에 남은 치즈 조각 수

while True:
    melted_count = melt_cheese()  # 이번 턴에 녹은 치즈 수

    if melted_count == 0:
        print(time)
        print(last_cheese)
        break

    last_cheese = melted_count  # 마지막 턴에 남아 있던 치즈 수 업데이트
    time += 1  # 시간 경과