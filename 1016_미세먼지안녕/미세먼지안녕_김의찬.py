# https://www.acmicpc.net/problem/17144
import sys
# sys.stdin = open('input_17144.txt', 'r')

def spread_dust(room):
    # 먼지를 퍼뜨릴 방향 (아래, 오른쪽, 위, 왼쪽)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 먼지가 퍼진 후의 방을 저장할 새로운 배열 생성
    after_room = [[0] * C for _ in range(R)]

    # 방의 각 셀을 순회
    for i in range(R):
        for j in range(C):
            # 셀의 값이 로봇(-1), 비어있음(0), 또는 먼지가 5 미만이면 건너뜀
            if room[i][j] == -1 or room[i][j] == 0 or room[i][j] < 5:
                after_room[i][j] += room[i][j]
                continue

            count = 0  # 먼지가 퍼진 인접 셀의 수

            # 인접 셀에 먼지 퍼뜨리기
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if 0 <= nx < R and 0 <= ny < C:
                    if room[nx][ny] == -1:  # 로봇에는 먼지를 퍼뜨리지 않음
                        continue
                    after_room[nx][ny] += room[i][j] // 5  # 먼지의 1/5을 퍼뜨림
                    count += 1

            # 현재 셀에 남은 먼지 업데이트
            after_room[i][j] += room[i][j] - (room[i][j] // 5) * count

    return after_room  # 먼지가 퍼진 후의 방을 반환


def up_rotate_dust(room):
    # 먼지를 회전시킬 방향 (위, 오른쪽, 아래, 왼쪽)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir = 2  # 위쪽으로 회전 시작
    x = robot - 1  # 위쪽 로봇의 위치
    y = 0
    delete_dust = room[x][y]  # 위쪽 로봇에서 제거할 먼지

    while True:
        # 위쪽 로봇으로 돌아오면 중지
        if x == robot and y == 0:
            break

        nx, ny = x + dx[dir], y + dy[dir]

        if 0 <= nx < R and 0 <= ny < C:
            if room[nx][ny] == -1:  # 로봇에 닿으면 먼지 제거
                room[x][y] = 0
            else:
                room[x][y] = room[nx][ny]  # 다음 셀의 먼지를 이동

        nnx, nny = nx + dx[dir], ny + dy[dir]
        # 방의 경계에 닿으면 방향 변경
        if nnx < 0 or nnx > robot or nny < 0 or nny >= C:
            dir -= 1  # 왼쪽으로 회전
            if dir < 0:
                dir = 3  # 방향이 벗어나면 왼쪽으로 리셋

        x, y = nx, ny  # 현재 방향으로 다음 위치로 이동

    return delete_dust  # 위쪽 로봇에서 제거한 먼지를 반환


def down_rotate_dust(room):
    # 먼지를 회전시킬 방향 (아래, 오른쪽, 위, 왼쪽)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir = 0  # 아래쪽으로 회전 시작
    x = robot + 2  # 아래쪽 로봇의 위치
    y = 0
    delete_dust = room[x][y]  # 아래쪽 로봇에서 제거할 먼지

    while True:
        # 아래쪽 로봇으로 돌아오면 중지
        if x == robot + 1 and y == 0:
            break

        nx, ny = x + dx[dir], y + dy[dir]

        if 0 <= nx < R and 0 <= ny < C:
            if room[nx][ny] == -1:  # 로봇에 닿으면 먼지 제거
                room[x][y] = 0
            else:
                room[x][y] = room[nx][ny]  # 다음 셀의 먼지를 이동

        nnx, nny = nx + dx[dir], ny + dy[dir]
        # 방의 경계에 닿으면 방향 변경
        if nnx < robot + 1 or nnx >= R or nny < 0 or nny >= C:
            dir = (dir + 1) % 4  # 오른쪽으로 회전 (시계방향)

        x, y = nx, ny  # 현재 방향으로 다음 위치로 이동

    return delete_dust  # 아래쪽 로봇에서 제거한 먼지를 반환


# 입력 값 읽기
R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]  # 먼지 값으로 방 초기화
total_dust = 0  # 전체 먼지 수 초기화

# 방의 초기 전체 먼지 계산
for r in room:
    total_dust += sum(r)

# 두 로봇(-1)을 고려하여 2 추가
total_dust += 2

# 위쪽 로봇의 위치 찾기
for i in range(R):
    if room[i][0] == -1:
        robot = i
        break

# T 시간 단위 동안 프로세스 시뮬레이션
for time in range(T):
    room = spread_dust(room)  # 먼지 퍼뜨리기
    total_dust -= up_rotate_dust(room)  # 위쪽 로봇에서 먼지 제거
    total_dust -= down_rotate_dust(room)  # 아래쪽 로봇에서 먼지 제거

# 남은 전체 먼지 출력
print(total_dust)
