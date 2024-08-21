# https://www.acmicpc.net/problem/14502
import sys
from collections import deque
sys.stdin = open('input_14502.txt','r')

def count_safe(after_lab):
    # 안전 구역의 카운트 하는 함수
    global ans
    cnt = 0
    for line in after_lab:
        for square in line:
            if square == 0: cnt+=1
    ans = max(ans,cnt)

def BFS():
    # 바이러스가 퍼져나가는 BFS
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    # 원복하기 어려우니 복사하자
    lab_copy = [temp[:] for temp in lab]
    virus = deque()
    # 바이러스들의 좌표를 virus에 저장
    for i in range(N):
        for j in range(M):
            if lab_copy[i][j] == 2:
                virus.append((i,j))
    # 모든 바이러스 들이 퍼져 나갈 수 있는 방향으로 퍼져나감
    while virus:
        x,y = virus.popleft()
        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                # 빈 공간(안전구역)으로 바이러스가 퍼져나감
                if lab_copy[nx][ny] == 0:
                    lab_copy[nx][ny] = 2
                    virus.append((nx,ny))
    # 바이러스들이 모두 퍼져나간후 안전구역 카운팅
    count_safe(lab_copy)


def make_wall(cnt):
    # 브루트포스 벽을 세울수 있는 공간에 전부 세워보기
    if cnt == 3:
        # 벽을 3개 세웠으니 바이러스 퍼져나가자
        BFS()
        return
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                # 벽 세우기
                lab[i][j] = 1
                make_wall(cnt+1)
                # 원복
                lab[i][j] = 0

for test_case in range(3):
    N,M = map(int,input().split())
    lab = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    make_wall(0)
    print(f'#{test_case} {ans}')
