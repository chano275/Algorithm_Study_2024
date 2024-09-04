# https://www.acmicpc.net/problem/1520
import sys
sys.stdin = open('input_1520.txt','r')

def DFS(x,y):
    global ans
    # 목표 지점에 도착하면 1을 반환 = 도착할 수 있다는 뜻
    if x == N-1 and y == M-1:
        return 1
    # -1이 아니라면 방문한적이 있다는 뜻 도착가능한 경우의 수 반환
    if visited[x][y] != -1:
        return visited[x][y]
    # 0으로 초기화 하여 방문한것을 표시함 / -1은 방문 X - 0은 방문했지만 갈 수 없음
    visited[x][y] = 0
    for d in range(4):
        now = groud[x][y]
        nx, ny = x+dx[d], y+dy[d]
        if 0<= nx < N and 0<= ny < M and now > groud[nx][ny]:
            # 이동 가능한 좌표들을 DFS를 통해 목표 지점에 도착가능한 모든 경우를 더해준다
            visited[x][y] += DFS(nx,ny)

    return visited[x][y]


N,M = map(int,input().split())
groud = [list(map(int,input().split())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
# 방문 여부를 확인하기 위함 + 각 칸 마다 몇개의 경우가 가능한지 count하기 위한 visited
visited = [[-1] * M for _ in range(N)]

ans = 0

print(DFS(0,0))
