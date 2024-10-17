import sys
from collections import deque

# BFS를 통해 공기와 접촉한 치즈를 찾아 녹이는 함수
def BFS():
    dx = [1, 0, -1, 0]  # x 방향 이동 (아래, 오른쪽, 위, 왼쪽)
    dy = [0, 1, 0, -1]  # y 방향 이동
    visited = [[False] * M for _ in range(N)]  # 방문 여부를 저장할 2D 배열
    visited[0][0] = True  # (0, 0) 좌표를 시작점으로 방문 처리
    d_que = deque()  # BFS를 위한 큐
    d_que.append((0, 0))  # 큐에 시작점 추가
    melt_cheese = []  # 녹을 치즈 좌표를 저장할 리스트

    while d_que:  # 큐가 비어있지 않으면 반복
        x, y = d_que.popleft()  # 큐에서 현재 좌표를 꺼냄
        for d in range(4):  # 4방향 탐색
            nx, ny = x + dx[d], y + dy[d]  # 다음 좌표 계산
            if 0 <= nx < N and 0 <= ny < M:  # 범위 체크
                if not visited[nx][ny]:  # 방문하지 않은 좌표인 경우
                    visited[nx][ny] = True  # 방문 처리
                    if cheese[nx][ny] == 1:  # 치즈가 있는 경우
                        melt_cheese.append((nx, ny))  # 녹을 치즈 리스트에 추가
                    else:
                        d_que.append((nx, ny))  # 빈 공간인 경우 큐에 추가

    # 녹을 치즈를 0으로 변경
    for x, y in melt_cheese:
        cheese[x][y] = 0

    return len(melt_cheese)  # 녹은 치즈의 개수 반환


# 입력 받기
N, M = map(int, input().split())  # N: 행, M: 열
cheese = [list(map(int, input().split())) for _ in range(N)]  # 치즈 배열 입력
ans = 0  # 전체 치즈 개수
time = 0  # 경과 시간

# 전체 치즈 개수 계산
for i in cheese:
    ans += sum(i)

# 치즈가 남아 있는 동안 반복
while True:
    time += 1  # 시간 증가
    temp = BFS()  # BFS를 통해 녹은 치즈의 개수 얻기
    if ans == temp:  # 남은 치즈가 없으면 종료
        break
    ans -= temp  # 남은 치즈 개수 업데이트

# 결과 출력
print(time)  # 녹는 데 걸린 시간 출력
print(ans)   # 마지막 남은 치즈의 개수 출력
