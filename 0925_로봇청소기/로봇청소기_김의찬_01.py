# https://www.acmicpc.net/problem/4991
import sys
sys.stdin = open('input_4991.txt','r')

from itertools import permutations
from collections import deque

def copy_arr(arr):
    # 2차원 배열을 깊은 복사하여 새로운 배열 반환
    temp = [i[:] for i in arr]
    return temp

def BFS(start, end):
    # 시작점과 끝점 간의 거리 계산 함수
    # 메모이제이션을 통해 이미 계산된 거리를 사용
    if (start, end) in dist_memo:
        return dist_memo[(start, end)]

    d_que = deque()  # BFS를 위한 큐 초기화
    d_que.append((start, 0))  # 시작점과 거리 0을 큐에 추가
    copy_room = copy_arr(room)  # 방 상태를 복사
    copy_room[start[0]][start[1]] = 'x'  # 시작 위치를 방문 처리

    while d_que:
        now, dist = d_que.popleft()  # 현재 위치와 거리 가져오기
        if now == end:  # 현재 위치가 목표 위치라면
            dist_memo[(start, end)] = dist  # 거리 메모이제이션
            dist_memo[(end, start)] = dist  # 반대 방향 거리 메모이제이션
            return dist  # 거리 반환
        # 상하좌우 탐색
        for d in range(4):
            nx, ny = now[0] + dx[d], now[1] + dy[d]  # 다음 위치 계산
            # 범위 확인 및 방문 여부 확인
            if 0 <= nx < M and 0 <= ny < N and copy_room[nx][ny] != 'x':
                copy_room[nx][ny] = 'x'  # 다음 위치를 방문 처리
                d_que.append(((nx, ny), dist + 1))  # 큐에 추가

    return -1  # 도달 불가능한 경우 -1 반환

while True:
    # 입력 받기
    N, M = map(int, input().split())  # N: 열의 수, M: 행의 수
    if N == 0 and M == 0:  # 입력 종료 조건
        break
    dx = [1, 0, -1, 0]  # x 방향 (하, 우, 상, 좌)
    dy = [0, 1, 0, -1]  # y 방향 (하, 우, 상, 좌)
    dist_memo = {}  # 거리 메모이제이션 딕셔너리
    room = [list(map(str, input())) for _ in range(M)]  # 방 상태 입력받기
    dust = []  # 먼지 위치 저장 리스트

    # 방 상태에서 로봇과 먼지 위치 찾기
    for i in range(M):
        for j in range(N):
            if room[i][j] == 'o':  # 로봇 위치
                robot = (i, j)
            elif room[i][j] == '*':  # 먼지 위치
                dust.append((i, j))
    
    flag = True  # 모든 먼지에 도달 가능한지 플래그 초기화
    for check_dust in dust:
        # 로봇에서 먼지까지의 거리 계산
        check_zero = BFS(robot, check_dust)
        if check_zero == -1:  # 도달 불가능한 경우
            print(-1)  # -1 출력
            flag = False  # 플래그 변경
            break
    
    if flag:  # 모든 먼지에 도달 가능한 경우
        ans = float('inf')  # 최소 거리 초기화
        for per in permutations(dust, len(dust)):  # 먼지 순열 생성
            now_robot = robot  # 현재 로봇 위치 초기화
            temp_ans = 0  # 임시 거리 초기화
            for next in per:
                # 현재 로봇 위치에서 다음 먼지까지의 거리 계산
                temp = BFS(now_robot, next)
                temp_ans += temp  # 임시 거리 누적
                if temp_ans > ans: break  # 거리 초과 시 탐색 중단
                now_robot = next  # 로봇 위치 업데이트
            ans = min(ans, temp_ans)  # 최소 거리 업데이트
        print(ans)  # 최종 최소 거리 출력