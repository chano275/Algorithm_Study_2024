# Q 2623. 치즈 > https://www.acmicpc.net/problem/2636

"""
예제)
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0

출력)
3
5
"""

from collections import deque

# n: 세로 크기, m: 가로 크기 입력
n, m = map(int, input().split())

# maps: 치즈가 있는 판의 정보를 저장 (0: 공기, 1: 치즈)
maps = [list(map(int, input().split())) for _ in range(n)]

# ans_time: 치즈가 녹는 데 걸린 시간, ans: 마지막에 남은 치즈 조각 수
ans_time, ans = 0, 0

# 치즈가 모두 녹을 때까지 반복
while 1:
    ans_time += 1  # 시간을 증가시킴
    visited = [[False] * m for _ in range(n)]  # 방문 여부를 기록할 배열 초기화

    ### 1. 외부 공기(테두리)와 연결된 공기 부분을 -1로 표시
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j == 0 or j == m-1:  # 테두리 부분에서 시작
                if visited[i][j] == False and maps[i][j] in {0, -1}:
                    maps[i][j] = -1  # 외부 공기는 -1로 표시
                    visited[i][j] = True

                    # BFS를 이용해 외부 공기와 연결된 모든 공기 영역을 탐색
                    queue = deque([(i, j)])
                    while queue:
                        cx, cy = queue.popleft()
                        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # 상하좌우 탐색
                            nx, ny = cx + dx, cy + dy
                            if maps[nx][ny] == 1:  # 치즈는 패스
                                continue
                            if visited[nx][ny] == False:
                                visited[nx][ny] = True
                                queue.append((nx, ny))
                                maps[nx][ny] = -1  # 외부 공기로 연결된 공기를 -1로 표시

    # 현재 상태를 저장하기 위해 maps를 복사
    maps_copy = [row[:] for row in maps]

    ### 2. 치즈가 녹을 조건을 확인하고 치즈 녹이기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:  # 치즈인 경우
                flag = 0
                # 4방향 중 외부 공기(-1)가 있으면 치즈를 녹임
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = i + dx, j + dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 범위 체크
                        continue
                    if maps[nx][ny] == -1:  # 외부 공기와 접촉한 경우
                        flag = 1
                        break

                if flag == 1:
                    maps_copy[i][j] = 0  # 치즈를 녹임 (0으로 변경)
                else:
                    maps_copy[i][j] = 1  # 그대로 유지

            else:
                maps_copy[i][j] = maps[i][j]  # 공기 또는 외부 공기는 그대로 유지

    ### 3. 남아있는 치즈가 있는지 확인
    one_flag = 0
    for p in range(n):
        for q in range(m):
            if maps_copy[p][q] == 1:  # 치즈가 남아있다면 반복 계속
                one_flag = 1
                break
        if one_flag == 1:
            break

    if one_flag == 1:
        maps = [row[:] for row in maps_copy]  # 다음 상태로 넘어감
        continue
    else:
        # 치즈가 다 녹았으면 남아있는 치즈 조각 개수 계산
        chk = 0
        for p in range(n):
            for q in range(m):
                if maps[p][q] == 1:
                    chk += 1

        ans = chk  # 마지막으로 남아있던 치즈 조각 수
        break

# 결과 출력: 치즈가 모두 녹을 때까지 걸린 시간과 마지막에 남은 치즈 조각 수
print(ans_time)
print(ans)
