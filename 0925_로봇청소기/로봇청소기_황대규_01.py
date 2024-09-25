'''
어떤 쓰레기를 먼저 먹느냐에 따라서 이동 거리가 달라질 수 있으므로
permutation을 이용해서 순열 만들어내고 그 순서대로 bfs 진행하면서 최소거리 찾기
출발지와 도착지가 계속해서 바뀐다고 생각 그러면서 거리는 더해주기
각 점에서 각 점까지 가는 거리 구하기 어떻게??
'''
from itertools import permutations
from itertools import combinations
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(s_i, s_j, e_i, e_j):
    q = deque()
    q.append((s_i, s_j))
    visit = [[-1] * w for _ in range(len(arr))]
    visit[s_i][s_j] = 0

    while q:
        cur_x, cur_y = q.popleft()
        if cur_x == e_i and cur_y == e_j:
            break
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if visit[nx][ny] != -1 or arr[nx][ny] == 'x':
                continue

            q.append((nx, ny))
            visit[nx][ny] = visit[cur_x][cur_y] + 1
    return visit[e_i][e_j]


while True:
    w, h = map(int, input().split())
    rx, ry = 0, 0
    count = 12345678
    trash = []
    dic = {}
    if not w + h:
        break

    arr = [list(map(str, input())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 'o':
                rx, ry = i, j
                trash.insert(0, (i, j))
            elif arr[i][j] == '*':
                trash.append((i, j))

    trash_com = list(combinations(trash, 2))
    for comb in trash_com:
        s_x, s_y = comb[0]
        e_x, e_y = comb[1]
        distance = bfs(s_x, s_y, e_x, e_y)
        if distance != -1:
            dic[(s_x, s_y, e_x, e_y)] = distance
            dic[(e_x, e_y, s_x, s_y)] = distance

    del_n = trash.pop(0)
    trash_per = list(permutations(trash))
    count = float('inf')

    for perm in trash_per:
        temp = 0
        valid = True
        for idx in range(len(perm)):
            if idx == 0:
                dist = dic.get((rx, ry, perm[idx][0], perm[idx][1]), -1)
            else:
                dist = dic.get((perm[idx - 1][0], perm[idx - 1][1], perm[idx][0], perm[idx][1]), -1)

            if dist == -1:  # 경로가 없으면 더 이상 확인하지 않고 중단
                valid = False
                break
            temp += dist

        if valid:
            count = min(count, temp)

    if count == float('inf'):
        print(-1)
    else:
        print(count)
