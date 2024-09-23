from collections import deque


def dfs(__axy, __cleaned, _depth):
    global ans

    if _depth > ans:return
    if len(__cleaned) == len(dirty):
        ans = min(ans, _depth)
        return

    ret = bfs(__axy, __cleaned)
    if ret == -1:return

    else:
        for chk in ret:
            new_ax, new_ay, dep = chk
            __cleaned.add((new_ax, new_ay))
            dfs((new_ax, new_ay), __cleaned, _depth + dep)
            __cleaned.discard((new_ax, new_ay))

    return


def bfs(_axy, _cleaned):
    queue = deque()
    queue.append(_axy)
    depth = 0
    visited = set()

    ret_flag = 0

    nxy = set()
    while 1:
        depth += 1
        temp_queue = deque()

        while queue:
            cx, cy = queue.popleft()
            visited.add((cx, cy))
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or ny < 0 or nx >= h or ny >= w: continue
                if (nx, ny) in fur: continue
                if (nx, ny) in visited: continue
                if (nx, ny) in dirty:
                    if (nx, ny) in _cleaned:continue
                    else:
                        ret_flag = 1
                        nxy.add((nx, ny, depth))
                temp_queue.append((nx, ny))
        queue = temp_queue

        if not queue: break
    if ret_flag == 1:return nxy

    return -1


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    maps = [list(map(str, input())) for _ in range(h)]

    dirty, fur = set(), set()

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'o':
                ax, ay = i, j  # 시작점
            elif maps[i][j] == 'x':
                fur.add((i, j))  # 가구
            elif maps[i][j] == '*':
                dirty.add((i, j))  # 더러운 칸

    ans = float('inf')
    dfs((ax, ay), set(), 0)

    if ans == float('inf'):print(-1)
    else:print(ans)