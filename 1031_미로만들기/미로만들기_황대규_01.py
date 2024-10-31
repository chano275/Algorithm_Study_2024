# 1번 아이디어 벽을 만나면 count 올리고 queue에 넣기
# 2번 아이디어 pop 하기전 상하좌우 다 체크 후 더하기?
# 3번 하나씩 다 부셔버리자 visit을 min값으로 교체

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

visit = [[float('inf')] * n for _ in range(n)]
visit[0][0] = 0

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 1 and visit[nx][ny] > visit[x][y]:
                visit[nx][ny] = visit[x][y]
                q.appendleft((nx, ny))
            elif arr[nx][ny] == 0 and visit[nx][ny] > visit[x][y] + 1:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))

print(visit[n - 1][n - 1])
