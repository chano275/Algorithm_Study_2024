def dfs(cxy, before_dxy, glass_cnt, v):
    global ans
    if cxy == st_en_point[1]:
        ans = min(ans, glass_cnt)
        return

    cx, cy = cxy

    can_go = glass_dict[before_dxy]
    for dx, dy in can_go:
        nx, ny = cx + dx, cy + dy
        if nx < 0 or ny < 0 or nx >= h or ny >= w:continue
        if maps[nx][ny] == '*': continue
        if v[nx][ny]:continue

        v[nx][ny] = True
        if (dx, dy) == before_dxy:            dfs((nx, ny), (dx, dy), glass_cnt, v)
        else:                                 dfs((nx, ny), (dx, dy), glass_cnt + 1, v)
        v[nx][ny] = False

    return


dxy = [(1,0), (0,1), (-1,0), (0,-1)]
glass_dict = {  # 90도 회전만 가능하므로, 이전 dxy에 대해 이동할 수 있는 좌표를 dict로 저장
    (1, 0): [(1, 0), (0, 1), (0, -1)],
    (0, 1): [(1, 0), (0, 1), (-1, 0)],
    (-1, 0): [(0, 1), (-1, 0), (0, -1)],
    (0, -1): [(1, 0), (-1, 0), (0, -1)],
}

w, h = map(int,input().split())
maps = [list(map(str, input())) for _ in range(h)]
visited = [[False] * w for _ in range(h)]
st_en_point = []
for i in range(h):
    for j in range(w):
        if maps[i][j] == 'C':
            st_en_point.append((i, j))

ans = float('inf')
visited[st_en_point[0][0]][st_en_point[0][1]] = True
for i in range(len(dxy)):
    dfs(st_en_point[0], dxy[i], 0, visited)

print(ans)