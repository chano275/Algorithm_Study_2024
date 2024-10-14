dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
air_purifier_pos = 0

for i in range(r):
    if arr[i][0] == -1:
        air_purifier_pos = i
        break


for _ in range(t):
    # 미세먼지 확산 과정
    next_arr = [arr[_][:] for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != -1:
                cur_x, cur_y = i, j

                for k in range(4):
                    nx = cur_x + dx[k]
                    ny = cur_y + dy[k]

                    if nx < 0 or ny < 0 or nx >= r or ny >= c:
                        continue
                    if (nx == air_purifier_pos and ny == 0) or (nx == air_purifier_pos + 1 and ny == 0):
                        continue
                    next_arr[nx][ny] += (arr[cur_x][cur_y]) // 5
                    next_arr[cur_x][cur_y] -= (arr[cur_x][cur_y]) // 5

    # 공기청정기 작동
    # 한단계씩 하고 나중에 develop해봅시다
    arr = [next_arr[_][:] for _ in range(r)]

    # 공기청정기 위쪽 앞으로 밀기
    next_arr[air_purifier_pos][1] = 0
    for i in range(2, c):
        next_arr[air_purifier_pos][i] = arr[air_purifier_pos][i-1]

    # 공기청정기 위쪽 위로 밀기
    for i in range(air_purifier_pos):
        next_arr[i][c-1] = arr[i+1][c-1]

    # 공기청정기 위쪽 왼쪽으로 밀기
    for i in range(c-2):
        next_arr[0][i] = arr[0][i+1]

    # 공기청정기 위쪽 아래쪽으로 밀기
    for i in range(1, air_purifier_pos):
        next_arr[i][0] = arr[i-1][0]


    # 공기청정기 아래쪽 앞으로 밀기
    next_arr[air_purifier_pos+1][1] = 0
    for i in range(2, c):
        next_arr[air_purifier_pos+1][i] = arr[air_purifier_pos+1][i - 1]

    # 공기청정기 아래쪽 밑으로 내리기
    for i in range(air_purifier_pos+2, r):
        next_arr[i][c-1] = arr[i-1][c-1]
    # 공기청정기 아래쪽 왼쪽으로 밀기
    for i in range(c-2):
        next_arr[r-1][i] = arr[r-1][i+1]

    # 공기청정기 아래쪽 위로 밀기
    for i in range(2, r-air_purifier_pos+1):
        next_arr[c-1-i][0] = arr[c-i][0]

    print(next_arr)