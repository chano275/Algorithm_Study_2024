from collections import deque

dxy_up = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 위 반시계
dxy_down = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 아래 시계
r, c, t = list(map(int, input().split()))
maps = [list(map(int, input().split())) for _ in range(r)]

flag = 0
for i in range(r):
    for j in range(c):
        if maps[i][j] == -1:  # 여기랑 바로 아래가 start_point
            s_01 = (i, j)
            s_02 = (i+1, j)
            flag = 1
            break
    if flag == 1: break

for _ in range(t):
    maps_copy = [row[:] for row in maps]

    ## 확산
    for i in range(r):
        for j in range(c):
            if maps[i][j] > 4:  # 4 아래면 가만히 
                for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                    nx, ny = i+dx, j+dy
                    if nx < 0 or nx >= r or ny < 0 or ny >= c or (nx, ny) in [s_01, s_02]:continue
                    maps_copy[nx][ny] += (maps[i][j] // 5)
                    maps_copy[i][j] -= (maps[i][j] // 5)
    
                    
    ## 공청 작동  /  바람분다
        # 위쪽 공기청정기 작동 (반시계 방향)
    x, y = s_01
    for i in range(c-1, 1, -1):maps_copy[x][i] = maps_copy[x][i-1]  # 오른
    for i in range(0, x):maps_copy[i][c-1] = maps_copy[i+1][c-1]    # 위
    for i in range(0, c-1):maps_copy[0][i] = maps_copy[0][i+1]      # 왼 
    for i in range(x-1, 0, -1):maps_copy[i][0] = maps_copy[i-1][0]  # 아래
    maps_copy[x][1] = 0

    # 아래쪽 공기청정기 작동 (시계 방향)
    x, y = s_02
    for i in range(c-1, 1, -1):maps_copy[x][i] = maps_copy[x][i-1]      # 오른
    for i in range(r-1, x, -1):maps_copy[i][c-1] = maps_copy[i-1][c-1]  # 아래
    for i in range(0, c-1):maps_copy[r-1][i] = maps_copy[r-1][i+1]      # 왼
    for i in range(x+1, r-1):maps_copy[i][0] = maps_copy[i+1][0]        # 위 
    maps_copy[x][1] = 0
    
    maps = [row[:] for row in maps_copy]


total_dust = sum(map(sum, maps)) + 2  # 공기청정기 위치의 -1 값을 보정
print(total_dust)
