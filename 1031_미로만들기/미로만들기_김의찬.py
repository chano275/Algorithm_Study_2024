# https://www.acmicpc.net/problem/2665
import sys
sys.stdin = open('input_2665.txt','r')

import heapq

def BFS():
    # 상하좌우 방향 벡터
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 우선순위 큐를 위한 리스트 초기화
    h_que = []

    # 각 위치에서 검은색 칸 수의 최솟값을 저장하기 위한 배열 초기화
    cnt = [[float('inf')] * N for _ in range(N)]
    cnt[0][0] = 0  # 시작점 (0,0)에서의 검은색 칸 수는 0

    # 우선순위 큐에 (검은색 칸 수, 좌표) 튜플 추가
    heapq.heappush(h_que, (0, (0, 0)))

    while h_que:
        # 검은색 칸 수가 가장 적은 위치를 꺼냄
        black, (x, y) = heapq.heappop(h_que)

        # 도착점에 도달하면 현재 검은색 칸 수 반환
        if (x, y) == (N - 1, N - 1):
            return black

        # 현재 위치의 검은색 칸 수가 저장된 값보다 크면 무시
        if cnt[x][y] < black:
            continue

        # 4방향 탐색
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]  # 새로운 좌표 계산

            # 새로운 좌표가 유효한 범위 내에 있는지 확인
            if 0 <= nx < N and 0 <= ny < N:
                # 현재 칸이 검은색(0)인지 흰색(1)인지에 따라 검은색 칸 수 업데이트
                if maze[nx][ny] == 0:
                    black_temp = black + 1  # 검은색 칸이면 +1
                else:
                    black_temp = black  # 흰색 칸이면 그대로

                # 새로운 검은색 칸 수가 기존 값보다 작으면 업데이트
                if black_temp < cnt[nx][ny]:
                    cnt[nx][ny] = black_temp  # 최솟값 갱신
                    heapq.heappush(h_que, (black_temp, (nx, ny)))  # 큐에 추가


# 입력 크기 N과 미로 정보 입력
N = int(input())
maze = [list(map(int, input().rstrip())) for _ in range(N)]

# BFS 호출하여 결과 출력
ans = BFS()
print(ans)
