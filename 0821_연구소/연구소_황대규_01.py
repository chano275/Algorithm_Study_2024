# 사방으로 퍼지니까 BFS로 풀 수 있지 않을까?
# 4행 6열을 확인할 방법은? 음 BFS를 진행하면서 count를 세는 방법?? queue에 넣을 때 마다 count 증가
# count가 하나 또는 2개인 곳에 벽을 세운다
# 1번 예시부터 안됨
# 예제 3번 대각선으로 내리는건 어떻게 할거...?
# 2번은 벽을 어디 세우길래 9개..?
# 그냥 완전 탐색?
# n과 m의 범위가 작다 = DFS로 벽 하나하나 세워보기 가능
# DFS로 벽 하나하나 세우고 BFS 돌리고 남은 애들 갯수 세아리기?
import copy
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(arr2):
    global answer
    q = deque()
    count = 0
    for (c_x, c_y) in vi_pos:
        q.append((c_x, c_y))

        while q:
            x, y = q.pop()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if arr2[nx][ny] != 0:
                    continue
                arr2[nx][ny] = 2
                q.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if arr2[i][j] == 0:
                count += 1

    answer = max(answer, count)


def dfs(depth, i, j):
    if depth == 3:
        arr2 = copy.deepcopy(arr)
        bfs(arr2)
        return

    for ii in range(i, n):
        for jj in range(j + 1, m):
            if arr[ii][jj] == 0:
                arr[ii][jj] = 1
                dfs(depth+1, ii, jj)
                arr[ii][jj] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
vi_pos = []
answer = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            vi_pos.append((i, j))

for i in range(n):
    for j in range(m):
        dfs(0, i, j)

print(answer)