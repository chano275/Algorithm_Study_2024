"""
0 빈칸
1 벽 
2 바이러스 

2<= 2의 개수 <= 10 

빈칸 개수 : 3개 이상 

연구소는 크기가 N×M인 직사각형
바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.


Q1 : 모든 0에 3개씩 1 > 2 퍼지는거 체크 > 0 갯수 최대일때 출력
 ㄴ 시간이 2초인데.. 될까?

Q2 : 1에서 8방향으로 뻗을 수 있는 모든 케이스를 dfs로 체크 > 퍼지는거 체크 > 0 갯수 최대일때 출력
  ㄴ 예제 2에서 2 세로가 2줄이라고 할때, 1에서 굉장히 먼데 3개로 클리어 가능

Q3 : 2에서 뻗기? - 2에서 떨어져서 1을 깔아야 최대가 되는 경우가 있다

"""
from collections import deque
from itertools import combinations


def bfs(_arr, _visited, cxy):  # 퍼지는 코드
    cx, cy = cxy
    queue = deque()
    queue.append((cx, cy))

    while queue:
        sx, sy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = sx + dx, sy + dy

            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue  # 네모 벗어나면 ㄴㄴ
            if _arr[nx][ny] == 1 or _arr[nx][ny] == 2: continue  # 벽 / 다음 바이러스 ( 알아서 들어올거 )
            if _visited[nx][ny]: continue  # 방문했었던거면 ㄴㄴ

            queue.append((nx, ny))
            _arr[nx][ny] = 2
            _visited[nx][ny] = True

    return


dxy = [(1,0), (0,1), (-1,0), (0,-1)]
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
zeros, start_point = [], []
ans = -float('inf')

for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            zeros.append((i, j))
        elif maps[i][j] == 2:
            start_point.append((i, j))
            visited[i][j] = True

walls = list(combinations(zeros, 3))

for wall in walls:
    temp_maps = [q[:] for q in maps]
    temp_visited = [q[:] for q in visited]
    for w in wall:temp_maps[w[0]][w[1]] = 1

    # 이 전에 maps에 3개 꽂았어야 함 / 이후 근원지에서 바이러스 퍼져나가고, 이중for문 다 끝나면 0 cnt 세기
    for start in start_point:
        bfs(temp_maps, temp_visited, start)

    temp_cnt = 0

    for i in range(n):
        for j in range(m):
            if temp_maps[i][j] == 0:
                temp_cnt += 1

    ans = max(ans, temp_cnt)


print(ans)