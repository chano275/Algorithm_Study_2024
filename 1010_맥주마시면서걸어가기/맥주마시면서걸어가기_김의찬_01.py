import sys
from collections import deque

sys.stdin = open('input_9205.txt', 'r')

# 테스트 케이스의 수를 읽기
T = int(input())


def BFS(s):
    # BFS를 위한 deque 초기화 및 시작 위치 추가
    d_que = deque()
    d_que.append(s)

    # BFS 수행
    while d_que:
        # 현재 위치를 가져오기
        now_x, now_y = d_que.popleft()

        # 현재 위치가 목적지까지의 거리가 1000 이내인지 확인
        if abs(end[0] - now_x) + abs(end[1] - now_y) <= 1000:
            return "happy"  # 도달 가능하면 "happy" 반환

        # 모든 맥주 가게에 대해 반복
        for i in range(len(beer)):
            # 맥주 가게가 방문되지 않았다면
            if not visited[i]:
                # 현재 위치에서 맥주 가게까지의 거리가 1000 이내인지 확인
                if abs(beer[i][0] - now_x) + abs(beer[i][1] - now_y) <= 1000:
                    visited[i] = True  # 맥주 가게를 방문한 것으로 표시
                    d_que.append(beer[i])  # BFS 탐색을 위해 맥주 가게 추가

    return "sad"  # 도착지까지의 경로를 찾지 못하면 "sad" 반환


# 각 테스트 케이스에 대해 반복
for test_case in range(1, T + 1):
    N = int(input())  # 맥주 가게의 수를 읽기
    start = list(map(int, input().split()))  # 시작 위치의 좌표 읽기
    beer = [list(map(int, input().split())) for _ in range(N)]  # 맥주 가게의 좌표 읽기
    end = list(map(int, input().split()))  # 목적지의 좌표 읽기
    visited = [False] * len(beer)  # 맥주 가게 방문 여부 초기화

    # BFS 호출 후 결과를 출력
    print(BFS(start))
